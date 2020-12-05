import datetime

import requests
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

import api.purifyurl
import api.shortener
from .models import long_and_short


# Create your views here.

def index(request):
    form = long_and_short()
    if request.method == 'POST':
        url = request.POST['url']
        try:
            purified_url = api.purifyurl.purifyurl(url)
        except requests.exceptions.ConnectionError:
            messages.add_message(request, messages.ERROR,
                                 "This URL doesnot exist. However we have created the shortform of it for you")
            purified_url = url
        except requests.exceptions.HTTPError as msg:
            messages.add_message(request, messages.ERROR, msg)
            messages.add_message(request, messages.WARNING,
                                 "There are some problems with this URL. However we have created the shortform of it for you")
            purified_url = url

        try:
            searchforthis = long_and_short.objects.get(long_url=purified_url)
            searchforthis.duration = request.POST['duration']
            searchforthis.created = datetime.datetime.now()
            context = {
                'long': purified_url,
                'short': searchforthis.shortform,
            }
        except long_and_short.DoesNotExist:
            shortform = api.shortener.short(purified_url)
            record = long_and_short(long_url=purified_url, shortform=shortform, duration=request.POST['duration'])
            record.save()
            context = {
                'long': purified_url,
                'short': shortform,
            }
        messages.add_message(request, messages.INFO, '/' + context['short'])
    return render(request, 'index.html', context={'form': form})


def redirecturl(request, shortURL):
    try:
        objs = long_and_short.objects.get(shortform=shortURL)
        delta = datetime.timedelta(hours=float(objs.duration))

        # can't compare offset-naive and offset-aware datetimes
        # to prevent this error, passed the timezone awareness of
        # objs.created to datetime.now
        if (objs.created + delta) < datetime.datetime.now(objs.created.tzinfo):
            return HttpResponse('The Duration of this website has expired.', status=404)
        longurl = objs.long_url
        return HttpResponseRedirect(longurl)
    except long_and_short.DoesNotExist:
        return HttpResponse('This Short URL doesn\'t exist.', status=404)


def viewall(request):
    alldata = long_and_short.objects.all()
    return render(request, 'viewall.html', context={'alldata': alldata})

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

import api.purifyurl
import api.shortener
from .models import long_and_short


# Create your views here.

def index(request):
    form = long_and_short()
    # if request.method == 'GET':
    #     alltheentry = ""
    #     allrecords = long_and_short.objects.all()
    #     for record in allrecords:
    #         alltheentry += f'<p>longurl = {record.long_url}  shorturl = {record.shortform}</p>'
    #     return HttpResponse(alltheentry)
    if request.method == 'POST':
        url = request.POST['url']
        purified_url = api.purifyurl.purifyurl(url)
        try:
            searchforthis = long_and_short.objects.get(long_url=purified_url)
            context = {
                'long': purified_url,
                'short': searchforthis.shortform,
            }
        except long_and_short.DoesNotExist:
            shortform = api.shortener.short(purified_url)
            record = long_and_short(long_url=purified_url, shortform=shortform)
            record.save()
            context = {
                'long': purified_url,
                'short': shortform,
            }
        return render(request, 'success.html', context=context)
    return render(request, 'index.html', context={'form': form})


def redirecturl(request, shortURL):
    try:
        objs = long_and_short.objects.get(shortform=shortURL)
        longurl = objs.long_url
        return HttpResponseRedirect(longurl)
    except long_and_short.DoesNotExist:
        return HttpResponse('This Short URL doesn\'t exist.', status=404)

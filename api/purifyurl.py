from urllib.parse import urlparse

import requests


def testurl(url):
    try:
        url = requests.get(url)
    except requests.exceptions.ConnectionError:
        raise
    if url.ok:
        return True
    else:
        url.raise_for_status()


def schemareplace(urlobj):
    if urlobj.scheme == '':
        urlobj = urlobj._replace(scheme='http')
    elif urlobj.scheme == 'https':
        urlobj = urlobj._replace(scheme='http')
    return urlobj.geturl()


def purifyurl(url, performtest=True):
    urlobj = urlparse(url)
    if not performtest:
        return schemareplace(urlobj)
    else:
        if testurl(url):
            return schemareplace(urlobj)

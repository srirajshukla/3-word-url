from urllib.parse import urlparse


def purifyurl(url):
    urlobj = urlparse(url)
    if urlobj.scheme == '':
        urlobj._replace(scheme='http')
    elif urlobj.scheme == 'https':
        urlobj._replace(scheme='http')
    return urlobj.geturl()

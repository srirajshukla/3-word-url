from urllib.parse import urlparse


def purifyurl(url):
    urlobj = urlparse(url)
    redirecturl = ""
    if urlobj.scheme == '':
        redirecturl += "http://"
    else:
        redirecturl += urlobj.scheme + "://"
    redirecturl += urlobj.netloc + urlobj.path
    return redirecturl

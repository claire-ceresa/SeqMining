import urllib


def connected_to_internet(url):
    """
    Check connection to Internet
    :param url : the url you want to test
    :return a dictionnary {'connected':bool, 'error':string}
    """
    try:
        urllib.request.urlopen(url)
        return {'connected':True, 'error':None}
    except Exception as e:
        return {'connected':False, 'error':str(e)}

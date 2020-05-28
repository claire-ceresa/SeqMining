import urllib
import calendar
from datetime import datetime

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


def string_to_datetime(date_initial):
    abbr_month = {v: k for k, v in enumerate(calendar.month_abbr)}
    date_split = date_initial.split("-")
    day = date_split[0]
    month_letter = date_split[1].capitalize()
    month_number = abbr_month[month_letter]
    year = date_split[2]
    date_final = datetime.datetime(year=int(year), month=int(month_number), day=int(day))
    return date_final

def get_string(value):
    if isinstance(value, datetime):
        return value.strftime("%d-%m-%Y")
    elif isinstance(value, list) and isinstance(value[0], str) :
        return " , ".join(value)
    else:
        return str(value)

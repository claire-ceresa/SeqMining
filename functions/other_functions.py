from urllib import request
import calendar
import webbrowser
from datetime import datetime

def connected_to_internet(url):
    """
    Check connection to Internet
    :param url : the url you want to test
    :return a dictionnary {'connected':bool, 'error':string}
    """
    try:
        request.urlopen(url)
        return {'connected':True, 'error':None}
    except Exception as e:
        return {'connected':False, 'error':str(e)}


def open_internet(url):
    """Open a link on an Internet brower"""
    try:
        webbrowser.open(url, new=2)
    except:
        return False
    else:
        return True


def string_to_datetime(date_initial):
    abbr_month = {v: k for k, v in enumerate(calendar.month_abbr)}
    date_split = date_initial.split("-")
    day = date_split[0]
    month_letter = date_split[1].capitalize()
    month_number = abbr_month[month_letter]
    year = date_split[2]
    date_final = datetime(year=int(year), month=int(month_number), day=int(day))
    return date_final


def get_string(object):
    if isinstance(object, datetime):
        string= object.strftime("%d-%m-%Y")
    elif isinstance(object, list) and isinstance(object[0], str):
        string= " , ".join(object)
    elif isinstance(object, dict):
        string = ""
        for key, value in object.items():
            if isinstance(value, dict):
                string = string + str(key) + "\n" + get_string(value)
            else:
                string = string + str(key) + ":" + str(value) + "\n"
    else:
        string= str(object)
    return string


def extract_list_of_attribute(list_old, attribute):
    list_new = []
    for item in list_old:
        list_new.append(item[attribute])
    return list_new


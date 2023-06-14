from env.config import *

def openlink(url):

    url = url.lstrip("['")
    url = url.rstrip("']")
    
    payload = ""
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text

def clicklink(url):

    url = url.lstrip("['")
    url = url.rstrip("']")

    payload = ""
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    
    return response.text

def unsubscribelink(url):

    url = url.lstrip("['")
    url = url.rstrip("']")

    payload = ""
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    
    return response.text

def unsubscribebuttonFunction(url):

    url = url.lstrip("['")
    url = url.rstrip("']")

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text
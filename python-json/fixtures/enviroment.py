from config.config import *

def environmentURL(collectionURL):

    for localValue in localEnvJsonLoad['values']:
        if localValue['enabled']:
            if localValue['value'] != '':
                collectionURL = collectionURL.replace('{{' + localValue['key'] + '}}', str(localValue['value']))
    
    for globalValue in globalEnvJsonLoad['values']:
        if globalValue['enabled']:
            if globalValue['value'] != '':
               collectionURL = collectionURL.replace('{{' + globalValue['key'] + '}}', str(globalValue['value']))

    return collectionURL

def environmentData(collectionData):

    if 'body' in collectionData:
        
        collectionData = collectionData['body']['raw']

        for localValue in localEnvJsonLoad['values']:
            if localValue['enabled']:
                if localValue['value'] != '':
                    collectionData = collectionData.replace('{{' + localValue['key'] + '}}', str(localValue['value']))
        
        for globalValue in globalEnvJsonLoad['values']:
            if globalValue['enabled']:
                if globalValue['value'] != '':
                    collectionData = collectionData.replace('{{' + globalValue['key'] + '}}', str(globalValue['value']))
    else:
        collectionData = ''
                
    return collectionData         
    
def headerEnvironment(collectionHeaders):

    headers = {
        'Content-Type': 'application/json'
    }
    
    if 'auth' in collectionHeaders and not collectionHeaders['header']:
        if collectionHeaders['auth']['type'] == 'basic':
            headers = {
                'Authorization': 'Basic cHJveHk6b25nYWdlcWE4Ng=='
            }
        
        if collectionHeaders['auth']['type'] == 'noauth':
            headers = {} 

    if collectionHeaders['header'] and collectionHeaders['header'][0]['key'] == 'X_USERNAME':
        for localValue in localEnvJsonLoad['values']:

            if localValue['enabled']:
                for idx in range(len(collectionHeaders['header'])):
                    collectionHeaders['header'][idx]['value'] = collectionHeaders['header'][idx]['value'].replace('{{' + localValue['key'] + '}}', str(localValue['value']))

        if collectionHeaders['header'][0]['key'] == 'X_USERNAME':
            headers = {
                str(collectionHeaders['header'][0]['key']): str(collectionHeaders['header'][0]['value']),
                str(collectionHeaders['header'][1]['key']): str(collectionHeaders['header'][1]['value']),
                str(collectionHeaders['header'][2]['key']): str(collectionHeaders['header'][2]['value']),
                'Content-Type': 'application/json'
            }
    
    return headers

def getEnvironmentValue(key):
    
    for localValue in localEnvJsonLoad['values']:
        if localValue['enabled']:
            if localValue['key'] == str(key):
                return localValue['value']
             
    for globalValue in globalEnvJsonLoad['values']:
        if globalValue['enabled']:
            if globalValue['key'] == str(key):
                return globalValue['value']

    return 'Invalid Key'

def setEnvironmentValue(key, value):
    
    # Update an existing element based on its key
    for eleValue in globalEnvJsonLoad['values']:
        if eleValue["key"] == key:
            eleValue["value"] = value
            
            return globalEnvJsonLoad
    
    jsonAppendData = { 
        "key": key,
        "value": value,
        "enabled": True
    }

    globalEnvJsonLoad['values'].append(jsonAppendData)

    return jsonAppendData

def removeEnvironmentValue(key):

    value = getEnvironmentValue(key)

    jsonAppendDeleteData = { 
        "key": key,
        "value": value,
        "enabled": True
    }

    for delArr in globalEnvJsonLoad:
        if delArr == jsonAppendDeleteData:
            globalEnvJsonLoad['values'].remove(delArr)


def listToString(string):
    stringData = ""
    for stringElement in string:
        stringData += stringElement
    return stringData


def getVariablefromWebhook(responseData):
    
    if "campaign_id_all_esps_campaign_mirror_test" in responseData:
        setEnvironmentValue('campaign_id_all_esps_campaign_mirror_test', responseData["campaign_id_all_esps_campaign_mirror_test"])
    
    if responseData["mail_count"] == 1:
        setEnvironmentValue('skipRequest', 1)
        setEnvironmentValue('nextRequest', 'Clear_webhook')
    else:
        setEnvironmentValue('skipRequest', 0)
        setEnvironmentValue('nextRequest', '')

def readmail(responseData, nextRequest):

    readmailJSON = responseData.json()

    if "headerLines" in readmailJSON:

        setEnvironmentValue('skipRequest', 1)
        setEnvironmentValue('nextRequest', nextRequest)

        connectionId = getEnvironmentValue("connectionId")
        responseText = responseData.text

        tracking_url = getEnvironmentValue('tracking_url')
        fieldValue = responseText.split("~!@#~")

        #click
        sRegExpClick = '((http:\\/\\/|https?:\\/\\/)'+tracking_url+'\\/\\?xm[^\\s\\\\]+)'
        regExpClick = re.compile(sRegExpClick, re.IGNORECASE)
        
        all_esp_mirror_page_link = re.search(regExpClick, responseText).group(0)

        setEnvironmentValue('all_esp_mirror_page_link_body', fieldValue[1])
        setEnvironmentValue('all_esp_mirror_page_link', all_esp_mirror_page_link)

        setEnvironmentValue('behaviour_mail_click_link_'+connectionId, all_esp_mirror_page_link)
        
        #Open
        sRegExpOpen = '((http:\\/\\/|https?:\\/\\/)'+tracking_url+'\\/\\?xol[^\\s\\\\]+)'
        regExpOpen = re.compile(sRegExpOpen, re.IGNORECASE)

        setEnvironmentValue('behaviour_mail_open_link_'+connectionId, re.search(regExpOpen, responseText).group(0) )
        
        #Unsubscribe
        sRegExpUnsubscribe = '((http:\\/\\/|https?:\\/\\/)'+tracking_url+'\\/\\?xul[^\\s\\\\]+)'
        regExpUnsubscribe = re.compile(sRegExpUnsubscribe, re.IGNORECASE)

        setEnvironmentValue('behaviour_mail_unsub_link_'+connectionId, re.search(regExpUnsubscribe, responseText).group(0) )

    else:
        setEnvironmentValue('skipRequest', 0)
        setEnvironmentValue('nextRequest', '')

def getOldSegment(responseData, segmentName, segmentKey = ''):
    
    if 'payload' in responseData:
        for payloadValue in responseData['payload']:
            if payloadValue['name'] == segmentName:
                setEnvironmentValue(segmentKey, payloadValue['id'])

        removeEnvironmentValue('skipRequest')
        removeEnvironmentValue('nextRequest')
    else:
        setEnvironmentValue('skipRequest', 1)
        setEnvironmentValue('nextRequest', 'Behavioural stats segment')
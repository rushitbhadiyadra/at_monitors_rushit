from fixtures.enviroment import *

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

collectionJsonName = open(os.path.join(__location__, 'Collections/ALL_Esps_Transactional_Send_Message_Id_Behaviour_Stats_13230.json'), 'r')
collectionJsonDataLoad = json.load(collectionJsonName)

setEnvironmentValue('skipRequest', 0)
setEnvironmentValue('nextRequest', '')

sameRequestName = 0

for collectionJsonItem in collectionJsonDataLoad['item']:

    #Variable 
    time_30 = round(time.time()) + 30
    setEnvironmentValue('time_30', time_30)

    current_GMT = time.time()
    current_date = round(current_GMT)   
    pre_date = round(current_GMT - (24*60*60))

    setEnvironmentValue('current_date', current_date)
    setEnvironmentValue('pre_date', pre_date)
    
    # Extract request details
    requestName = collectionJsonItem['name']
    requestCollectionData = collectionJsonItem['request']
    collectionURLItem = requestCollectionData['url']['raw']
    collectionMethod = requestCollectionData['method']

    headers = headerEnvironment(requestCollectionData)
    collectionURL = environmentURL(collectionURLItem)
    collectionData = environmentData(requestCollectionData)

    #check process
    print("Running : ", requestName)
    
    skipRequest = getEnvironmentValue('skipRequest')
    nextRequest = getEnvironmentValue('nextRequest')

    # Generate Response
    if skipRequest == 0 or skipRequest == 'Invalid Key':
        response = requests.request(
            collectionMethod.lower(),
            headers=headers,
            url=collectionURL,
            data=collectionData
        )

    if skipRequest == 1:
        if nextRequest == requestName:
            print("Skipped Request ", nextRequest)
            response = requests.request(
                collectionMethod.lower(),
                headers=headers,
                url=collectionURL,
                data=collectionData
            )
            removeEnvironmentValue('skipRequest')
            removeEnvironmentValue('nextRequest')

    try:
        responseData = response.json()
        responseText = response.text

        print(requestName + " Json => ", json.dumps(responseData, indent=4) )
        
        if response.status_code == 200:
            
            connectionId = getEnvironmentValue("connectionId")
            tracking_url = getEnvironmentValue("tracking_url")
            
            if requestName == 'Create transactional campaign':
                setEnvironmentValue('all_esps_transactionsl_send_message_id_behaviour_stats_campaign_id', responseData['payload']['id'])
            
            if skipRequest == 0 or skipRequest == 'Invalid Key':
                if requestName == 'Read mail1' or requestName == 'Read mail11' :
                    if "headerLines" in responseData:

                        #Open
                        sRegExpOpen = '((http:\\/\\/|https?:\\/\\/)'+tracking_url+'\\/\\?xol[^\\s\\\\]+)'
                        regExpOpen = re.compile(sRegExpOpen, re.IGNORECASE)

                        setEnvironmentValue('behaviour_mail_open_link_'+connectionId, re.search(regExpOpen, responseText).group(0) )

                        #click
                        sRegExpClick = '((http:\\/\\/|https?:\\/\\/)'+tracking_url+'\\/\\?xm[^\\s\\\\]+)'
                        regExpClick = re.compile(sRegExpClick, re.IGNORECASE)
                        
                        setEnvironmentValue('behaviour_mail_click_link_'+connectionId, all_esp_mirror_page_link = re.search(regExpClick, responseText).group(0))
                        
                        #Unsubscribe
                        html = json.dumps(responseData['html'])

                        sRegExpUnsubscribe = '((http:\\/\\/|https?:\\/\\/)'+tracking_url+'\\/\\?xul[^\\s\\\\]+)'
                        regExpUnsubscribe = re.compile(sRegExpUnsubscribe, re.IGNORECASE)

                        setEnvironmentValue('behaviour_mail_unsub_link_'+connectionId, re.search(regExpUnsubscribe, html).group(0) )

                        setEnvironmentValue('skipRequest', 1)
                        setEnvironmentValue('nextRequest', 'Open-mail1')

                    else:
                        removeEnvironmentValue('skipRequest')
                        removeEnvironmentValue('nextRequest')
            
            
            if requestName == 'Open-mail1' :
                removeEnvironmentValue('behaviour_mail_open_link_'+connectionId)
            
            if requestName == 'Click Link1' :
                removeEnvironmentValue('behaviour_mail_click_link_'+connectionId)
            
            if requestName == 'Unsubscribe link1' :

                unsubscribe = responseText.split("~!@#~")
                
                setEnvironmentValue('rc_behaviours_stats_unsubscribe_link', "http://"+getEnvironmentValue("tracking_url")+responseText.split("'")[1])

                assert unsubscribe[1] == 'To confirm you want to unsubscribe, please click the button below', "Test failed : Test Regular Behaviours stats Unsubscribe Link Is Working"
                print('Test Passed : Test Regular Behaviours stats Unsubscribe Link Is Working') 


    except JSONDecodeError:

        responseData = json.dumps(response.text, indent=4)
        print(requestName + " Text => ", responseData )
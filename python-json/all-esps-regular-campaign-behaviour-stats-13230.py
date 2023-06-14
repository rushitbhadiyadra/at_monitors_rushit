from fixtures.enviroment import *

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

collectionJsonName = open(os.path.join(__location__, 'Collections/ALL_Esps_Regular_Campaign_Behaviour_Stats_13230.json'), 'r')
collectionJsonDataLoad = json.load(collectionJsonName)

removeEnvironmentValue('skipRequest')
removeEnvironmentValue('nextRequest')

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
            
            removeEnvironmentValue('skipRequest')
            removeEnvironmentValue('nextRequest')

            response = requests.request(
                collectionMethod.lower(),
                headers=headers,
                url=collectionURL,
                data=collectionData
            )
            
    try:
        responseData = response.json()
        responseText = response.text

        print(requestName + " Json => ", json.dumps(responseData, indent=4) )
        
        if response.status_code == 200:
            
            connectionId = getEnvironmentValue("connectionId")
            tracking_url = getEnvironmentValue("tracking_url")

            if requestName == 'Get variable from webhook':
                getVariablefromWebhook(responseData)

            if requestName == 'Get old Segment':
                segmentName = "All ESPs Behavioural stats-" + connectionId
                segmentKey = "old_segment_id_bh_state"
                getOldSegment(responseData, segmentName, segmentKey)

            if requestName == 'Delete old Segment':
                removeEnvironmentValue('old_segment_id_bh_state')
                

            if requestName == 'Behavioural stats segment':
                setEnvironmentValue('segment_id_all_esps_regular_campaign_behavioural_stat', responseData['payload']['id'])
            
            if requestName == 'Create and send campaign':
                setEnvironmentValue('all_esps_regular_campaign_behaviour_campaign_id', responseData['payload']['id'])
            
            if requestName == 'Create and send campaign':
                setEnvironmentValue('all_esps_regular_campaign_behaviour_campaign_id', responseData['payload']['id'])
            
            if requestName == 'Read mail11' or requestName == 'Read mail1' :
                
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
            
            if requestName == 'Unsubscribe link1':
                
                unsubscribe = responseText.split("~!@#~")

                if sameRequestName == 0:
                    
                    setEnvironmentValue('rc_behaviours_stats_unsubscribe_link', "http://"+tracking_url+responseText.split("'")[1])

                    assert unsubscribe[1] == 'To confirm you want to unsubscribe, please click the button below', "Test failed : Test Regular Behaviours stats Unsubscribe Link Is Working"
                    print('Test Passed : Test Regular Behaviours stats Unsubscribe Link Is Working') 

                    sameRequestName = 1

                if sameRequestName == 1:
                    
                    assert unsubscribe[1] == 'You have been successfully unsubscribed', "Test failed : Test Regular Behaviours stats Unsubscribe Is Working"
                    print('Test Passed : Test Regular Behaviours stats Unsubscribe Is Working')

                    removeEnvironmentValue('behaviour_mail_unsub_link_'+connectionId)
            
            if requestName == 'Read mail2' or requestName == 'Read mail22':
                if "headerLines" in responseData:
                    #Open
                    sRegExpOpen = '((http:\\/\\/|https?:\\/\\/)'+tracking_url+'\\/\\?xol[^\\s\\\\]+)'
                    regExpOpen = re.compile(sRegExpOpen, re.IGNORECASE)

                    setEnvironmentValue('behaviour_mail_open_link_1'+connectionId, re.search(regExpOpen, responseText).group(0) )

                    #click
                    sRegExpClick = '((http:\\/\\/|https?:\\/\\/)'+tracking_url+'\\/\\?xm[^\\s\\\\]+)'
                    regExpClick = re.compile(sRegExpClick, re.IGNORECASE)
                    
                    setEnvironmentValue('behaviour_mail_click_link_1'+connectionId, all_esp_mirror_page_link = re.search(regExpClick, responseText).group(0))
                    
                    setEnvironmentValue('skipRequest', 1)
                    setEnvironmentValue('nextRequest', 'Open-mail2')

                else:
                    removeEnvironmentValue('skipRequest')
                    removeEnvironmentValue('nextRequest')
            
            if requestName == 'Open-mail2' :
                removeEnvironmentValue('behaviour_mail_open_link_1'+connectionId)
            
            if requestName == 'Click Link2' :
                removeEnvironmentValue('behaviour_mail_click_link_1'+connectionId)
            
            if requestName == 'Read mail3' or requestName == 'Read mail33':

                if "headerLines" in responseData:

                    #Open
                    sRegExpOpen = '((http:\\/\\/|https?:\\/\\/)'+tracking_url+'\\/\\?xol[^\\s\\\\]+)'
                    regExpOpen = re.compile(sRegExpOpen, re.IGNORECASE)

                    setEnvironmentValue('behaviour_mail_open_link_2'+connectionId, re.search(regExpOpen, responseText).group(0) )

                    #click
                    sRegExpClick = '((http:\\/\\/|https?:\\/\\/)'+tracking_url+'\\/\\?xm[^\\s\\\\]+)'
                    regExpClick = re.compile(sRegExpClick, re.IGNORECASE)
                    
                    setEnvironmentValue('behaviour_mail_click_link_2'+connectionId, all_esp_mirror_page_link = re.search(regExpClick, responseText).group(0))
                    
                    setEnvironmentValue('skipRequest', 1)
                    setEnvironmentValue('nextRequest', 'Open-mail3')

                else:
                    removeEnvironmentValue('skipRequest')
                    removeEnvironmentValue('nextRequest')
            
            if requestName == 'Open-mail3' :
                removeEnvironmentValue('behaviour_mail_open_link_2'+connectionId)
            
            if requestName == 'Click Link3' :
                removeEnvironmentValue('behaviour_mail_click_link_2'+connectionId)

            
            if requestName == 'Read mail4' or requestName == 'Read mail44':

                if "headerLines" in responseData:
                    
                    #Open
                    sRegExpOpen = '((http:\\/\\/|https?:\\/\\/)'+tracking_url+'\\/\\?xol[^\\s\\\\]+)'
                    regExpOpen = re.compile(sRegExpOpen, re.IGNORECASE)

                    setEnvironmentValue('behaviour_mail_open_link_3'+connectionId, re.search(regExpOpen, responseText).group(0) )

                    #click
                    sRegExpClick = '((http:\\/\\/|https?:\\/\\/)'+tracking_url+'\\/\\?xm[^\\s\\\\]+)'
                    regExpClick = re.compile(sRegExpClick, re.IGNORECASE)
                    
                    setEnvironmentValue('behaviour_mail_click_link_3'+connectionId, all_esp_mirror_page_link = re.search(regExpClick, responseText).group(0))
                    
                    setEnvironmentValue('skipRequest', 1)
                    setEnvironmentValue('nextRequest', 'Open-mail4')

                else:
                    removeEnvironmentValue('skipRequest')
                    removeEnvironmentValue('nextRequest')
            
            if requestName == 'Open-mail4' :
                removeEnvironmentValue('behaviour_mail_open_link_3'+connectionId)
            
            if requestName == 'Click Link4' :
                removeEnvironmentValue('behaviour_mail_click_link_3'+connectionId)

            if requestName == 'RC-generate aggregate report' :

                assert int(responseData['payload'][0]['opens']) > 0, 'Test Failed : Test Regular Campaign Behavioural Open stats'
                print('Test Passed : Test Regular Campaign Behavioural Open stats')

                assert int(responseData['payload'][0]['sent']) > 0, 'Test Failed : Test Regular Campaign Behavioural Sent stats'
                print('Test Passed : Test Regular Campaign Behavioural Sent stats')

                assert int(responseData['payload'][0]['clicks']) > 0, 'Test Failed : Test Regular Campaign Behavioural Click stats'
                print('Test Passed : Test Regular Campaign Behavioural Click stats')

                assert int(responseData['payload'][0]['unsubscribes']) > 0, 'Test Failed : Test Regular Campaign Behavioural Unsubscribes stats'
                print('Test Passed : Test Regular Campaign Behavioural Unsubscribes stats')

                assert int(responseData['payload'][0]['success']) > 0, 'Test Failed : Test Regular Campaign Behavioural Success stats'
                print('Test Passed : Test Regular Campaign Behavioural Success stats')

                assert int(responseData['payload'][0]['unique_opens']) > 0, 'Test Failed : Test Regular Campaign Behavioural unique_opens stats'
                print('Test Passed : Test Regular Campaign Behavioural unique_opens stats')

                assert int(responseData['payload'][0]['unique_clicks']) > 0, 'Test Failed : Test Regular Campaign Behavioural unique_clicks stats'
                print('Test Passed : Test Regular Campaign Behavioural unique_clicks stats')
            
            if requestName == 'RC-generate Contact Activity report':

                setEnvironmentValue('all_esps_regular_campaign_behaviour_report_id', responseData['payload']['id'])
                removeEnvironmentValue('pre_date')
                removeEnvironmentValue('current_date')
            
            if requestName == 'RC-Contact Activity report result':
                
                assert int(responseData['payload'][0]['opens']) > 0, 'Test Failed : Test Regular Campaign Behavioural Open stats'
                print('Test Passed : Test Regular Campaign Behavioural Open stats')

                assert int(responseData['payload'][0]['sent']) > 0, 'Test Failed : Test Campaign Behavioural Open stats'
                print('Test Passed : Test Campaign Behavioural Sent stats')

                assert int(responseData['payload'][0]['clicks']) > 0, 'Test Failed : Test Campaign Behavioural Click stats'
                print('Test Passed : Test Campaign Behavioural Click stats')

                assert int(responseData['payload'][0]['unsubscribes']) > 0, 'Test Failed : Test Regular Campaign Behavioural Unsubscribes stats'
                print('Test Passed : Test Regular Campaign Behavioural Unsubscribes stats')

                assert int(responseData['payload'][0]['success']) > 0, 'Test Failed : Test Regular Campaign Behavioural Success stats'
                print('Test Passed : Test Regular Campaign Behavioural Success stats')

                assert int(responseData['payload'][0]['unique_opens']) > 0, 'Test Failed : Test Regular Campaign Behavioural unique_opens stats'
                print('Test Passed : Test Regular Campaign Behavioural unique_opens stats')

                assert int(responseData['payload'][0]['unique_clicks']) > 0, 'Test Failed : Test Regular Campaign Behavioural unique_clicks stats'
                print('Test Passed : Test Regular Campaign Behavioural unique_clicks stats')

                env = getEnvironmentValue("env")

                if env == "All-Esps-Dev-28299" :

                    assert str(responseData['payload'][0]['ocx_status']) == 'Unsubscribed', 'Test Failed : Test Campaign Behavioural Unsubscribes stats is equal to  contact status'
                    print('Test Passed : Test Campaign Behavioural Unsubscribes stats is equal to  contact status')

                else :
                    assert str(responseData['payload'][3]['ocx_status']) == 'Unsubscribed', 'Test Failed : Test Campaign Behavioural Unsubscribes stats is equal to  contact status'
                    print('Test Passed : Test Campaign Behavioural Unsubscribes stats is equal to  contact status')
                
                removeEnvironmentValue("all_esps_regular_campaign_behaviour_report_id")
            
            if requestName == 'Delete Segmet':
                removeEnvironmentValue("segment_id_all_esps_regular_campaign_behavioural_stat")
            

    except JSONDecodeError:

        responseData = json.dumps(response.text, indent=4)
        print(requestName + " Text => ", responseData )
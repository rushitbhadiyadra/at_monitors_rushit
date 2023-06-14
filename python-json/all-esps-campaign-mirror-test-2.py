from fixtures.enviroment import *

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

collectionJsonName = open(os.path.join(__location__, 'Collections/All_Esps_Campaign_Mirror_Test_2.json'), 'r')
collectionJsonDataLoad = json.load(collectionJsonName)

setEnvironmentValue('skipRequest', 0)
setEnvironmentValue('nextRequest', '')

skipRequest = 0

for collectionJsonItem in collectionJsonDataLoad['item']:

    #Variable 
    time_30 = round(time.time()) + 30
    setEnvironmentValue('time', time_30)
    
    # Extract request details
    requestName = collectionJsonItem['name']
    requestCollectionData = collectionJsonItem['request']
    collectionURL = requestCollectionData['url']['raw']
    collectionMethod = requestCollectionData['method']
    collectionHeaders = requestCollectionData['header']
    collectionData = requestCollectionData['body']['raw']
    
    headers = headerEnvironment(collectionHeaders)
    collectionURL = environmentURL(collectionURL)
    collectionData = environmentData(collectionData)

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
            setEnvironmentValue('skipRequest', 0)
            setEnvironmentValue('nextRequest', '')

    try:
        responseData = response.json()
        print(requestName + " Json => ", json.dumps(responseData, indent=4) )
        
        if response.status_code == 200:
            
            if requestName == 'Get variable from webhook':
                getVariablefromWebhook(responseData)

            if requestName == 'create and run campaign' :
                setEnvironmentValue('campaign_id_all_esps_campaign_mirror_test', responseData['payload']['id'])
            
            if skipRequest == 0 or skipRequest == 'Invalid Key':
                if requestName == 'readmail' :
                    readmail(response, 'Create_Segment_via_Search')
            
            if requestName == 'Create_Segment_via_Search':
                setEnvironmentValue('segment_id_all_esp_search_report', responseData['payload']['id'])

            if requestName == 'Delete_Segment_via_Search':
                removeEnvironmentValue("segment_id_all_esp_search_report")
            
            if requestName == 'Click_mail_link':

                responseText = response.text

                fieldValue = responseText.split("~!@#~")
                
                assert fieldValue[1] == getEnvironmentValue('all_esp_mirror_page_link_body'), "Test failed : Test All ESP Mirror Page Link is working"
                print('Test All ESP Mirror Page Link is working')
               
                removeEnvironmentValue("all_esp_mirror_page_link")
                removeEnvironmentValue("all_esp_mirror_page_link_body")
            
    except JSONDecodeError:

        responseData = json.dumps(response.text, indent=4)
        print(requestName + " Text => ", responseData )
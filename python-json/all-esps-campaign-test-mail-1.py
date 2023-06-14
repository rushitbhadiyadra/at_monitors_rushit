from fixtures.enviroment import *

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

collectionJsonName = open(os.path.join(__location__, 'Collections/All_Esps_Campaign_Test_Mail_1.json'), 'r')
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
        connectionId = getEnvironmentValue("connectionId")
        responseData = response.json()
        responseText = response.text
        # print(requestName + " Json => ", json.dumps(responseData, indent=4) )
        
        if response.status_code == 200:
            
            if requestName == 'Get variable from webhook':
                getVariablefromWebhook(responseData)

            if requestName == 'Send Mail' :
                setEnvironmentValue('maling_id_campaign_test_mail', responseData['payload']['id'])
            
            if skipRequest == 0 or skipRequest == 'Invalid Key':
                if requestName == 'Test-Cases' :
                    if "headerLines" in responseData:
                        setEnvironmentValue('skipRequest', 1)
                        setEnvironmentValue('nextRequest', "Click_Link")
                        setEnvironmentValue('ae_cp_test_open_link'+ connectionId, responseData['HTMLTextLinks'][0])
                        htmlText = responseData['html']
                        fieldValue = htmlText.split("~!@#~")
                        assert fieldValue[1] == "Test Mail","Test failed : Test All Esp Campaign Mail Test"
                        print("Test Passed : Test All Esp Campaign Mail Test")
                    else:
                        removeEnvironmentValue('skipRequest')
                        removeEnvironmentValue('nextRequest')                    
            
            if requestName == 'Click_Link':
                jsonData = response.text                
                assert jsonData == "ongage"
                print("Test Passed : Test All Esp Campaign Mail Test")
                removeEnvironmentValue("ae_cp_test_open_link"+connectionId)
                removeEnvironmentValue("maling_id_campaign_test_mail")            
    except JSONDecodeError:

        responseData = json.dumps(response.text, indent=4)
        print(requestName + " Text => ", responseData )
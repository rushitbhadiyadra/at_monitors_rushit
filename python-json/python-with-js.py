from fixtures.enviroment import *
import js2py

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

collectionJsonName = open(os.path.join(__location__, 'Collections/All_Esps_Campaign_Mirror_Test_2.json'), 'r')
collectionJsonDataLoad = json.load(collectionJsonName)

skipRequest = 0

for collectionJsonItem in collectionJsonDataLoad['item']:

    #Variable
    
    # Extract request details
    requestName = collectionJsonItem['name']
    requestCollectionData = collectionJsonItem['request']
    collectionURL = requestCollectionData['url']['raw']
    collectionMethod = requestCollectionData['method']
    collectionHeaders = requestCollectionData['header']
    collectionData = requestCollectionData['body']['raw']
    
    headers = headerEnvironment(requestCollectionData)
    collectionURL = environmentURL(collectionURL)
    collectionData = environmentData(requestCollectionData)

    # Generate Response
    response = requests.request(
        collectionMethod.lower(),
        headers=headers,
        url=collectionURL,
        data=collectionData
    )
    
    try:
        responseData = response.json()
        if response.status_code == 200:
            
            print(requestName + " Json => ", json.dumps(responseData, indent=4) )
            
    except JSONDecodeError:

        responseData = response.text 
        print(requestName + " Text => ", responseData )

    if "event" in collectionJsonItem:

    #     collectionEventScriptData = collectionJsonItem['event'][0]['script']['exec']
    #     collectionEventScriptString = listToString(collectionEventScriptData)

    #     jsonData = json.loads(collectionEventScriptString)
    #     exec(jsonData)

    #     jsonData = json.loads(collectionEventScriptString)
    #     print("Json => ", jsonData)

        
        collectionEventScriptData = collectionJsonItem['event'][0]['script']['exec']
        if collectionEventScriptData[0] :
            collectionEventScriptString = listToString(collectionEventScriptData)

    #         #jsonData = json.loads(collectionEventScriptString)
    #         #exec(collectionEventScriptString)

    #         #print("Text : ", collectionEventScriptString)

    #         # Create an ExecJS context
            
            js_code = """
                function runJavaScript() {
                    """+collectionEventScriptString+"""
                }

                runJavaScript();
            """

            js_code = """
            const jsonData = pm.response.json();
            pm.globals.set("all_esps_regular_campaign_behaviour_campaign_id", jsonData.all_esps_regular_campaign_behaviour_campaign_id);
            if(parseInt(jsonData.mail_count) ===1 )
            {
                postman.setNextRequest('Clear_webhook');
            }
            """

            # Create a js2py context and execute the JavaScript code
            context = js2py.EvalJs()
            context.execute(js_code)

            # Access the global variable set in the JavaScript code
            all_esps_regular_campaign_behaviour_campaign_id = context
            print(all_esps_regular_campaign_behaviour_campaign_id)


            exit()

from fixtures.delay import *
from fixtures.readmail import *
from fixtures.get_old_segment import *
from fixtures.delete_old_segment import *
from fixtures.behaviour_stats import *
from fixtures.contact_activity_report_result import *
from fixtures.delete_mail_by_id_and_subject import *
from ALL_Esps_Regular_Campaign_Behaviour_Stats_13230.create_contact import *
from ALL_Esps_Regular_Campaign_Behaviour_Stats_13230.create_segment import *
from ALL_Esps_Regular_Campaign_Behaviour_Stats_13230.create_and_send_campaign import *
from ALL_Esps_Regular_Campaign_Behaviour_Stats_13230.rc_generate_aggregate_report import *
from ALL_Esps_Regular_Campaign_Behaviour_Stats_13230.rc_generate_contact_activity_report import *
from ALL_Esps_Regular_Campaign_Behaviour_Stats_13230.remove_contact import *

deleteMailUsername = "ae_rc_bs_"+os.environ['connectionId']+"@hoohem.com"
deleteMailSubject = "Test All Esp Behavioural Stats Email-"+os.environ['connectionId']+"-"+str(os.environ['env'])

deleteMailByIdAndSubjectData = delete_mail_by_id_and_subject(deleteMailUsername, deleteMailSubject)
deleteMailByIdAndSubject = deleteMailByIdAndSubjectData.json()
print(deleteMailByIdAndSubject)

createContactData = create_contact()
createContact = createContactData.json()
print("Create Contact : ", json.dumps(createContact, indent=4) )

getOldSegmentData = get_old_segment()
getOldSegment = getOldSegmentData.json()

createSendCampaign = 0

if getOldSegmentData.status_code == 200:
    
    if len(getOldSegment['payload']) > 0:
        for segment in getOldSegment['payload']:
            if segment['name'] == "All ESPs Behavioural stats-"+os.environ['connectionId'] :
                os.environ['old_segment_id_bh_state'] = str(segment['id'])
    else:
        createSendCampaign = 1

if createSendCampaign == 0:
    if 'old_segment_id_bh_state' in os.environ:
        deleteOldSegment = delete_old_segment( (os.environ['old_segment_id_bh_state']) )
        del os.environ['old_segment_id_bh_state']

createSegmentData = create_segment()
createSegment = createSegmentData.json()
print("Create Segment : ", json.dumps(createSegment, indent=4) )

if createSegmentData.status_code == 200:
    
    connectionId = os.environ['connectionId']
    os.environ['segment_id_all_esps_regular_campaign_behavioural_stat'] = str(createSegment['payload']['id'])

    delay(29)
    delay(29)
    delay(29)
    delay(29)
    delay(29)

    createAndSendCampaignData = create_and_send_campaign()
    createAndSendCampaign = createAndSendCampaignData.json()
    print("Create And Send Campaign : ", json.dumps(createAndSendCampaign, indent=4) )

    if createAndSendCampaignData.status_code == 200:
        
        os.environ['all_esps_regular_campaign_behaviour_campaign_id'] = str(createAndSendCampaign['payload']['id'])

        delay(29)
        delay(29)
        delay(29)
        delay(29)
        delay(29)

        ##ReadMail Open Click for 1
        usernameReadMail = "ae_rc_bs_"+os.environ['connectionId']+"@hoohem.com"
        subjectReadMail = "Test All Esp Behavioural Stats Email-"+os.environ['connectionId']+"-"+os.environ['env']
        timeoutReadMail = 1200000

        readMailData = read_mail(usernameReadMail, subjectReadMail, timeoutReadMail)
        readMail = readMailData.json()
        print("Read Mail 1 : ", json.dumps(readMail, indent=4) )

        readMailCount = 0

        if readMailData.status_code == 200 :
               
            os.environ['behaviour_mail_click_link_'+os.environ['connectionId']] = str(readMail['HTMLTextLinks'])
            os.environ['behaviour_mail_open_link_'+os.environ['connectionId']] = str(readMail['HTMLOpenLinks'])
            os.environ['behaviour_mail_unsub_link_'+os.environ['connectionId']] = str(readMail['HTMLUnsubLinks'])

            readMailCount = 1
        else:
            readMailData11 = read_mail(usernameReadMail, subjectReadMail, timeoutReadMail)
            readMail11 = readMailData11.json()
            print("Read Mail 11 : ", json.dumps(readMail11, indent=4) )

            if readMailData11.status_code == 200:
                os.environ['behaviour_mail_click_link_'+os.environ['connectionId']] = str(readMail11['HTMLTextLinks'])
                os.environ['behaviour_mail_open_link_'+os.environ['connectionId']] = str(readMail11['HTMLOpenLinks'])
                os.environ['behaviour_mail_unsub_link_'+os.environ['connectionId']] = str(readMail11['HTMLUnsubLinks'])
                readMailCount = 1
            else:
                print('Read Mail 11 : Mail Not Received')

        if readMailCount == 1:

            openlink(str(os.environ['behaviour_mail_open_link_'+os.environ['connectionId']]))
            clicklink(str(os.environ['behaviour_mail_click_link_'+os.environ['connectionId']]))
            
            unsubscribelinkResponse = unsubscribelink(str(os.environ['behaviour_mail_unsub_link_'+os.environ['connectionId']]))
            
            unsubscribebutton = unsubscribelinkResponse.split("~!@#~")
            os.environ['rc_behaviours_stats_unsubscribe_link'] = "http://"+os.environ['tracking_url']+unsubscribelinkResponse.split("'")[1]
            
            if unsubscribebutton[1] == 'To confirm you want to unsubscribe, please click the button below':
                print('Unsubscribe 1 : To confirm you want to unsubscribe, please click the button below')
            else:
                print('Unsubscribe 1 : Failed')

            unsubscribeBtnFunction = unsubscribebuttonFunction(str(os.environ['rc_behaviours_stats_unsubscribe_link']))
            unsubscribebuttonText = unsubscribeBtnFunction.split("~!@#~")

            if unsubscribebuttonText[1] == 'You have been successfully unsubscribed':
                print('Unsubscribe 1 : You have been successfully unsubscribed')

            del os.environ['behaviour_mail_open_link_'+os.environ['connectionId']]
            del os.environ['behaviour_mail_click_link_'+os.environ['connectionId']]
            del os.environ['behaviour_mail_unsub_link_'+os.environ['connectionId']]
            del os.environ['rc_behaviours_stats_unsubscribe_link']

        ##ReadMail Open Click for 2
        usernameReadMail2 = "ae_rc_bs_1_"+os.environ['connectionId']+"@hoohem.com"

        readMail2Data = read_mail(usernameReadMail2, subjectReadMail, timeoutReadMail)
        readMail2 = readMail2Data.json()
        print("Read Mail 2 : ", json.dumps(readMail2, indent=4) )

        readMailCount2 = 0

        if readMail2Data.status_code == 200 :
            os.environ['behaviour_mail_open_link_1'+os.environ['connectionId']] = str(readMail2['HTMLOpenLinks'])
            os.environ['behaviour_mail_click_link_1'+os.environ['connectionId']] = str(readMail2['HTMLTextLinks'])
            readMailCount2 = 1
        else:

            readMail22Data = read_mail(usernameReadMail2, subjectReadMail, timeoutReadMail)
            readMail22 = readMail22Data.json()
            print("Read Mail 22 : ", json.dumps(readMail22, indent=4) ) 

            if readMail22Data.status_code == 200 :
                os.environ['behaviour_mail_open_link_1'+os.environ['connectionId']] = str(readMail22['HTMLOpenLinks'])
                os.environ['behaviour_mail_click_link_1'+os.environ['connectionId']] = str(readMail22['HTMLTextLinks'])
                readMailCount2 = 1
            else:
                os.environ['behaviour_mail_open_link_1'+os.environ['connectionId']] = 'https://www.lipsum.com'
                os.environ['behaviour_mail_click_link_1'+os.environ['connectionId']] = 'https://www.lipsum.com'
                readMailCount2 = 1

        if readMailCount2 == 1:
            
            openlink(str(os.environ['behaviour_mail_open_link_1'+os.environ['connectionId']]))
            clicklink(str(os.environ['behaviour_mail_click_link_1'+os.environ['connectionId']]))
            
            del os.environ['behaviour_mail_open_link_1'+os.environ['connectionId']]
            del os.environ['behaviour_mail_click_link_1'+os.environ['connectionId']]
        
        ##ReadMail Open Click for 3
        usernameReadMail3 = "ae_rc_bs_2_"+os.environ['connectionId']+"@hoohem.com"

        readMail3Data = read_mail(usernameReadMail3, subjectReadMail, timeoutReadMail)
        readMail3 = readMail3Data.json()
        print("Read Mail 3 : ", json.dumps(readMail3, indent=4) )

        readMailCount3 = 0

        if readMail3Data.status_code == 200 :    
            os.environ['behaviour_mail_open_link_2'+os.environ['connectionId']] = str(readMail3['HTMLOpenLinks'])
            os.environ['behaviour_mail_click_link_2'+os.environ['connectionId']] = str(readMail3['HTMLTextLinks'])
            readMailCount3 = 1
        else:
            readMail33Data = read_mail(usernameReadMail3, subjectReadMail, timeoutReadMail)
            readMail33 = readMail33Data.json()
            print("Read Mail 33 : ", json.dumps(readMail33, indent=4) )

            if readMail33Data.status_code == 200 :
                os.environ['behaviour_mail_open_link_2'+os.environ['connectionId']] = str(readMail33['HTMLOpenLinks'])
                os.environ['behaviour_mail_click_link_2'+os.environ['connectionId']] = str(readMail33['HTMLTextLinks'])
                readMailCount3 = 1
            else:
                os.environ['behaviour_mail_open_link_2'+os.environ['connectionId']] = 'https://www.lipsum.com'
                os.environ['behaviour_mail_click_link_2'+os.environ['connectionId']] = 'https://www.lipsum.com'
                readMailCount3 = 1

        if readMailCount3 == 1:
            openlink(str(os.environ['behaviour_mail_open_link_2'+os.environ['connectionId']]))
            clicklink(str(os.environ['behaviour_mail_click_link_2'+os.environ['connectionId']]))
            
            del os.environ['behaviour_mail_open_link_2'+os.environ['connectionId']]
            del os.environ['behaviour_mail_click_link_2'+os.environ['connectionId']]

        ##ReadMail Open Click for 4
        usernameReadMail4 = "ae_rc_bs_3_"+os.environ['connectionId']+"@hoohem.com"

        readMail4Data = read_mail(usernameReadMail4, subjectReadMail, timeoutReadMail)
        readMail4 = readMail4Data.json()
        print("Read Mail 4 : ", json.dumps(readMail4, indent=4) )

        readMailCount4 = 0
        if readMail4Data.status_code == 200 :    
            os.environ['behaviour_mail_open_link_3'+os.environ['connectionId']] = str(readMail4['HTMLOpenLinks'])
            os.environ['behaviour_mail_click_link_3'+os.environ['connectionId']] = str(readMail4['HTMLTextLinks'])
            readMailCount4 = 1
        else:
            readMail44Data = read_mail(usernameReadMail4, subjectReadMail, timeoutReadMail)
            readMail44 = readMail44Data.json()
            print("Read Mail 44 : ", json.dumps(readMail44, indent=4) )

            if readMail44Data.status_code == 200 :
                os.environ['behaviour_mail_open_link_3'+os.environ['connectionId']] = str(readMail44['HTMLOpenLinks'])
                os.environ['behaviour_mail_click_link_3'+os.environ['connectionId']] = str(readMail44['HTMLTextLinks'])
                readMailCount4 = 1
            else:
                os.environ['behaviour_mail_open_link_3'+os.environ['connectionId']] = 'https://www.lipsum.com'
                os.environ['behaviour_mail_click_link_3'+os.environ['connectionId']] = 'https://www.lipsum.com'
                readMailCount4 = 1

        if readMailCount4 == 1:

            openlink(str(os.environ['behaviour_mail_open_link_3'+os.environ['connectionId']]))
            clicklink(str(os.environ['behaviour_mail_click_link_3'+os.environ['connectionId']]))
            
            del os.environ['behaviour_mail_open_link_3'+os.environ['connectionId']]
            del os.environ['behaviour_mail_click_link_3'+os.environ['connectionId']]

        delay(29)
        delay(29)
        delay(29)
        delay(29)
        delay(29)

        generateAggregatedReportData = generate_aggregated_report()
        generateAggregatedReport = generateAggregatedReportData.json()
        print("Transactional Report : ", json.dumps(generateAggregatedReport, indent=4) )

        if generateAggregatedReportData.status_code == 200 :

            if int(generateAggregatedReport['payload'][0]['success']) > 0:
                print("Test Regular Campaign Behavioural Success stats : Passed")
            else:
                print("Test Regular Campaign Behavioural Success stats : Failed")

            if int(generateAggregatedReport['payload'][0]['opens']) > 0:
                print("Test Regular Campaign Behavioural Open stats : Passed")
            else:
                print("Test Regular Campaign Behavioural Open stats : Failed")

            if int(generateAggregatedReport['payload'][0]['sent']) > 0:
                print("Test Regular Campaign Behavioural Sent stats : Passed")
            else:
                print("Test Regular Campaign Behavioural Sent stats : Failed")

            if int(generateAggregatedReport['payload'][0]['clicks']) > 0:
                print("Test Regular Campaign Behavioural Click stats : Passed")
            else:
                print("Test Regular Campaign Behavioural Click stats : Failed")

            if int(generateAggregatedReport['payload'][0]['unsubscribes']) > 0:
                print("Test Regular Campaign Behavioural Unsubscribes stats : Passed")
            else:
                print("Test Regular Campaign Behavioural Unsubscribes stats : Failed")

            if int(generateAggregatedReport['payload'][0]['unique_opens']) > 0:
                print("Test Regular Campaign Behavioural unique_opens stats : Passed")
            else:
                print("Test Regular Campaign Behavioural unique_opens stats : Failed")

            if int(generateAggregatedReport['payload'][0]['unique_clicks']) > 0:
                print("Test Regular Campaign Behavioural unique_clicks stats : Passed")
            else:
                print("Test Regular Campaign Behavioural unique_clicks stats : Failed")

        generateContactActivityReportData = generate_contact_activity_report()
        generateContactActivityReport = generateContactActivityReportData.json()
        print("Generate Contact Activity Report : ", json.dumps(generateContactActivityReport, indent=4) )

        if generateContactActivityReportData.status_code != 200:
            print('Generate Report Failed')
        else :
            delay(29)
            delay(29)

            contactActivityReportResultData = contact_activity_report_result( str(generateContactActivityReport['payload']['id']) )
            contactActivityReportResult = contactActivityReportResultData.json()
            print("Contact Activity Report Result : ", json.dumps(contactActivityReportResult, indent=4) )

            if contactActivityReportResultData.status_code != 200:
                print('Contact Activity result Failed')
            else:

                if int(contactActivityReportResult['payload'][0]['opens']) > 0:
                    print("Test Campaign Behavioural Open stats : Passed")
                else:
                    print("Test Campaign Behavioural Open stats : Failed")
                
                if int(contactActivityReportResult['payload'][0]['sent']) > 0:
                    print("Test Campaign Behavioural Open sent : Passed")
                else:
                    print("Test Campaign Behavioural Open sent : Failed")

                if int(contactActivityReportResult['payload'][0]['clicks']) > 0:
                    print("Test Campaign Behavioural Open clicks : Passed")
                else:
                    print("Test Campaign Behavioural Open clicks : Failed")
                
                if os.environ['env'] == "All-Esps-Dev-28299" : 
                    if str(contactActivityReportResult['payload'][0]['ocx_status']) == 'Unsubscribed':
                        print("Test Campaign Behavioural Unsubscribes : Passed")
                    else:
                        print("Test Campaign Behavioural Unsubscribes : Failed")
                else:
                    if str(contactActivityReportResult['payload'][3]['ocx_status']) == 'Unsubscribed':
                        print("Test Campaign Behavioural Unsubscribes : Passed")
                    else:
                        print("Test Campaign Behavioural Unsubscribes : Failed")                

removeContactData = remove_contact()
removeContact = removeContactData.json()
print("Remove Contact : ", json.dumps(removeContact, indent=4) )

deleteOldSegmentData = delete_old_segment(os.environ['segment_id_all_esps_regular_campaign_behavioural_stat'])
deleteOldSegment = deleteOldSegmentData.json()
print("Delete segment : ", json.dumps(deleteOldSegment, indent=4) )
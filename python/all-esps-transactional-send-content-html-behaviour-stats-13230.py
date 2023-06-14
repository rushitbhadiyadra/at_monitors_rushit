from fixtures.delay import *
from fixtures.readmail import *
from fixtures.get_old_segment import *
from fixtures.delete_old_segment import *
from fixtures.behaviour_stats import *
from fixtures.contact_activity_report_result import *
from fixtures.delete_mail_by_id_and_subject import *
from fixtures.create_transactional_campaign import *
from ALL_Esps_Transactional_Send_Content_HTML_Behaviour_Stats_13230.create_contact import *
from ALL_Esps_Transactional_Send_Content_HTML_Behaviour_Stats_13230.send_embeded_mail import *
from ALL_Esps_Transactional_Send_Content_HTML_Behaviour_Stats_13230.transactional_report import *
from ALL_Esps_Transactional_Send_Content_HTML_Behaviour_Stats_13230.generate_contact_activity_report import *
from ALL_Esps_Transactional_Send_Content_HTML_Behaviour_Stats_13230.remove_contact import *

deleteMailUsername = "ae_trnsl_sd_htm_bs_"+os.environ['connectionId']+"@hoohem.com"
deleteMailSubject = "Test Transactional Send Content HTML Behavioral Stats-"+os.environ['connectionId']+"-"+str(os.environ['env'])

deleteMailByIdAndSubjectData = delete_mail_by_id_and_subject(deleteMailUsername, deleteMailSubject)
deleteMailByIdAndSubject = deleteMailByIdAndSubjectData.json()
print(deleteMailByIdAndSubject)

createContactData = create_contact()
createContact = createContactData.json()
print("Create Contact : ", json.dumps(createContact, indent=4) )

if createContactData.status_code == 200:
    delay(29)
    delay(29)

transactionalName = "All Esps Transactional Send Content HTML Behaviour Stats"
transactionalDescription = "Test Transactional Send Content HTML Behaviour Stats"

createTransactionalCampaignData = create_transactional_campaign(transactionalName, transactionalDescription)
createTransactionalCampaign = createTransactionalCampaignData.json()
print("Transactional Campaign : ", json.dumps(createTransactionalCampaign, indent=4) )

if createTransactionalCampaignData.status_code == 200:
    os.environ['all_esps_transactionsl_send_content_html_behaviour_stats_campaign_id'] = str(createTransactionalCampaign['payload']['id'])

    sendEmbededMailData = send_embeded_mail()
    sendEmbededMail = sendEmbededMailData.json()
    print("Send Embed Mail : ", json.dumps(sendEmbededMail, indent=4) )

    if sendEmbededMailData.status_code == 200:
        
        ##ReadMail for 1
        usernameReadMail = "ae_trnsl_sd_htm_bs_"+os.environ['connectionId']+"@hoohem.com"
        subjectReadMail = "Test Transactional Send Content HTML Behavioral Stats-"+os.environ['connectionId']+"-"+os.environ['env']
        timeoutReadMail = 1200000

        readMailData1 = read_mail(usernameReadMail, subjectReadMail, timeoutReadMail)
        readMail1 = readMailData1.json()
        print("Read Mail 1 : ", json.dumps(readMail1, indent=4) )

        readMailCount = 0

        if readMailData1.status_code == 200:

            os.environ['transactional_send_content_html_behaviour_stats_open_link'] = str(readMail1['HTMLOpenLinks'])
            os.environ['transactional_send_content_html_behaviour_stats_click_link'] = str(readMail1['HTMLTextLinks'])
            os.environ['transactional_send_content_html_behaviour_stats_unsub_link'] = str(readMail1['HTMLUnsubLinks'])

            readMailCount = 1
        else:
            readMailData11 = read_mail(usernameReadMail, subjectReadMail, timeoutReadMail)
            readMail11 = readMailData11.json()
            print("Read Mail 11 : ", json.dumps(readMail11, indent=4) )

            if readMailData11.status_code == 200:
                os.environ['transactional_send_content_html_behaviour_stats_open_link'] = str(readMail11['HTMLOpenLinks'])
                os.environ['transactional_send_content_html_behaviour_stats_click_link'] = str(readMail11['HTMLTextLinks'])
                os.environ['transactional_send_content_html_behaviour_stats_unsub_link'] = str(readMail11['HTMLUnsubLinks'])
                readMailCount = 1
            else:
                print('Read Mail 1 : Mail Not Received')
        
        if readMailCount == 1:

            openlink(str(os.environ['transactional_send_content_html_behaviour_stats_open_link']))
            clicklink(str(os.environ['transactional_send_content_html_behaviour_stats_click_link']))
            
            unsubscribelinkResponse = unsubscribelink(str(os.environ['transactional_send_content_html_behaviour_stats_unsub_link']))
            
            unsubscribebutton = unsubscribelinkResponse.split("~!@#~")
            transactional_send_unsubscribe_link = "http://"+os.environ['tracking_url']+unsubscribelinkResponse.split("'")[1]
            
            if unsubscribebutton[1] == 'To confirm you want to unsubscribe, please click the button below':
                print('Unsubscribe 1 : To confirm you want to unsubscribe, please click the button below')

            unsubscribeBtnFunction = unsubscribebuttonFunction(str(transactional_send_unsubscribe_link))
            unsubscribebuttonText = unsubscribeBtnFunction.split("~!@#~")

            if unsubscribebuttonText[1] == 'You have been successfully unsubscribed':
                print('Unsubscribe 1 : You have been successfully unsubscribed')
            else:
                print('Unsubscribe 1 : You have been failed to unsubscribed')

            del os.environ['transactional_send_content_html_behaviour_stats_open_link']
            del os.environ['transactional_send_content_html_behaviour_stats_click_link']
            del os.environ['transactional_send_content_html_behaviour_stats_unsub_link']

        #Read Mail For 2
        usernameReadMail2 = "ae_trnsl_sd_htm_bs_1_"+os.environ['connectionId']+"@hoohem.com"

        readMailData2 = read_mail(usernameReadMail2, subjectReadMail, timeoutReadMail)
        readMail2 = readMailData2.json()
        print("Read Mail 2 : ", json.dumps(readMail2, indent=4) )

        readMailCount = 0

        if readMailData2.status_code == 200:

            os.environ['transactional_send_content_html_behaviour_stats_open_link_1'] = str(readMail2['HTMLOpenLinks'])
            os.environ['transactional_send_content_html_behaviour_stats_click_link_1'] = str(readMail2['HTMLTextLinks'])
            
            readMailCount = 1
        else:
            readMailData22 = read_mail(usernameReadMail2, subjectReadMail, timeoutReadMail)
            readMail22 = readMailData22.json()
            print("Read Mail 22 : ", json.dumps(readMail22, indent=4) )

            if readMailData22.status_code == 200:
                os.environ['transactional_send_content_html_behaviour_stats_open_link_1'] = str(readMail22['HTMLOpenLinks'])
                os.environ['transactional_send_content_html_behaviour_stats_click_link_1'] = str(readMail22['HTMLTextLinks'])
                readMailCount = 1
            else:
                print('Read Mail 2 : Mail Not Received')
        
        if readMailCount == 1:

            openlink(str(os.environ['transactional_send_content_html_behaviour_stats_open_link_1']))
            clicklink(str(os.environ['transactional_send_content_html_behaviour_stats_click_link_1']))
            
            del os.environ['transactional_send_content_html_behaviour_stats_open_link_1']
            del os.environ['transactional_send_content_html_behaviour_stats_click_link_1']

        #Read Mail For 3
        usernameReadMail3 = "ae_trnsl_sd_htm_bs_2_"+os.environ['connectionId']+"@hoohem.com"

        readMailData3 = read_mail(usernameReadMail3, subjectReadMail, timeoutReadMail)
        readMail3 = readMailData3.json()
        print("Read Mail 3 : ", json.dumps(readMail3, indent=4) )

        readMailCount = 0

        if readMailData3.status_code == 200:

            os.environ['transactional_send_content_html_behaviour_stats_open_link_2'] = str(readMail3['HTMLOpenLinks'])
            os.environ['transactional_send_content_html_behaviour_stats_click_link_2'] = str(readMail3['HTMLTextLinks'])
            
            readMailCount = 1
        else:
            readMailData33 = read_mail(usernameReadMail3, subjectReadMail, timeoutReadMail)
            readMail33 = readMailData33.json()
            print("Read Mail 33 : ", json.dumps(readMail33, indent=4) )

            if readMailData33.status_code == 200:
                os.environ['transactional_send_content_html_behaviour_stats_open_link_2'] = str(readMail33['HTMLOpenLinks'])
                os.environ['transactional_send_content_html_behaviour_stats_click_link_2'] = str(readMail33['HTMLTextLinks'])
                readMailCount = 1
            else:
                print('Read Mail 3 : Mail Not Received')
        
        if readMailCount == 1:

            openlink(str(os.environ['transactional_send_content_html_behaviour_stats_open_link_2']))
            clicklink(str(os.environ['transactional_send_content_html_behaviour_stats_click_link_2']))
            
            del os.environ['transactional_send_content_html_behaviour_stats_open_link_2']
            del os.environ['transactional_send_content_html_behaviour_stats_click_link_2']

        #Read Mail For 4

        usernameReadMail4 = "ae_trnsl_sd_htm_bs_3_"+os.environ['connectionId']+"@hoohem.com"

        readMailData4 = read_mail(usernameReadMail4, subjectReadMail, timeoutReadMail)
        readMail4 = readMailData4.json()
        print("Read Mail 4 : ", json.dumps(readMail4, indent=4) )

        readMailCount = 0

        if readMailData4.status_code == 200:

            os.environ['transactional_send_content_html_behaviour_stats_open_link_3'] = str(readMail4['HTMLOpenLinks'])
            os.environ['transactional_send_content_html_behaviour_stats_click_link_3'] = str(readMail4['HTMLTextLinks'])
            
            readMailCount = 1
        else:
            readMailData44 = read_mail(usernameReadMail4, subjectReadMail, timeoutReadMail)
            readMail44 = readMailData44.json()
            print("Read Mail 44 : ", json.dumps(readMail44, indent=4) )

            if readMailData44.status_code == 200:
                os.environ['transactional_send_content_html_behaviour_stats_open_link_3'] = str(readMail44['HTMLOpenLinks'])
                os.environ['transactional_send_content_html_behaviour_stats_click_link_3'] = str(readMail44['HTMLTextLinks'])
                readMailCount = 1
            else:
                print('Read Mail 4 : Mail Not Received')
        
        if readMailCount == 1:

            openlink(str(os.environ['transactional_send_content_html_behaviour_stats_open_link_3']))
            clicklink(str(os.environ['transactional_send_content_html_behaviour_stats_click_link_3']))
            
            del os.environ['transactional_send_content_html_behaviour_stats_open_link_3']
            del os.environ['transactional_send_content_html_behaviour_stats_click_link_3']
            
        delay(29)
        delay(29)
        delay(29)
        delay(29)
        delay(29)

        transactionalReportData = transactional_report()
        transactionalReport = transactionalReportData.json()
        print("Transactional Report : ", json.dumps(transactionalReport, indent=4) )

        if transactionalReportData.status_code == 200 :

            TCI = os.environ['all_esps_transactionsl_send_content_html_behaviour_stats_campaign_id']

            if int(transactionalReport['payload'][0]['unique_opens']) > 0:
                print("Test Transactional Send Using HTML Message unique opens stats Transactiona Campaign Id : "+TCI+" :Passed")
            else:
                print("Test Transactional Send Using HTML Message unique opens stats Transactiona Campaign Id : "+TCI+" :Failed")

            if int(transactionalReport['payload'][0]['sent']) > 0:
                print("Test Transactional Send Using HTML Message Sent stats Transactiona Campaign Id : "+TCI+" :Passed")
            else:
                print("Test Transactional Send Using HTML Message Sent stats Transactiona Campaign Id : "+TCI+" :Failed")

            if int(transactionalReport['payload'][0]['clicks']) > 0:
                print("Test Transactional Send Using HTML Message Click stats Transactiona Campaign Id : "+TCI+" :Passed")
            else:
                print("Test Transactional Send Using HTML Message Click stats Transactiona Campaign Id : "+TCI+" :Failed")

            if int(transactionalReport['payload'][0]['unsubscribes']) > 0:
                print("Test Transactional Send Using HTML Message Unsubscribes stats Transactiona Campaign Id : "+TCI+" :Passed")
            else:
                print("Test Transactional Send Using HTML Message Unsubscribes stats Transactiona Campaign Id : "+TCI+" :Failed")

            if int(transactionalReport['payload'][0]['success']) > 0:
                print("Test Transactional Send Using HTML Message Success stats Transactiona Campaign Id : "+TCI+" :Passed")
            else:
                print("Test Transactional Send Using HTML Message Success stats Transactiona Campaign Id : "+TCI+" :Failed")

            if int(transactionalReport['payload'][0]['unique_opens']) == 4:
                print("Test Transactional Send Using HTML Message unique_opens stats : "+TCI+" :Passed")
            else:
                print("Test Transactional Send Using HTML Message unique_opens stats : "+TCI+" :Failed")

            if int(transactionalReport['payload'][0]['unique_clicks']) == 4:
                print("Test Transactional Send Using HTML Message unique_clicks stats : "+TCI+" :Passed")
            else:
                print("Test Transactional Send Using HTML Message unique_clicks stats : "+TCI+" :Failed")
        else:
            print("Failed to test Notify Transactional Message Id stats Transactiona Campaign Id ")

        generateContactActivityReportData = generate_contact_activity_report()
        generateContactActivityReport = generateContactActivityReportData.json()
        print("Generate Contact Activity Report : ", json.dumps(generateContactActivityReport, indent=4) )

        if generateContactActivityReportData.status_code != 200:
            print('Generate Report Failed')
        else:
            delay(29)
            delay(29)

            contactActivityReportResultData = contact_activity_report_result( str(generateContactActivityReport['payload']['id']) )
            contactActivityReportResult = contactActivityReportResultData.json()
            print("Contact Activity Report Result : ", json.dumps(contactActivityReportResult, indent=4) )

            if contactActivityReportResultData.status_code != 200:
                print('Contact Activity result Failed')
            else:

                TCI = os.environ['all_esps_transactionsl_send_content_html_behaviour_stats_campaign_id']
        
                if int(contactActivityReportResult['payload'][0]['opens']) > 0:
                    print("Test Transactional Send Using HTML Message Behavioural Open stats Transactiona Campaign Id : "+TCI+" :Passed")
                else:
                    print("Test Transactional Send Using HTML Message Behavioural Open stats Transactiona Campaign Id : "+TCI+" :Failed")
                
                if int(contactActivityReportResult['payload'][0]['sent']) > 0:
                    print("Test Transactional Send Using HTML Message Behavioural Sent stats Transactiona Campaign Id : "+TCI+" :Passed")
                else:
                    print("Test Transactional Send Using HTML Message Behavioural Sent stats Transactiona Campaign Id : "+TCI+" :Failed")
                
                if int(contactActivityReportResult['payload'][0]['clicks']) > 0:
                    print("Test Transactional Send Using HTML Message Behavioural Click stats Transactiona Campaign Id : "+TCI+" :Passed")
                else:
                    print("Test Transactional Send Using HTML Message Behavioural Click stats Transactiona Campaign Id : "+TCI+" :Failed")
                
                if str(os.environ['env']) == "All-Esps-Dev-28299":
                    if str(contactActivityReportResult['payload'][0]['ocx_status']) == 'Unsubscribed':
                        print("Test Transactional Send Using HTML Message Behavioural Unsubscribes stats is equal to contact status Transactiona Campaign Id : "+TCI+" :Passed")
                    else:
                        print("Test Transactional Send Using HTML Message Behavioural Unsubscribes stats is equal to contact status Transactiona Campaign Id : "+TCI+" :Failed")
                else:
                    if str(contactActivityReportResult['payload'][3]['ocx_status']) == 'Unsubscribed':
                        print("Test Transactional Send Using HTML Message Behavioural Unsubscribes stats is equal to contact status Transactiona Campaign Id : "+TCI+" :Passed")
                    else:
                        print("Test Transactional Send Using HTML Message Behavioural Unsubscribes stats is equal to contact status Transactiona Campaign Id : "+TCI+" :Failed")

                del os.environ['all_esps_transactionsl_send_content_html_behaviour_stats_campaign_id']

removeContactData = remove_contact()
removeContact = removeContactData.json()
print("Remove Contact Result : ", json.dumps(removeContact, indent=4) )
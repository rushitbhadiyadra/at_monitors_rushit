from fixtures.delay import *
from fixtures.readmail import *
from fixtures.behaviour_stats import *
from fixtures.contact_activity_report_result import *
from fixtures.delete_mail_by_id_and_subject import *
from ALL_Esps_Transactional_Send_Message_Id_Behaviour_Stats_13230.create_contact import *
from ALL_Esps_Transactional_Send_Message_Id_Behaviour_Stats_13230.change_contact_status import *
from ALL_Esps_Transactional_Send_Message_Id_Behaviour_Stats_13230.create_transactional_campaign import *
from ALL_Esps_Transactional_Send_Message_Id_Behaviour_Stats_13230.send_mail import *
from ALL_Esps_Transactional_Send_Message_Id_Behaviour_Stats_13230.transactional_report import *
from ALL_Esps_Transactional_Send_Message_Id_Behaviour_Stats_13230.generate_contact_activity_report import *
from ALL_Esps_Transactional_Send_Message_Id_Behaviour_Stats_13230.remove_contact import *

deleteMailUsername = "ae_trnsl_sd_mail_bs_"+os.environ['connectionId']+"@hoohem.com"
deleteMailSubject = "Test All Esp Behavioural Stats Email and unsubscribed link-"+os.environ['connectionId']+"-"+str(os.environ['env'])

deleteMailByIdAndSubjectData = delete_mail_by_id_and_subject(deleteMailUsername, deleteMailSubject)
deleteMailByIdAndSubject = deleteMailByIdAndSubjectData.json()

contactStatus = change_contact_status()
createContactData = create_contact()
createContact = createContactData.json()

if createContactData.status_code == 200:
    delay(29)
    delay(29)

createTransactionalCampaignData = create_transactional_campaign()
createTransactionalCampaign = createTransactionalCampaignData.json()
print(createTransactionalCampaign)
os.environ['all_esps_transactional_send_message_id_behaviour_stats_campaign_id'] = str(createTransactionalCampaign['payload']['id'])

sendMailData = sendMail()
sendMailJson = sendMailData.json()
print(sendMailJson)

if sendMailData.status_code == 200:

    ##ReadMail Open Click for 1
    usernameReadMail = "ae_trnsl_sd_mail_bs_"+os.environ['connectionId']+"@hoohem.com"
    subjectReadMail = "Test All Esp Behavioural Stats Email and unsubscribed link-"+os.environ['connectionId']+"-"+os.environ['env']
    timeoutReadMail = 120000

    readMailData = read_mail(usernameReadMail, subjectReadMail, timeoutReadMail)
    readMail = readMailData.json()
    print("Read Mail 1 : ", json.dumps(readMail, indent=4) )

    readMailCount = 0

    if readMailData.status_code == 200 :    
        os.environ['tc_send_message_id_behaviour_stats_click_link'] = str(readMail['HTMLTextLinks'])
        os.environ['tc_send_message_id_behaviour_stats_open_link'] = str(readMail['HTMLOpenLinks'])
        os.environ['tc_send_message_id_behaviour_stats_unsub_link'] = str(readMail['HTMLUnsubLinks'])

        readMailCount = 1
    else:
        readMailData11 = read_mail(usernameReadMail, subjectReadMail, timeoutReadMail)
        readMail11 = readMailData11.json()
        print("Read Mail 11 : ", json.dumps(readMail11, indent=4) )

        if readMailData11.status_code == 200:
            os.environ['tc_send_message_id_behaviour_stats_click_link'] = str(readMail11['HTMLTextLinks'])
            os.environ['tc_send_message_id_behaviour_stats_open_link'] = str(readMail11['HTMLOpenLinks'])
            os.environ['tc_send_message_id_behaviour_stats_unsub_link'] = str(readMail11['HTMLUnsubLinks'])
            readMailCount = 1
        else:
            print('Read Mail 11 : Mail Not Received')

    if readMailCount == 1:

        openlink(str(os.environ['tc_send_message_id_behaviour_stats_open_link']))
        clicklink(str(os.environ['tc_send_message_id_behaviour_stats_click_link']))
        
        unsubscribelinkResponse = unsubscribelink(str(os.environ['tc_send_message_id_behaviour_stats_unsub_link']))
        
        unsubscribebutton = unsubscribelinkResponse.split("~!@#~")
        os.environ['tc_send_email_unsubscribebutton_link'] = "http://"+os.environ['tracking_url']+unsubscribelinkResponse.split("'")[1]
        
        if unsubscribebutton[1] == 'To confirm you want to unsubscribe, please click the button below':
            print('Unsubscribe 1 : To confirm you want to unsubscribe, please click the button below')
        else:
            print('Unsubscribe 1 : Failed')

        unsubscribeBtnFunction = unsubscribebuttonFunction(str(os.environ['tc_send_email_unsubscribebutton_link']))
        unsubscribebuttonText = unsubscribeBtnFunction.split("~!@#~")

        if unsubscribebuttonText[1] == 'You have been successfully unsubscribed':
            print('Unsubscribe 1 : You have been successfully unsubscribed')

        del os.environ['tc_send_message_id_behaviour_stats_click_link']
        del os.environ['tc_send_message_id_behaviour_stats_open_link']
        del os.environ['tc_send_message_id_behaviour_stats_unsub_link']
        del os.environ['tc_send_email_unsubscribebutton_link']

    ##ReadMail Open Click for 2
    usernameReadMail2 = "ae_trnsl_sd_mail_bs_1_"+os.environ['connectionId']+"@hoohem.com"

    readMail2Data = read_mail(usernameReadMail2, subjectReadMail, timeoutReadMail)
    readMail2 = readMail2Data.json()
    print("Read Mail 2 : ", json.dumps(readMail2, indent=4) )

    readMailCount2 = 0

    if readMail2Data.status_code == 200 :
        os.environ['tc_send_message_id_behaviour_stats_click_link_2'] = str(readMail2['HTMLTextLinks'])
        os.environ['tc_send_message_id_behaviour_stats_open_link_2'] = str(readMail2['HTMLOpenLinks'])
        os.environ['tc_send_message_id_behaviour_stats_unsub_link_2'] = str(readMail2['HTMLUnsubLinks'])
        readMailCount2 = 1
    else:

        readMail22Data = read_mail(usernameReadMail2, subjectReadMail, timeoutReadMail)
        readMail22 = readMail22Data.json()
        print("Read Mail 22 : ", json.dumps(readMail22, indent=4) ) 

        if readMail22Data.status_code == 200 :
            os.environ['tc_send_message_id_behaviour_stats_open_link_2'] = str(readMail22['HTMLOpenLinks'])
            os.environ['tc_send_message_id_behaviour_stats_click_link_2'] = str(readMail22['HTMLTextLinks'])
            os.environ['tc_send_message_id_behaviour_stats_unsub_link_2'] = str(readMail22['HTMLUnsubLinks'])
            readMailCount2 = 1
        else:
            print('Read Mail 2 : Mail Not Received')

    if readMailCount2 == 1:
        openlink(str(os.environ['tc_send_message_id_behaviour_stats_open_link_2']))
        clicklink(str(os.environ['tc_send_message_id_behaviour_stats_click_link_2']))
        unsubscribelinkResponse = unsubscribelink(str(os.environ['tc_send_message_id_behaviour_stats_unsub_link_2']))
        unsubscribebutton = unsubscribelinkResponse.split("~!@#~")
        os.environ['tc_send_email_unsubscribebutton_link_2'] = "http://"+os.environ['tracking_url']+unsubscribelinkResponse.split("'")[1]
        
        if unsubscribebutton[1] == 'To confirm you want to unsubscribe, please click the button below':
            print('Unsubscribe 2 : To confirm you want to unsubscribe, please click the button below')
        else:
            print('Unsubscribe 2 : Failed')

        unsubscribeBtnFunction = unsubscribebuttonFunction(str(os.environ['tc_send_email_unsubscribebutton_link_2']))
        unsubscribebuttonText = unsubscribeBtnFunction.split("~!@#~")

        if unsubscribebuttonText[1] == 'You have been successfully unsubscribed':
            print('Unsubscribe 2 : You have been successfully unsubscribed')

        del os.environ['tc_send_message_id_behaviour_stats_open_link_2']
        del os.environ['tc_send_message_id_behaviour_stats_click_link_2']
        del os.environ['tc_send_message_id_behaviour_stats_unsub_link_2']
        del os.environ['tc_send_email_unsubscribebutton_link_2']

    ##ReadMail Open Click for 3
    usernameReadMail3 = "ae_trnsl_sd_mail_bs_2_"+os.environ['connectionId']+"@hoohem.com"

    readMail3Data = read_mail(usernameReadMail3, subjectReadMail, timeoutReadMail)
    readMail3 = readMail3Data.json()
    print("Read Mail 3 : ", json.dumps(readMail3, indent=4) )

    readMailCount3 = 0

    if readMail3Data.status_code == 200 :    
        os.environ['tc_send_message_id_behaviour_stats_click_link_3'] = str(readMail3['HTMLTextLinks'])
        os.environ['tc_send_message_id_behaviour_stats_open_link_3'] = str(readMail3['HTMLOpenLinks'])
        os.environ['tc_send_message_id_behaviour_stats_unsub_link_3'] = str(readMail3['HTMLUnsubLinks'])
        readMailCount3 = 1
    else:
        readMail33Data = read_mail(usernameReadMail3, subjectReadMail, timeoutReadMail)
        readMail33 = readMail33Data.json()
        print("Read Mail 33 : ", json.dumps(readMail33, indent=4) )

        if readMail33Data.status_code == 200 :
            os.environ['tc_send_message_id_behaviour_stats_open_link_3'] = str(readMail33['HTMLOpenLinks'])
            os.environ['tc_send_message_id_behaviour_stats_click_link_3'] = str(readMail33['HTMLTextLinks'])
            os.environ['tc_send_message_id_behaviour_stats_unsub_link_3'] = str(readMail33['HTMLUnsubLinks'])

            readMailCount3 = 1
        else:
            print('Read Mail 3 : Mail Not Received')

    if readMailCount3 == 1:
        openlink(str(os.environ['tc_send_message_id_behaviour_stats_open_link_3']))
        clicklink(str(os.environ['tc_send_message_id_behaviour_stats_click_link_3']))
        
        unsubscribelinkResponse = unsubscribelink(str(os.environ['tc_send_message_id_behaviour_stats_unsub_link_3']))

        unsubscribebutton = unsubscribelinkResponse.split("~!@#~")
        os.environ['tc_send_email_unsubscribebutton_link_3'] = "http://"+os.environ['tracking_url']+unsubscribelinkResponse.split("'")[1]
        
        if unsubscribebutton[1] == 'To confirm you want to unsubscribe, please click the button below':
            print('Unsubscribe 3 : To confirm you want to unsubscribe, please click the button below')
        else:
            print('Unsubscribe 3 : Failed')

        unsubscribeBtnFunction = unsubscribebuttonFunction(str(os.environ['tc_send_email_unsubscribebutton_link_3']))
        unsubscribebuttonText = unsubscribeBtnFunction.split("~!@#~")

        if unsubscribebuttonText[1] == 'You have been successfully unsubscribed':
            print('Unsubscribe 3 : You have been successfully unsubscribed')

        del os.environ['tc_send_message_id_behaviour_stats_open_link_3']
        del os.environ['tc_send_message_id_behaviour_stats_click_link_3']
        del os.environ['tc_send_message_id_behaviour_stats_unsub_link_3']
        del os.environ['tc_send_email_unsubscribebutton_link_3']

    ##ReadMail Open Click for 4
    usernameReadMail4 = "ae_trnsl_sd_mail_bs_3_"+os.environ['connectionId']+"@hoohem.com"

    readMail4Data = read_mail(usernameReadMail4, subjectReadMail, timeoutReadMail)
    readMail4 = readMail4Data.json()
    print("Read Mail 4 : ", json.dumps(readMail4, indent=4) )

    readMailCount4 = 0
    if readMail4Data.status_code == 200 :    
        os.environ['tc_send_message_id_behaviour_stats_click_link_4'] = str(readMail4['HTMLTextLinks'])
        os.environ['tc_send_message_id_behaviour_stats_open_link_4'] = str(readMail4['HTMLOpenLinks'])
        os.environ['tc_send_message_id_behaviour_stats_unsub_link_4'] = str(readMail4['HTMLUnsubLinks'])
        readMailCount4 = 1
    else:
        readMail44Data = read_mail(usernameReadMail4, subjectReadMail, timeoutReadMail)
        readMail44 = readMail44Data.json()
        print("Read Mail 44 : ", json.dumps(readMail44, indent=4) )

        if readMail44Data.status_code == 200 :
            os.environ['tc_send_message_id_behaviour_stats_open_link_4'] = str(readMail44['HTMLOpenLinks'])
            os.environ['tc_send_message_id_behaviour_stats_click_link_4'] = str(readMail44['HTMLTextLinks'])
            os.environ['tc_send_message_id_behaviour_stats_unsub_link_4'] = str(readMail44['HTMLUnsubLinks'])

            readMailCount4 = 1
        else:
            print('Read Mail 4 : Mail Not Received')

    if readMailCount4 == 1:

        openlink(str(os.environ['tc_send_message_id_behaviour_stats_open_link_4']))
        clicklink(str(os.environ['tc_send_message_id_behaviour_stats_click_link_4']))
        unsubscribelinkResponse = unsubscribelink(str(os.environ['tc_send_message_id_behaviour_stats_unsub_link_4']))

        unsubscribebutton = unsubscribelinkResponse.split("~!@#~")
        os.environ['tc_send_email_unsubscribebutton_link_4'] = "http://"+os.environ['tracking_url']+unsubscribelinkResponse.split("'")[1]
        
        if unsubscribebutton[1] == 'To confirm you want to unsubscribe, please click the button below':
            print('Unsubscribe 4 : To confirm you want to unsubscribe, please click the button below')
        else:
            print('Unsubscribe 4 : Failed')

        unsubscribeBtnFunction = unsubscribebuttonFunction(str(os.environ['tc_send_email_unsubscribebutton_link_4']))
        unsubscribebuttonText = unsubscribeBtnFunction.split("~!@#~")

        if unsubscribebuttonText[1] == 'You have been successfully unsubscribed':
            print('Unsubscribe 4 : You have been successfully unsubscribed')

        del os.environ['tc_send_message_id_behaviour_stats_open_link_4']
        del os.environ['tc_send_message_id_behaviour_stats_click_link_4']
        del os.environ['tc_send_message_id_behaviour_stats_unsub_link_4']
        del os.environ['tc_send_email_unsubscribebutton_link_4']

    delay(29)
    delay(29)
    delay(29)

    transactionalReportData = transactional_report()
    transactionalReport = transactionalReportData.json()
    print("Transactional Report : ", json.dumps(transactionalReport, indent=4) )

    if transactionalReportData.status_code == 200 :

        TCI = os.environ['all_esps_transactional_send_message_id_behaviour_stats_campaign_id']

        if int(transactionalReport['payload'][0]['unique_opens']) > 0:
            print("Test Transactional Send Message Id Uninque Open stats Transactiona Campaign Id : "+TCI+" :Passed")
        else:
            print("Test Transactional Send Message Id Uninque Open stats Transactiona Campaign Id : "+TCI+" :Failed")

        if int(transactionalReport['payload'][0]['sent']) > 0:
            print("Test Transactional Send Message Id Sent stats Transactiona Campaign Id : "+TCI+" :Passed")
        else:
            print("Test Transactional Send Message Id Sent stats Transactiona Campaign Id : "+TCI+" :Failed")

        if int(transactionalReport['payload'][0]['clicks']) > 0:
            print("Test Transactional Send Message Id Clicks stats Transactiona Campaign Id : "+TCI+" :Passed")
        else:
            print("Test Transactional Send Message Id Clicks stats Transactiona Campaign Id : "+TCI+" :Failed")

        if int(transactionalReport['payload'][0]['unsubscribes']) > 0:
            print("Test Transactional Send Message Id unsubscribes stats Transactiona Campaign Id : "+TCI+" :Passed")
        else:
            print("Test Transactional Send Message Id unsubscribes stats Transactiona Campaign Id : "+TCI+" :Failed")

        if int(transactionalReport['payload'][0]['success']) > 0:
            print("Test Transactional Send Message Id success stats Transactiona Campaign Id : "+TCI+" :Passed")
        else:
            print("Test Transactional Send Message Id success stats Transactiona Campaign Id : "+TCI+" :Failed")

        if int(transactionalReport['payload'][0]['unique_opens']) > 0:
            print("Test Transactional Send Message Id unique opens stats Transactiona Campaign Id : "+TCI+" :Passed")
        else:
            print("Test Transactional Send Message Id unique opens stats Transactiona Campaign Id : "+TCI+" :Failed")

        if int(transactionalReport['payload'][0]['unique_clicks']) > 0:
            print("Test Transactional Send Message Id unique clicks stats Transactiona Campaign Id : "+TCI+" :Passed")
        else:
            print("Test Transactional Send Message Id unique clicks stats Transactiona Campaign Id : "+TCI+" :Failed")
    else:
        print("Failed to test Transactional Send Message Id stats Transactiona Campaign Id ")

    generateContactActivityReportData = generate_contact_activity_report()
    generateContactActivityReport = generateContactActivityReportData.json()
    print("Generate Contact Activity Report : ", json.dumps(generateContactActivityReport, indent=4) )

    if generateContactActivityReportData.status_code != 200:
        print('Generate Report Failed')

    delay(29)
    delay(29)

    contactActivityReportResultData = contact_activity_report_result( str(generateContactActivityReport['payload']['id']) )
    contactActivityReportResult = contactActivityReportResultData.json()
    print("Contact Activity Report Result : ", json.dumps(contactActivityReportResult, indent=4) )

    if contactActivityReportResultData.status_code != 200:
        print('Contact Activity result Failed')
    else:
        TCI = os.environ['all_esps_transactional_send_message_id_behaviour_stats_campaign_id']
        
        if int(contactActivityReportResult['payload'][0]['opens']) > 0:
            print("`Test Transactional Send Message Id Behavioural Open stats Transactiona Campaign Id : "+TCI+" :Passed")
        else:
            print("`Test Transactional Send Message Id Behavioural Open stats Transactiona Campaign Id : "+TCI+" :Failed")
        
        if int(contactActivityReportResult['payload'][0]['sent']) > 0:
            print("`Test Transactional Send Message Id Behavioural sent stats Transactiona Campaign Id : "+TCI+" :Passed")
        else:
            print("`Test Transactional Send Message Id Behavioural sent stats Transactiona Campaign Id : "+TCI+" :Failed")
        
        if int(contactActivityReportResult['payload'][0]['clicks']) > 0:
            print("`Test Transactional Send Message Id Behavioural clicks stats Transactiona Campaign Id : "+TCI+" :Passed")
        else:
            print("`Test Transactional Send Message Id Behavioural clicks stats Transactiona Campaign Id : "+TCI+" :Failed")
        
        if str(os.environ['env']) == "All-Esps-Dev-28299":
            if str(contactActivityReportResult['payload'][0]['ocx_status']) == 'Unsubscribed':
                print("`Test Transactional Send Message Id Behavioural Unsubscribed stats Transactiona Campaign Id : "+TCI+" :Passed")
            else:
                print("`Test Transactional Send Message Id Behavioural Unsubscribed stats Transactiona Campaign Id : "+TCI+" :Failed")
        else:
            if str(contactActivityReportResult['payload'][3]['ocx_status']) == 'Unsubscribed':
                print("`Test Transactional Send Message Id Behavioural Unsubscribed stats Transactiona Campaign Id : "+TCI+" :Passed")
            else:
                print("`Test Transactional Send Message Id Behavioural Unsubscribed stats Transactiona Campaign Id : "+TCI+" :Failed")
    
    del os.environ['all_esps_transactional_send_message_id_behaviour_stats_campaign_id']

removeContactData = remove_contact()
removeContact = removeContactData.json()
print("Remove Contact Result : ", json.dumps(removeContact, indent=4) )
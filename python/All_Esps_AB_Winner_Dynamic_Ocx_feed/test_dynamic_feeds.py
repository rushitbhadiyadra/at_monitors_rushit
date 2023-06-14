from env.config import *
from fixtures.get_last_mail_by_subject import *


def test_dynamic_feeds(param):

    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    current_GMT = str(dt_string)

    ##Test_Dynamic_Ocx_Feed
    subjectLastMail = "Test AB-Winner Send Message Id Dynamic Ocx Feed-"+os.environ['connectionId']+"-"+os.environ['env']
    timeoutLastMail = 60000

    getLastMailBySubjectData = get_last_mail_by_subject(subjectLastMail, timeoutLastMail)
    getLastMailBySubject = getLastMailBySubjectData.json()
    print("Test Dynamic Ocx Feed 1 : ", json.dumps(getLastMailBySubject, indent=4) )

    testdynamicocxfeedcount = 0

    if getLastMailBySubjectData.status_code == 200:
        testdynamicocxfeedcount = testdynamicocxfeedcount + 1
    else:
        getLastMailBySubjectData = get_last_mail_by_subject(subjectLastMail, timeoutLastMail)
        getLastMailBySubject = getLastMailBySubjectData.json()
        print("Test Dynamic Ocx Feed 2 : ", json.dumps(getLastMailBySubject, indent=4) )

        testdynamicocxfeedcount = 0

        if getLastMailBySubjectData.status_code == 200:
            testdynamicocxfeedcount = testdynamicocxfeedcount + 1

    if testdynamicocxfeedcount == 1:

        htmlText = getLastMailBySubject['html']
        fieldValue = htmlText.split("~!@#~")
        ocxFeedDynamic = xmltodict.parse(fieldValue[1])

        if param == 2:
            os.environ['all_esp_ab_winner_dynamic_ocx_feed'+os.environ['connectionId']] = getLastMailBySubject['HTMLOpenLinks'][0]
            
        if ocxFeedDynamic['table']['tbody']['tr'][0]['td'][0] == "Hotel Name":
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : Hotel Name : Passed')
        else:
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : Hotel Name : Failed')
        
        if ocxFeedDynamic['table']['tbody']['tr'][0]['td'][1] == "Location":
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : Location : Passed')
        else:
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : Location : Failed')
            
        if ocxFeedDynamic['table']['tbody']['tr'][0]['td'][1] == "Rooms":
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : Rooms : Passed')
        else:
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : Rooms : Failed')
        
        if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][0] == "Hilton":
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : Hilton : Passed')
        else:
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : Hilton : Failed')
        
        if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][1] == "NYC":
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : NYC : Passed')
        else:
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : NYC : Failed')
            
        if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2]['table']['tbody']['tr'][0]['td'][0] == "Room Type":
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : Room Type : Passed')
        else:
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : Room Type : Failed')
        
        if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2]['table']['tbody']['tr'][0]['td'][1] == "Count":
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : Count : Passed')
        else:
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : Count : Failed')
        
        if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2]['table']['tbody']['tr'][1]['td'][0] == "Regular":
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : Regular : Passed')
        else:
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : Regular : Failed')
            
        if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2]['table']['tbody']['tr'][1]['td'][1] == "111":
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : 111 : Passed')
        else:
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : 111 : Failed')
            
        if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2]['table']['tbody']['tr'][2]['td'][0] == "suit":
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : suit : Passed')
        else:
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : suit : Failed')
            
        if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2]['table']['tbody']['tr'][2]['td'][1] == "222":
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : 222 : Passed')
        else:
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : 222 : Failed')
        
        if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2]['table']['tbody']['tr'][3]['td'][0] == "Gorgeous":
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : Gorgeous : Passed')
        else:
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : Gorgeous : Failed')
        
        if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2]['table']['tbody']['tr'][3]['td'][1] == "555":
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : 555 : Passed')
        else:
            print('Test ab-winner in ocx_feed_dynamic with nested loop is working Time : '+current_GMT+' : 555 : Failed')

        ##Test_Dynamic_Ocx_Feed_Html
        ocx_feed_html_subject = "Test AB-Winner Send Message Id Dynamic Ocx Feed Html-"+os.environ['connectionId']+"-"+os.environ['env']
        ocx_feed_html_timeout = 60000

        ocx_feed_html_last_mail_subject_data = get_last_mail_by_subject(ocx_feed_html_subject, ocx_feed_html_timeout)
        ocx_feed_html_last_mail_subject = ocx_feed_html_last_mail_subject_data.json()
        print("Test Dynamic Ocx Feed Html 1 : ", json.dumps(ocx_feed_html_last_mail_subject, indent=4) )

        ocx_feed_html_last_mail_subject_count = 0

        if ocx_feed_html_last_mail_subject_data.status_code == 200:
            ocx_feed_html_last_mail_subject_count = 1
        else:
            ocx_feed_html_last_mail_subject_data = get_last_mail_by_subject(ocx_feed_html_subject, ocx_feed_html_timeout)
            ocx_feed_html_last_mail_subject = ocx_feed_html_last_mail_subject_data.json()
            print("Test Dynamic Ocx Feed Html 2 : ", json.dumps(ocx_feed_html_last_mail_subject, indent=4) )

            ocx_feed_html_last_mail_subject_count = 0

            if ocx_feed_html_last_mail_subject_data.status_code == 200:
                ocx_feed_html_last_mail_subject_count =  1

        if ocx_feed_html_last_mail_subject_count == 1:

            ocx_feed_html_last_mail_subject_htmlText = ocx_feed_html_last_mail_subject['html']
            ocx_feed_html_last_mail_subject_fieldValue = ocx_feed_html_last_mail_subject_htmlText.split("~!@#~")
            ocx_feed_html_last_mail_subject_ocxFeedDynamic = xmltodict.parse(ocx_feed_html_last_mail_subject_fieldValue[1])

            if param == 2:
                os.environ['all_esp_ab_winner_dynamic_ocx_feed_html'+os.environ['connectionId']] = ocx_feed_html_last_mail_subject['HTMLOpenLinks'][0]
            
            if ocx_feed_html_last_mail_subject['to']['value'][0]['address'] == "ae_abw_dy_of_htm1@hoohem.com" :
                ab_winner_all_esp_list_field_first_name = os.environ['ab_winner_all_esp_list_field_first_name1']
                ab_winner_all_esp_list_field_address = os.environ['ab_winner_all_esp_list_field_address1']
            
            if ocx_feed_html_last_mail_subject['to']['value'][0]['address'] == "ae_abw_dy_of_htm2@hoohem.com" :
                ab_winner_all_esp_list_field_first_name = os.environ['ab_winner_all_esp_list_field_first_name2']
                ab_winner_all_esp_list_field_address = os.environ['ab_winner_all_esp_list_field_address2']
            
            if ocx_feed_html_last_mail_subject['to']['value'][0]['address'] == "ae_abw_dy_of_htm3@hoohem.com":
                ab_winner_all_esp_list_field_first_name = os.environ['ab_winner_all_esp_list_field_first_name3']
                ab_winner_all_esp_list_field_address = os.environ['ab_winner_all_esp_list_field_address3']
            
            if ocx_feed_html_last_mail_subject_ocxFeedDynamic['div']['table']['tr'][0]['td'][0] == "Hotel Name":
                print('Test Ab Winner in ocx_feed_dynamic_html is working Time : '+current_GMT+' : Hotel Name : Passed')
            else:
                print('Test Ab Winner in ocx_feed_dynamic_html is working Time : '+current_GMT+' : Hotel Name : Failed')
            
            if ocx_feed_html_last_mail_subject_ocxFeedDynamic['div']['table']['tr'][0]['td'][1] == "Hotel location":
                print('Test Ab Winner in ocx_feed_dynamic_html is working Time : '+current_GMT+' : Hotel location : Passed')
            else:
                print('Test Ab Winner in ocx_feed_dynamic_html is working Time : '+current_GMT+' : Hotel location : Failed')
                
            if ocx_feed_html_last_mail_subject_ocxFeedDynamic['div']['table']['tr'][0]['td'][2] == "First Name":
                print('Test Ab Winner in ocx_feed_dynamic_html is working Time : '+current_GMT+' : First Name : Passed')
            else:
                print('Test Ab Winner in ocx_feed_dynamic_html is working Time : '+current_GMT+' : First Name : Failed')
            
            if ocx_feed_html_last_mail_subject_ocxFeedDynamic['div']['table']['tr'][0]['td'][3] == "address":
                print('Test Ab Winner in ocx_feed_dynamic_html is working Time : '+current_GMT+' : address : Passed')
            else:
                print('Test Ab Winner in ocx_feed_dynamic_html is working Time : '+current_GMT+' : address : Failed')
            
            if ocx_feed_html_last_mail_subject_ocxFeedDynamic['div']['table']['tr'][1]['td'][0] == "BVN":
                print('Test Ab Winner in ocx_feed_dynamic_html is working Time : '+current_GMT+' : BVN : Passed')
            else:
                print('Test Ab Winner in ocx_feed_dynamic_html is working Time : '+current_GMT+' : BVN : Failed')
                
            if ocx_feed_html_last_mail_subject_ocxFeedDynamic['div']['table']['tr'][1]['td'][1] == "10":
                print('Test Ab Winner in ocx_feed_dynamic_html is working Time : '+current_GMT+' : 10 : Passed')
            else:
                print('Test Ab Winner in ocx_feed_dynamic_html is working Time : '+current_GMT+' : 10 : Failed')
            
            if ocx_feed_html_last_mail_subject_ocxFeedDynamic['div']['table']['tr'][1]['td'][2] == str(ab_winner_all_esp_list_field_first_name):
                print('Test Ab Winner in ocx_feed_dynamic_html is working Time : '+current_GMT+' : '+ab_winner_all_esp_list_field_first_name+' : Passed')
            else:
                print('Test Ab Winner in ocx_feed_dynamic_html is working Time : '+current_GMT+' : '+ab_winner_all_esp_list_field_first_name+' : Failed')
            
            if ocx_feed_html_last_mail_subject_ocxFeedDynamic['div']['table']['tr'][1]['td'][3] == str(ab_winner_all_esp_list_field_address):
                print('Test Ab Winner in ocx_feed_dynamic_html is working Time : '+current_GMT+' : '+ab_winner_all_esp_list_field_address+' : Passed')
            else:
                print('Test Ab Winner in ocx_feed_dynamic_html is working Time : '+current_GMT+' : '+ab_winner_all_esp_list_field_address+' : Failed')
            
            ##Test_Ocx_Feed_Html
            test_ocx_feed_html_subject = "Test AB-Winnner Send Message Id Ocx Feed Html-"+os.environ['connectionId']+"-"+os.environ['env']
            test_ocx_feed_html_timeout = 60000

            test_ocx_feed_html_timeout_last_mail_subject_data = get_last_mail_by_subject(test_ocx_feed_html_subject, test_ocx_feed_html_timeout)
            test_ocx_feed_html_timeout_last_mail_subject = test_ocx_feed_html_timeout_last_mail_subject_data.json()
            print("Test Ocx Feed Html 1 : ", json.dumps(test_ocx_feed_html_timeout_last_mail_subject, indent=4) )

            test_ocx_feed_html_count = 0

            if test_ocx_feed_html_timeout_last_mail_subject_data.status_code == 200:
                test_ocx_feed_html_count = 1
            else:
                test_ocx_feed_html_timeout_last_mail_subject_data = get_last_mail_by_subject(test_ocx_feed_html_subject, test_ocx_feed_html_timeout)
                test_ocx_feed_html_timeout_last_mail_subject = test_ocx_feed_html_timeout_last_mail_subject_data.json()
                print("Test Ocx Feed Html 2 : ", json.dumps(test_ocx_feed_html_timeout_last_mail_subject, indent=4) )

                test_ocx_feed_html_count = 0

                if test_ocx_feed_html_timeout_last_mail_subject_data.status_code == 200:
                    test_ocx_feed_html_count = 1

            if test_ocx_feed_html_count == 1:

                if param == 2:
                    os.environ['all_esp_ab_winner_ocx_feed_html'+os.environ['connectionId']] = test_ocx_feed_html_timeout_last_mail_subject['HTMLOpenLinks'][0]

                test_ocx_feed_html_htmlText = test_ocx_feed_html_timeout_last_mail_subject['html']
                test_ocx_feed_html_fieldValue = test_ocx_feed_html_htmlText.split("~!@#~")
                test_ocx_feed_html_ocxFeedDynamic = xmltodict.parse(test_ocx_feed_html_fieldValue[1])

                if test_ocx_feed_html_ocxFeedDynamic['div']['table']['tr'][0]['td'][0] == "Hotel Name":
                    print('Test Ab Winner in ocx_feed_html is working Time : '+current_GMT+' : Hotel Name : Passed')
                else:
                    print('Test Ab Winner in ocx_feed_html is working Time : '+current_GMT+' : Hotel Name : Failed')
                
                if test_ocx_feed_html_ocxFeedDynamic['div']['table']['tr'][0]['td'][1] == "Hotel location":
                    print('Test Ab Winner in ocx_feed_html is working Time : '+current_GMT+' : Hotel location : Passed')
                else:
                    print('Test Ab Winner in ocx_feed_html is working Time : '+current_GMT+' : Hotel location : Failed')
                    
                if test_ocx_feed_html_ocxFeedDynamic['div']['table']['tr'][0]['td'][2] == "First Name":
                    print('Test Ab Winner in ocx_feed_html is working Time : '+current_GMT+' : First Name : Passed')
                else:
                    print('Test Ab Winner in ocx_feed_html is working Time : '+current_GMT+' : First Name : Failed')
                
                if test_ocx_feed_html_ocxFeedDynamic['div']['table']['tr'][0]['td'][3] == "address":
                    print('Test Ab Winner in ocx_feed_html is working Time : '+current_GMT+' : address : Passed')
                else:
                    print('Test Ab Winner in ocx_feed_html is working Time : '+current_GMT+' : address : Failed')
                
                if test_ocx_feed_html_ocxFeedDynamic['div']['table']['tr'][1]['td'][0] == "BVN":
                    print('Test Ab Winner in ocx_feed_html is working Time : '+current_GMT+' : BVN : Passed')
                else:
                    print('Test Ab Winner in ocx_feed_html is working Time : '+current_GMT+' : BVN : Failed')
                    
                if test_ocx_feed_html_ocxFeedDynamic['div']['table']['tr'][1]['td'][1] == "Ahmedabad":
                    print('Test Ab Winner in ocx_feed_html is working Time : '+current_GMT+' : Ahmedabad : Passed')
                else:
                    print('Test Ab Winner in ocx_feed_html is working Time : '+current_GMT+' : Ahmedabad : Failed')
                
                if test_ocx_feed_html_ocxFeedDynamic['div']['table']['tr'][1]['td'][2] == 'Ongage':
                    print('Test Ab Winner in ocx_feed_html is working Time : '+current_GMT+' : Ongage : Passed')
                else:
                    print('Test Ab Winner in ocx_feed_html is working Time : '+current_GMT+' : Ongage : Failed')
                
                if test_ocx_feed_html_ocxFeedDynamic['div']['table']['tr'][1]['td'][3] == 'Ahmedabad':
                    print('Test Ab Winner in ocx_feed_html is working Time : '+current_GMT+' : Ahmedabad : Passed')
                else:
                    print('Test Ab Winner in ocx_feed_html is working Time : '+current_GMT+' : Ahmedabad : Failed')

                ##Test_Ocx_Feed1
                test_ocx_feed_subject_last_mail = "Test AB-Winner Send Message Id Ocx Feed-"+os.environ['connectionId']+"-"+os.environ['env']
                test_ocx_feed_subject_last_mail_timeout = 60000

                test_ocx_feed_subject_data = get_last_mail_by_subject(test_ocx_feed_subject_last_mail, test_ocx_feed_subject_last_mail_timeout)
                test_ocx_feed_subject = test_ocx_feed_subject_data.json()
                print("Test Ocx Feed  1 : ", json.dumps(test_ocx_feed_subject, indent=4) )

                test_ocx_feed_count = 0

                if test_ocx_feed_subject_data.status_code == 200:
                    test_ocx_feed_count = 1
                else:
                    test_ocx_feed_subject_data = get_last_mail_by_subject(test_ocx_feed_subject_last_mail, test_ocx_feed_subject_last_mail_timeout)
                    test_ocx_feed_subject = test_ocx_feed_subject_data.json()
                    print("Test Ocx Feed 2 : ", json.dumps(test_ocx_feed_subject, indent=4) )

                    test_ocx_feed_count = 0

                    if test_ocx_feed_subject_data.status_code == 200:
                        test_ocx_feed_count = 1

                if test_ocx_feed_count == 1:

                    if param == 2:
                        os.environ['all_esp_ab_winner_ocx_feed'+os.environ['connectionId']] = test_ocx_feed_subject['HTMLOpenLinks'][0]

                    test_ocx_feed_htmlText = test_ocx_feed_subject['html']
                    test_ocx_feed_fieldValue = test_ocx_feed_htmlText.split("~!@#~")
                    test_ocx_feed_ocxFeedDynamic = xmltodict.parse(test_ocx_feed_fieldValue[1])

                    if test_ocx_feed_ocxFeedDynamic['table']['tbody']['tr'][0]['td'][0] == "Hotel Name":
                        print('Test Ab Winner in ocx_feed is working Time : '+current_GMT+' : Hotel Name : Passed')
                    else:
                        print('Test Ab Winner in ocx_feed is working Time : '+current_GMT+' : Hotel Name : Failed')
                    
                    if test_ocx_feed_ocxFeedDynamic['table']['tbody']['tr'][0]['td'][1] == "Location":
                        print('Test Ab Winner in ocx_feed is working Time : '+current_GMT+' : Location : Passed')
                    else:
                        print('Test Ab Winner in ocx_feed is working Time : '+current_GMT+' : Location : Failed')
                        
                    if test_ocx_feed_ocxFeedDynamic['table']['tbody']['tr'][0]['td'][2] == "Link":
                        print('Test Ab Winner in ocx_feed is working Time : '+current_GMT+' : Link : Passed')
                    else:
                        print('Test Ab Winner in ocx_feed is working Time : '+current_GMT+' : Link : Failed')
                    
                    if test_ocx_feed_ocxFeedDynamic['table']['tbody']['tr'][1]['td'][0] == "Regular":
                        print('Test Ab Winner in ocx_feed is working Time : '+current_GMT+' : Regular : Passed')
                    else:
                        print('Test Ab Winner in ocx_feed is working Time : '+current_GMT+' : Regular : Failed')
                    
                    if test_ocx_feed_ocxFeedDynamic['table']['tbody']['tr'][1]['td'][1] == "India":
                        print('Test Ab Winner in ocx_feed is working Time : '+current_GMT+' : India : Passed')
                    else:
                        print('Test Ab Winner in ocx_feed is working Time : '+current_GMT+' : India : Failed')
                        
                    if test_ocx_feed_ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2] == "www.test.com":
                        print('Test Ab Winner in ocx_feed is working Time : '+current_GMT+' : www.test.com : Passed')
                    else:
                        print('Test Ab Winner in ocx_feed is working Time : '+current_GMT+' : www.test.com : Failed')
                    
                    if test_ocx_feed_ocxFeedDynamic['table']['tbody']['tr'][2]['td'][0] == 'Suit':
                        print('Test Ab Winner in ocx_feed is working Time : '+current_GMT+' : Suit : Passed')
                    else:
                        print('Test Ab Winner in ocx_feed is working Time : '+current_GMT+' : Suit : Failed')
                    
                    if test_ocx_feed_ocxFeedDynamic['table']['tbody']['tr'][2]['td'][1] == 'Rajasthan':
                        print('Test Ab Winner in ocx_feed is working Time : '+current_GMT+' : Rajasthan : Passed')
                    else:
                        print('Test Ab Winner in ocx_feed is working Time : '+current_GMT+' : Rajasthan : Failed')
                    
                    if test_ocx_feed_ocxFeedDynamic['table']['tbody']['tr'][2]['td'][2] == 'www.google.com':
                        print('Test Ab Winner in ocx_feed is working Time : '+current_GMT+' : www.google.com : Passed')
                    else:
                        print('Test Ab Winner in ocx_feed is working Time : '+current_GMT+' : www.google.com : Failed')

                    ##Test_ocx_feed_rss
                    test_ocx_feed_rss_subject_last_mail = "Test AB-Winner Send Message Id Ocx Feed Rss-"+os.environ['connectionId']+"-"+os.environ['env']
                    test_ocx_feed_rss_subject_last_mail_timeout = 60000

                    test_ocx_feed_rss_subject_data = get_last_mail_by_subject(test_ocx_feed_rss_subject_last_mail, test_ocx_feed_rss_subject_last_mail_timeout)
                    test_ocx_feed_rss_subject = test_ocx_feed_rss_subject_data.json()
                    print("Test ocx feed rss 1 : ", json.dumps(test_ocx_feed_rss_subject, indent=4) )

                    test_ocx_feed_rss_subject_count = 0

                    if test_ocx_feed_rss_subject_data.status_code == 200:
                        test_ocx_feed_rss_subject_count = 1
                    else:
                        test_ocx_feed_rss_subject_data = get_last_mail_by_subject(test_ocx_feed_rss_subject_last_mail, test_ocx_feed_rss_subject_last_mail_timeout)
                        test_ocx_feed_rss_subject = test_ocx_feed_rss_subject_data.json()
                        print("Test ocx feed rss 2 : ", json.dumps(test_ocx_feed_rss_subject, indent=4) )

                        test_ocx_feed_rss_subject_count = 0

                        if test_ocx_feed_rss_subject_data.status_code == 200:
                            test_ocx_feed_rss_subject_count = 1

                    if test_ocx_feed_rss_subject_count == 1:

                        if param == 2:
                            os.environ['all_esp_ab_winner_ocx_feed_rss'+os.environ['connectionId']] = test_ocx_feed_rss_subject['HTMLOpenLinks'][0]

                        test_ocx_feed_rss_htmlText = test_ocx_feed_rss_subject['html']
                        test_ocx_feed_rss_fieldValue = test_ocx_feed_rss_htmlText.split("~!@#~")
                        ocxRSSTitle = test_ocx_feed_rss_fieldValue[1]
                        ocxRSSLink = test_ocx_feed_rss_fieldValue[2]
                        ocxRSSDesc = test_ocx_feed_rss_fieldValue[3]

                        if str(ocxRSSTitle) == str(os.environ['ocx_rss_title']):
                            print('Test Ab winner in ocx_rss with title Is equals to Time : '+current_GMT+' : Passed')
                        else:
                            print('Test Ab winner in ocx_rss with title Is equals to Time : '+current_GMT+' : Failed')

                        if str(ocxRSSLink) == str(os.environ['ocx_rss_link']):
                            print('Test Ab winner in ocx_rss with link Is equals to Time : '+current_GMT+' : Passed')
                        else:
                            print('Test Ab winner in ocx_rss with link Is equals to Time : '+current_GMT+' : Failed')
                        
                        if str(ocxRSSDesc) == str(os.environ['ocx_rss_desc']):
                            print('Test Ab winner in ocx_rss with description Is equals to Time : '+current_GMT+' : Passed')
                        else:
                            print('Test Ab winner in ocx_rss with description Is equals to Time : '+current_GMT+' : Failed')
                        
                        for data in test_ocx_feed_rss_subject['headerLines']:
                            if data['key'].lower() == 'customheader' :
                                header = data['line'].split(":")
                                if header[0].lower() == 'customheader':
                                    print('Test customheader Is Working Time :'+current_GMT+' : Passed')
                                else:
                                    print('Test customheader Is Working Time :'+current_GMT+' : Failed')

                                if header[1].lower().strip() == 'test':
                                    print('Test test Is Working Time :'+current_GMT+' : Passed')
                                else:
                                    print('Test test Is Working Time :'+current_GMT+' : Failed')
                    else:
                        print('Test ocx feed rss : Mail Not Receive')
                else:
                    print('Test Ocx Feed : Mail Not Receive')
            else:
                print('Test Ocx Feed Html : Mail Not Receive')
        else:
            print('Test Dynamic Ocx Feed Html : Mail Not Receive')
    else:
        print('Test Dynamic Ocx Feed : Mail Not Receive')
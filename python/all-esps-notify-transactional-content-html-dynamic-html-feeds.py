from fixtures.delay import *
from All_Esps_Notify_Transactional_Content_HTML_Dynamic_HTML_Feeds.delete_mail_by_id_and_subject import *
from All_Esps_Notify_Transactional_Content_HTML_Dynamic_HTML_Feeds.Change_contact_status import *
from All_Esps_Notify_Transactional_Content_HTML_Dynamic_HTML_Feeds.Change_contact_status_2 import *
from All_Esps_Notify_Transactional_Content_HTML_Dynamic_HTML_Feeds.Dynamic_Ocx_Feed import *
from All_Esps_Notify_Transactional_Content_HTML_Dynamic_HTML_Feeds.Dynamic_Ocx_Feed_Html import *
from All_Esps_Notify_Transactional_Content_HTML_Dynamic_HTML_Feeds.Ocx_Feed_Html import *
from All_Esps_Notify_Transactional_Content_HTML_Dynamic_HTML_Feeds.OcxFeed import *
from All_Esps_Notify_Transactional_Content_HTML_Dynamic_HTML_Feeds.OcxFeed_Rss import *
from All_Esps_Notify_Transactional_Content_HTML_Dynamic_HTML_Feeds.Distinct_Case import *
from All_Esps_Notify_Transactional_Content_HTML_Dynamic_HTML_Feeds.Test_Dynamic_Ocx_Feed import *
from All_Esps_Notify_Transactional_Content_HTML_Dynamic_HTML_Feeds.Test_Dynamic_Ocx_Feed1 import *
from All_Esps_Notify_Transactional_Content_HTML_Dynamic_HTML_Feeds.Get_Contact_Info import *
from All_Esps_Notify_Transactional_Content_HTML_Dynamic_HTML_Feeds.Test_Dynamic_Ocx_Feed_Html import *
from All_Esps_Notify_Transactional_Content_HTML_Dynamic_HTML_Feeds.Test_Dynamic_Ocx_Feed_Html1 import *
from All_Esps_Notify_Transactional_Content_HTML_Dynamic_HTML_Feeds.Test_Ocx_Feed_Html import *
from All_Esps_Notify_Transactional_Content_HTML_Dynamic_HTML_Feeds.Test_Ocx_Feed_Html1 import *
from All_Esps_Notify_Transactional_Content_HTML_Dynamic_HTML_Feeds.Test_Ocx_Feed import *
from All_Esps_Notify_Transactional_Content_HTML_Dynamic_HTML_Feeds.Test_Ocx_Feed1 import *
from All_Esps_Notify_Transactional_Content_HTML_Dynamic_HTML_Feeds.Test_Ocx_Feed_Rss import *
from All_Esps_Notify_Transactional_Content_HTML_Dynamic_HTML_Feeds.Test_Ocx-Feed_Rss1 import *
from All_Esps_Notify_Transactional_Content_HTML_Dynamic_HTML_Feeds.Test_Distinct_Case import *
from All_Esps_Notify_Transactional_Content_HTML_Dynamic_HTML_Feeds.Test_Distinct_Case_1 import *

deleteMailByIdAndSubject = delete_mail_by_id_and_subject()
print(deleteMailByIdAndSubject)

changeContactStatusData = Change_contact_status()
changeContactStatus = changeContactStatusData.json()
print("Change Contact Status : ",  json.dumps(changeContactStatus, indent=4))

changeContactStatus2Data = Change_contact_status_2()
changeContactStatus2 = changeContactStatus2Data.json()
print("Change Contact Status 2 : ",  json.dumps(changeContactStatus2, indent=4))

dynamicOcxFeedData = Dynamic_Ocx_Feed()
dynamicOcxFeed = dynamicOcxFeedData.json()
print("Dynamic Ocx Feed : ",  json.dumps(dynamicOcxFeed, indent=4))

if dynamicOcxFeedData.status_code == 200:
    if dynamicOcxFeed['payload']['not_active'][0] == "ae_nt_sd_htm_dy_of1@hoohem.com":
        print('Test Notify Transactional Check Status Using HTML : ae_nt_sd_htm_dy_of1@hoohem.com: pass')
    else:
        print('Test Notify Transactional Check Status Using HTML : ae_nt_sd_htm_dy_of1@hoohem.com: failed')

dynamicOcxFeedHtmlData = Dynamic_Ocx_Feed_Html()
dynamicOcxFeedHtml = dynamicOcxFeedHtmlData.json()
print("Dynamic Ocx Feed Html : ",  json.dumps(dynamicOcxFeedHtml, indent=4))

ocxFeedHtmlData = Ocx_Feed_Html()
ocxFeedHtml = ocxFeedHtmlData.json()
print("Ocx Feed Html : ",  json.dumps(ocxFeedHtml, indent=4))

ocxFeedData = OcxFeed()
ocxFeed = ocxFeedData.json()
print("Ocx Feed : ",  json.dumps(ocxFeed, indent=4))

ocxFeedRssData = OcxFeed_Rss()
ocxFeedRss = ocxFeedRssData.json()
print("Ocx Feed Rss : ",  json.dumps(ocxFeedRss, indent=4))

os.environ['nt_html_id_maling_id'] = str(ocxFeedRss['payload']['mailing_id'])

distinctCaseData = Distinct_Case()
distinctCase = distinctCaseData.json()
print("Distinct Case : ",  json.dumps(distinctCase, indent=4))

delay(29)
delay(29)
delay(29)
delay(29)
delay(29)
delay(29)
delay(29)
delay(29)

testDynamicOcxFeedData = Test_Dynamic_Ocx_Feed()
testDynamicOcxFeed = testDynamicOcxFeedData.json()
print("Test Dynamic Ocx Feed : ",  json.dumps(testDynamicOcxFeed, indent=4))
fieldValue = testDynamicOcxFeed.split("~!@#~")
ocxFeedDynamic = xml2Json(fieldValue[1])

if testDynamicOcxFeedData.status_code == 200:
    if ocxFeedDynamic['table']['tbody']['tr'][0]['td'][0] == "Hotel Name":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Hotel Name: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Hotel Name: failed')
    if ocxFeedDynamic['table']['tbody']['tr'][0]['td'][1] == "Location":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Location: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Location: failed')
    if ocxFeedDynamic['table']['tbody']['tr'][0]['td'][2] == "Rooms":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Rooms: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Rooms: failed')
    if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][0] == "Hilton":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Hilton: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Hilton: failed')
    if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][1] == "NYC":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : NYC: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : NYC: failed')
    if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2]['table']['tbody']['tr'][0]['td'][0] == "Room Type":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Room Type: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Room Type: failed')
    if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2]['table']['tbody']['tr'][0]['td'][1] == "Count":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Count: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Count: failed')
    if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2]['table']['tbody']['tr'][1]['td'][0] == "Regular":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Regular: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Regular: failed')
    if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2]['table']['tbody']['tr'][1]['td'][1] == "111":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : 111: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : 111: failed')
    if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2]['table']['tbody']['tr'][2]['td'][0] == "suit":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : suit: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : suit: failed')
    if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2]['table']['tbody']['tr'][2]['td'][1] == "222":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : 222: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : 222: failed')
    if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2]['table']['tbody']['tr'][3]['td'][0] == "Gorgeous":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Gorgeous: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Gorgeous: failed')
    if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2]['table']['tbody']['tr'][3]['td'][1] == "555":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : 555: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : 555: failed')

else:
    testDynamicOcxFeed1Data = Test_Dynamic_Ocx_Feed1()
    testDynamicOcxFeed1 = testDynamicOcxFeed1Data.json()
    print("Test Dynamic Ocx Feed1 : ",  json.dumps(testDynamicOcxFeed1, indent=4))
    fieldValue = testDynamicOcxFeed1.split("~!@#~")
    ocxFeedDynamic = xml2Json(fieldValue[1])

    if testDynamicOcxFeed1Data.status_code == 200:
        if ocxFeedDynamic['table']['tbody']['tr'][0]['td'][0] == "Hotel Name":
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Hotel Name: pass')
        else:
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Hotel Name: failed')
        if ocxFeedDynamic['table']['tbody']['tr'][0]['td'][1] == "Location":
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Location: pass')
        else:
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Location: failed')
        if ocxFeedDynamic['table']['tbody']['tr'][0]['td'][2] == "Rooms":
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Rooms: pass')
        else:
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Rooms: failed')
        if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][0] == "Hilton":
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Hilton: pass')
        else:
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Hilton: failed')
        if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][1] == "NYC":
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : NYC: pass')
        else:
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : NYC: failed')
        if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2]['table']['tbody']['tr'][0]['td'][0] == "Room Type":
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Room Type: pass')
        else:
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Room Type: failed')
        if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2]['table']['tbody']['tr'][0]['td'][1] == "Count":
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Count: pass')
        else:
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Count: failed')
        if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2]['table']['tbody']['tr'][1]['td'][0] == "Regular":
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Regular: pass')
        else:
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Regular: failed')
        if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2]['table']['tbody']['tr'][1]['td'][1] == "111":
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : 111: pass')
        else:
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : 111: failed')
        if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2]['table']['tbody']['tr'][2]['td'][0] == "suit":
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : suit: pass')
        else:
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : suit: failed')
        if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2]['table']['tbody']['tr'][2]['td'][1] == "222":
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : 222: pass')
        else:
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : 222: failed')
        if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2]['table']['tbody']['tr'][3]['td'][0] == "Gorgeous":
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Gorgeous: pass')
        else:
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : Gorgeous: failed')
        if ocxFeedDynamic['table']['tbody']['tr'][1]['td'][2]['table']['tbody']['tr'][3]['td'][1] == "555":
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : 555: pass')
        else:
            print('Test Notify Transactional content HTML in ocx_feed_dynamic with nested loop is working Time : 555: failed')

        else:
            print('Dynamic Ocx Feed Mail not received : Mail Not Received')

getContactInfoData = Get_Contact_Info()
getContactInfo = getContactInfoData.json()
print("Get Contact Info : ",  json.dumps(getContactInfo, indent=4))

os.environ['notify_transactional_content_html_list_field_first_name'] = str(getContactInfo['payload']['first_name'])
os.environ['notify_transactional_content_html_list_field_address'] = str(getContactInfo['payload']['address'])
os.environ['regular_campaign_list_field_address'] = str(getContactInfo['payload']['address'])
os.environ['rc_ocx_created_date'] = str(getContactInfo['payload']['ocx_created_date']['toString()']['substring(0,7)'])
os.environ['rc_contact_id'] = str(getContactInfo['payload']['id'])

testDynamicOcxFeedHtmlData = Test_Dynamic_Ocx_Feed_Html()
testDynamicOcxFeedHtml = testDynamicOcxFeedHtmlData.json()
print("Test Dynamic Ocx Feed Html : ",  json.dumps(testDynamicOcxFeedHtml, indent=4))
fieldValue = testDynamicOcxFeedHtml.split("~!@#~")
ocxFeedDynamicHtml = xml2Json(fieldValue[1])
mail_received_time = Math.round(Date.parse(testDynamicOcxFeedHtmlData.date)/1000)

if testDynamicOcxFeedHtmlData.status_code == 200:
    if ocxFeedDynamicHtml['div']['table']['tr'][0]['td'][0] == "Hotel Name":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : Hotel Name: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : Hotel Name: failed')
    if ocxFeedDynamicHtml['div']['table']['tr'][0]['td'][1] == "Hotel location":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : Hotel location: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : Hotel location: failed')
    if ocxFeedDynamicHtml['div']['table']['tr'][0]['td'][2] == "First Name":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : First Name: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : First Name: failed')
    if ocxFeedDynamicHtml['div']['table']['tr'][0]['td'][3] == "address":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : address: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : address: failed')
    if ocxFeedDynamicHtml['div']['table']['tr'][1]['td'][0] == "BVN":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : BVN: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : BVN: failed')
    if ocxFeedDynamicHtml['div']['table']['tr'][1]['td'][1] == "10":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : 10: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : 10: failed')
    if testDynamicOcxFeedHtml['div']['table']['tr'][1]['td'][2] == os.environ['notify_transactional_content_html_list_field_first_name']:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : notify_transactional_content_html_list_field_first_name: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : notify_transactional_content_html_list_field_first_name: failed')
    if ocxFeedDynamicHtml['div']['table']['tr'][1]['td'][3] == os.environ['notify_transactional_content_html_list_field_address']:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : notify_transactional_content_html_list_field_address: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : notify_transactional_content_html_list_field_address: failed')

    if mail_received_time - os.environ['nt_ch_dh_feed_send_schedule_date_mail_sending_time'] > "250":
            print('Test Notify Transactional Content HTML Feed Schedule Date "Is Working" Time : 250: pass')
        else:
            print('Test Notify Transactional Content HTML Feed Schedule Date "Is Working" Time : 250: failed')

else:
    testDynamicOcxFeedHtml1Data = Test_Dynamic_Ocx_Feed_Html1()
    testDynamicOcxFeedHtml1 = testDynamicOcxFeedHtml1Data.json()
    print("Test Dynamic Ocx Feed Html1 : ",  json.dumps(testDynamicOcxFeedHtml1, indent=4))
    fieldValue = testDynamicOcxFeedHtml1.split("~!@#~")
    ocxFeedDynamicHtml = xml2Json(fieldValue[1])
    mail_received_time = Math.round(Date.parse(testDynamicOcxFeedHtml1Data.date)/1000)

    if testDynamicOcxFeedHtml1Data.status_code == 200:
        if ocxFeedDynamicHtml['div']['table']['tr'][0]['td'][0] == "Hotel Name":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : Hotel Name: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : Hotel Name: failed')
    if ocxFeedDynamicHtml['div']['table']['tr'][0]['td'][1] == "Hotel location":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : Hotel location: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : Hotel location: failed')
    if ocxFeedDynamicHtml['div']['table']['tr'][0]['td'][2] == "First Name":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : First Name: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : First Name: failed')
    if ocxFeedDynamicHtml['div']['table']['tr'][0]['td'][3] == "address":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : address: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : address: failed')
    if ocxFeedDynamicHtml['div']['table']['tr'][1]['td'][0] == "BVN":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : BVN: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : BVN: failed')
    if ocxFeedDynamicHtml['div']['table']['tr'][1]['td'][1] == "10":
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : 10: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : 10: failed')
    if ocxFeedDynamicHtml['div']['table']['tr'][1]['td'][2] == os.environ['notify_transactional_content_html_list_field_first_name']:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : notify_transactional_content_html_list_field_first_name: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : notify_transactional_content_html_list_field_first_name: failed')
    if ocxFeedDynamicHtml['div']['table']['tr'][1]['td'][3] == os.environ['notify_transactional_content_html_list_field_address']:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : notify_transactional_content_html_list_field_address: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_dynamic_html is working Time : notify_transactional_content_html_list_field_address: failed')
        
    if mail_received_time - os.environ['nt_ch_dh_feed_send_schedule_date_mail_sending_time'] > "250":
        print('Test Notify Transactional Content HTML Feed Schedule Date "Is Working" Time : 250: pass')
    else:
        print('Test Notify Transactional Content HTML Feed Schedule Date "Is Working" Time : 250: failed')

        else:
            print('Dynamic Ocx Feed HTML Mail not received : Mail Not Received')

testOcxFeedHtmlData = Test_Ocx_Feed_Html()
testOcxFeedHtml = testOcxFeedHtmlData.json()
print("Test Ocx Feed Html : ",  json.dumps(testOcxFeedHtml, indent=4))
fieldValue = testOcxFeedHtml.split("~!@#~")
ocxFeedHtml = xml2Json(fieldValue[1])
mail_received_time = Math.round(Date.parse(testOcxFeedHtmlData.date)/1000)

if testOcxFeedHtmlData.status_code == 200:
    if ocxFeedHtml['div']['table']['tr'][0]['td'][0] == "Hotel name":
        print('Test Notify Transactional content HTML in ocx_feed_html is working Time : Hotel name: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_html is working Time : Hotel name: failed')
    if ocxFeedHtml['div']['table']['tr'][0]['td'][1] == "Hotel location":
        print('Test Notify Transactional content HTML in ocx_feed_html is working Time : Hotel location: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_html is working Time : Hotel location: failed')
    if ocxFeedHtml['div']['table']['tr'][0]['td'][2] == "First Name":
        print('Test Notify Transactional content HTML in ocx_feed_html is working Time : First Name: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_html is working Time : First Name: failed')
    if ocxFeedHtml['div']['table']['tr'][0]['td'][3] == "address":
        print('Test Notify Transactional content HTML in ocx_feed_html is working Time : address: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_html is working Time : address: failed')
    if ocxFeedHtml['div']['table']['tr'][1]['td'][0] == "BVN":
        print('Test Notify Transactional content HTML in ocx_feed_html is working Time : BVN: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_html is working Time : BVN: failed')
    if ocxFeedHtml['div']['table']['tr'][1]['td'][1] == "Ahmedabad":
        print('Test Notify Transactional content HTML in ocx_feed_html is working Time : Ahmedabad: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_html is working Time : Ahmedabad: failed')
    if ocxFeedHtml['div']['table']['tr'][1]['td'][2] == "Ongage":
        print('Test Notify Transactional content HTML in ocx_feed_html is working Time : Ongage: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_html is working Time : Ongage: failed')
    if ocxFeedHtml['div']['table']['tr'][1]['td'][3] == "Ahmedabad":
        print('Test Notify Transactional content HTML in ocx_feed_html is working Time : Ahmedabad: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed_html is working Time : Ahmedabad: failed')
        
    if mail_received_time - os.environ['notify_transactional_delay_html_sending_time'] > "250":
        print('Test Notify Transactional HTML Dealy Send in  is working Time : 250: pass')
    else:
        print('Test Notify Transactional HTML Dealy Send in  is working Time : 250: failed')

        else:
            testOcxFeedHtml1Data = Test_Ocx_Feed_Html1()
            testOcxFeedHtml1 = testOcxFeedHtml1Data.json()
            print("Test Ocx Feed Html1 : ",  json.dumps(testOcxFeedHtml1, indent=4))
            fieldValue = testOcxFeedHtml1.split("~!@#~")
            ocxFeedHtml = xml2Json(fieldValue[1])
            mail_received_time = Math.round(Date.parse(testOcxFeedHtml1Data.date)/1000)

            if testOcxFeedHtml1Data.status_code == 200:
                if ocxFeedHtml['div']['table']['tr'][0]['td'][0] == "Hotel name":
                    print('Test Notify Transactional content HTML in ocx_feed_html is working Time : Hotel name: pass')
                else:
                    print('Test Notify Transactional content HTML in ocx_feed_html is working Time : Hotel name: failed')
                if ocxFeedHtml['div']['table']['tr'][0]['td'][1] == "Hotel location":
                    print('Test Notify Transactional content HTML in ocx_feed_html is working Time : Hotel location: pass')
                else:
                    print('Test Notify Transactional content HTML in ocx_feed_html is working Time : Hotel location: failed')
                if ocxFeedHtml['div']['table']['tr'][0]['td'][2] == "First Name":
                    print('Test Notify Transactional content HTML in ocx_feed_html is working Time : First Name: pass')
                else:
                    print('Test Notify Transactional content HTML in ocx_feed_html is working Time : First Name: failed')
                if ocxFeedHtml['div']['table']['tr'][0]['td'][3] == "address":
                    print('Test Notify Transactional content HTML in ocx_feed_html is working Time : address: pass')
                else:
                    print('Test Notify Transactional content HTML in ocx_feed_html is working Time : address: failed')
                if ocxFeedHtml['div']['table']['tr'][1]['td'][0] == "BVN":
                    print('Test Notify Transactional content HTML in ocx_feed_html is working Time : BVN: pass')
                else:
                    print('Test Notify Transactional content HTML in ocx_feed_html is working Time : BVN: failed')
                if ocxFeedHtml['div']['table']['tr'][1]['td'][1] == "Ahmedabad":
                    print('Test Notify Transactional content HTML in ocx_feed_html is working Time : Ahmedabad: pass')
                else:
                    print('Test Notify Transactional content HTML in ocx_feed_html is working Time : Ahmedabad: failed')
                if ocxFeedHtml['div']['table']['tr'][1]['td'][2] == "Ongage":
                    print('Test Notify Transactional content HTML in ocx_feed_html is working Time : Ongage: pass')
                else:
                    print('Test Notify Transactional content HTML in ocx_feed_html is working Time : Ongage: failed')
                if ocxFeedHtml['div']['table']['tr'][1]['td'][3] == "Ahmedabad":
                    print('Test Notify Transactional content HTML in ocx_feed_html is working Time : Ahmedabad: pass')
                else:
                    print('Test Notify Transactional content HTML in ocx_feed_html is working Time : Ahmedabad: failed')
                    
                if mail_received_time - os.environ['notify_transactional_delay_html_sending_time'] > "250":
                    print('Test Notify Transactional HTML Dealy Send in  is working Time : 250: pass')
                else:
                    print('Test Notify Transactional HTML Dealy Send in  is working Time : 250: failed')

            else:
            print('Ocx Feed HTML Mail not received : Mail Not Received')

testOcxFeedData = Test_Ocx_Feed()
testOcxFeed = testOcxFeedData.json()
print("Test Ocx Feed : ",  json.dumps(testOcxFeed, indent=4))
fieldValue = testOcxFeed.split("~!@#~")
ocxFeedData = xml2Json(fieldValue[1])

if testOcxFeedData.status_code == 200:
    if ocxFeedData['table']['tbody']['tr'][0]['td'][0] == "Hotel Name":
        print('Test Notify Transactional content HTML in ocx_feed is working Time : Hotel Name: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed is working Time : Hotel Name: failed')
    if ocxFeedData['table']['tbody']['tr'][0]['td'][1] == "Location":
        print('Test Notify Transactional content HTML in ocx_feed is working Time : Location: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed is working Time : Location: failed')
    if ocxFeedData['table']['tbody']['tr'][0]['td'][2] == "Link":
        print('Test Notify Transactional content HTML in ocx_feed is working Time : Link: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed is working Time : Link: failed')
    if ocxFeedData['table']['tbody']['tr'][1]['td'][0] == "Regular":
        print('Test Notify Transactional content HTML in ocx_feed is working Time : Regular: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed is working Time : Regular: failed')
    if ocxFeedData['table']['tbody']['tr'][1]['td'][1] == "India":
        print('Test Notify Transactional content HTML in ocx_feed is working Time : India: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed is working Time : India: failed')
    if ocxFeedData['table']['tbody']['tr'][1]['td'][2] == "www.test.com":
        print('Test Notify Transactional content HTML in ocx_feed is working Time : www.test.com: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed is working Time : www.test.com: failed')
    if ocxFeedData['table']['tbody']['tr'][2]['td'][0] == "Suit":
        print('Test Notify Transactional content HTML in ocx_feed is working Time : Suit: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed is working Time : Suit: failed')
    if ocxFeedData['table']['tbody']['tr'][2]['td'][1] == "Rajasthan":
        print('Test Notify Transactional content HTML in ocx_feed is working Time : Rajasthan: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed is working Time : Rajasthan: failed')
    if ocxFeedData['table']['tbody']['tr'][2]['td'][2] == "www.google.com":
        print('Test Notify Transactional content HTML in ocx_feed is working Time : www.google.com: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_feed is working Time : www.google.com: failed')

    jsonFields = JSON.parse(fieldValue[2])

    if jsonFields['dyanmic_field']['zip1'] == "SiDev3":
        print('Test Notify Transactional content HTML message_dynamic_fields in String field "Is equals to" Time : SiDev3: pass')
    else:
        print('Test Notify Transactional content HTML message_dynamic_fields in String field "Is equals to" Time : SiDev3: failed')
    if jsonFields['dyanmic_field']['sr_no'] == "123":
        print('Test Notify Transactional content HTML message_dynamic_fields in numeric field "Is equals to" Time : 123: pass')
    else:
        print('Test Notify Transactional content HTML message_dynamic_fields in numeric field "Is equals to" Time : 123: failed')
    if jsonFields['dyanmic_field']['dob'] == "01/01/2020":
        print('Test Notify Transactional content HTML message_dynamic_fields in Date field "Is equals to" Time : 01/01/2020: pass')
    else:
        print('Test Notify Transactional content HTML message_dynamic_fields in Date field "Is equals to" Time : 01/01/2020: failed')

    else:
        testOcxFeed1Data = Test_Ocx_Feed1()
        testOcxFeed1 = testOcxFeed1Data.json()
        print("Test Ocx Feed1 : ",  json.dumps(testOcxFeed1, indent=4))
        fieldValue = testOcxFeed1.split("~!@#~")
        ocxFeedData = xml2Json(fieldValue[1])

        if testOcxFeed1Data.status_code == 200:
            if ocxFeedData['table']['tbody']['tr'][0]['td'][0] == "Hotel Name":
                print('Test Notify Transactional content HTML in ocx_feed is working Time : Hotel Name: pass')
            else:
                print('Test Notify Transactional content HTML in ocx_feed is working Time : Hotel Name: failed')
            if ocxFeedData['table']['tbody']['tr'][0]['td'][1] == "Location":
                print('Test Notify Transactional content HTML in ocx_feed is working Time : Location: pass')
            else:
                print('Test Notify Transactional content HTML in ocx_feed is working Time : Location: failed')
            if ocxFeedData['table']['tbody']['tr'][0]['td'][2] == "Link":
                print('Test Notify Transactional content HTML in ocx_feed is working Time : Link: pass')
            else:
                print('Test Notify Transactional content HTML in ocx_feed is working Time : Link: failed')
            if ocxFeedData['table']['tbody']['tr'][1]['td'][0] == "Regular":
                print('Test Notify Transactional content HTML in ocx_feed is working Time : Regular: pass')
            else:
                print('Test Notify Transactional content HTML in ocx_feed is working Time : Regular: failed')
            if ocxFeedData['table']['tbody']['tr'][1]['td'][1] == "India":
                print('Test Notify Transactional content HTML in ocx_feed is working Time : India: pass')
            else:
                print('Test Notify Transactional content HTML in ocx_feed is working Time : India: failed')
            if ocxFeedData['table']['tbody']['tr'][1]['td'][2] == "www.test.com":
                print('Test Notify Transactional content HTML in ocx_feed is working Time : www.test.com: pass')
            else:
                print('Test Notify Transactional content HTML in ocx_feed is working Time : www.test.com: failed')
            if ocxFeedData['table']['tbody']['tr'][2]['td'][0] == "Suit":
                print('Test Notify Transactional content HTML in ocx_feed is working Time : Suit: pass')
            else:
                print('Test Notify Transactional content HTML in ocx_feed is working Time : Suit: failed')
            if ocxFeedData['table']['tbody']['tr'][2]['td'][1] == "Rajasthan":
                print('Test Notify Transactional content HTML in ocx_feed is working Time : Rajasthan: pass')
            else:
                print('Test Notify Transactional content HTML in ocx_feed is working Time : Rajasthan: failed')
            if ocxFeedData['table']['tbody']['tr'][2]['td'][2] == "www.google.com":
                print('Test Notify Transactional content HTML in ocx_feed is working Time : www.google.com: pass')
            else:
                print('Test Notify Transactional content HTML in ocx_feed is working Time : www.google.com: failed')

            jsonFields = JSON.parse(fieldValue[2])

            if jsonFields['dyanmic_field']['zip1'] == "SiDev3":
                print('Test Notify Transactional content HTML message_dynamic_fields in String field "Is equals to" Time : SiDev3: pass')
            else:
                print('Test Notify Transactional content HTML message_dynamic_fields in String field "Is equals to" Time : SiDev3: failed')
            if jsonFields['dyanmic_field']['sr_no'] == "123":
                print('Test Notify Transactional content HTML message_dynamic_fields in numeric field "Is equals to" Time : 123: pass')
            else:
                print('Test Notify Transactional content HTML message_dynamic_fields in numeric field "Is equals to" Time : 123: failed')
            if jsonFields['dyanmic_field']['dob'] == "01/01/2020":
                print('Test Notify Transactional content HTML message_dynamic_fields in Date field "Is equals to" Time : 01/01/2020: pass')
            else:
                print('Test Notify Transactional content HTML message_dynamic_fields in Date field "Is equals to" Time : 01/01/2020: failed')

        else:
            print('Ocx Feed Mail not received : Mail Not Received')

TestOcxFeedRssData = Test_Ocx_Feed_Rss()
TestOcxFeedRss = TestOcxFeedRssData.json()
print("Test Ocx Feed Rss : ",  json.dumps(TestOcxFeedRss, indent=4))
count = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0
count11 = 0
count12 = 0
count13 = 0
fieldValue = TestOcxFeedRss.split("~!@#~")
ocxRSSTitle = fieldValue[1]
ocxRSSLink = fieldValue[2]
ocxRSSDesc = fieldValue[3]

if TestOcxFeedRssData.status_code == 200:
    if ocxRSSTitle == os.environ['ocx_rss_title']:
        print('Test Notify Transactional content HTML in ocx_rss with title "Is equals to" Time : ocx_rss_title: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_rss with title "Is equals to" Time : ocx_rss_title: failed')
    if ocxRSSLink == os.environ['ocx_rss_link']:
        print('Test Notify Transactional content HTML in ocx_rss with link "Is equals to" Time : ocx_rss_link: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_rss with link "Is equals to" Time : ocx_rss_link: failed')
    if ocxRSSDesc == os.environ['ocx_rss_desc']:
        print('Test Notify Transactional content HTML in ocx_rss with description "Is equals to" Time : ocx_rss_desc: pass')
    else:
        print('Test Notify Transactional content HTML in ocx_rss with description "Is equals to" Time : ocx_rss_desc: failed')

    jsonFields = JSON.parse(fieldValue[4])

    if jsonFields['dyanmic_field']['zip1'] == "SiDev3":
        print('Test Notify Transactional content HTML message_dynamic_fields_per_recipient in String field "Is equals to" Time : SiDev3: pass')
    else:
        print('Test Notify Transactional content HTML message_dynamic_fields_per_recipient in String field "Is equals to" Time : SiDev3: failed')
    if parse(jsonFields['dyanmic_field']['sr_no']) == "123":
        print('Test Notify Transactional content HTML message_dynamic_fields_per_recipient in numeric field "Is equals to" Time : 123: pass')
    else:
        print('Test Notify Transactional content HTML message_dynamic_fields_per_recipient in numeric field "Is equals to" Time : 123: failed')
    if jsonFields['dyanmic_field']['dob'] == "01/01/2020":
        print('Test Notify Transactional content HTML message_dynamic_fields_per_recipient in Date field "Is equals to" Time : 01/01/2020: pass')
    else:
        print('Test Notify Transactional content HTML message_dynamic_fields_per_recipient in Date field "Is equals to" Time : 01/01/2020: failed')

    TestOcxFeedRssData.headerLines.forEach(def(data, index)

    if data['key']['toLowerCase()'] === "x-customheader":
        count = count + 1
        header = data.line.split(":")
        if header[0]['toLowerCase()'] == "x-customheader":
            print('Test Static customheader "Is Working" Time : x-customheader: pass')
        else:
            print('Test Static customheader "Is Working" Time : x-customheader: failed')
        if header[1]['toLowerCase()']['trim()'] == "test":
            print('Test Static customheader "Is Working" Time : test: pass')
        else:
            print('Test Static customheader "Is Working" Time : test: failed')

    if data['key']['toLowerCase()'] === "x-esp_id":
        count2 = count2 + 1
        header = data.line.split(":")
        if header[0]['toLowerCase()'] == "x-esp_id":
            print('Test Esp ID customheader "Is Working" Time : x-esp_id: pass')
        else:
            print('Test Esp ID customheader "Is Working" Time : x-esp_id: failed')
        if header[1]['toLowerCase()']['trim()'] == "espId":
            print('Test Esp ID customheader "Is Working" Time : espId: pass')
        else:
            print('Test Esp ID customheader "Is Working" Time : espId: failed')

    if data['key']['toLowerCase()'] === "x-list_id":
        count3 = count3 + 1
        header = data.line.split(":")
        if header[0]['toLowerCase()'] == "x-list_id":
            print('Test List ID customheader "Is Working" Time : x-list_id: pass')
        else:
            print('Test List ID customheader "Is Working" Time : x-list_id: failed')
        if header[1]['toLowerCase()']['trim()'] == "list_id":
            print('Test List ID customheader "Is Working" Time : list_id: pass')
        else:
            print('Test List ID customheader "Is Working" Time : list_id: failed')
        
    if data['key']['toLowerCase()'] === "x-mailing_id":
        count4 = count4 + 1
        header = data.line.split(":")
        if header[0]['toLowerCase()'] == "x-mailing_id":
            print('Test Mailing ID customheader "Is Working" Time : x-mailing_id: pass')
        else:
            print('Test Mailing ID customheader "Is Working" Time : x-mailing_id: failed')
        if header[1]['toLowerCase()']['trim()'] == parse(os.environ['nt_html_id_maling_id']):
            print('Test Mailing ID customheader "Is Working" Time : nt_html_id_maling_id: pass')
        else:
            print('Test Mailing ID customheader "Is Working" Time : nt_html_id_maling_id: failed')
    
    if data['key']['toLowerCase()'] === "x-from_address":
        count6 = count6 + 1
        header = data.line.split(":")
        if header[0]['toLowerCase()'] == "x-from_address":
            print('Test From Address customheader "Is Working" Time : x-from_address: pass')
        else:
            print('Test From Address customheader "Is Working" Time : x-from_address: failed')
        if header[1]['toLowerCase()']['trim()'] == os.environ['system_field_from_address']:
            print('Test From Address customheader "Is Working" Time : system_field_from_address: pass')
        else:
            print('Test From Address customheader "Is Working" Time : system_field_from_address: failed')

    if data['key']['toLowerCase()'] === "x-friendly_from":
        count7 = count7 + 1
        header = data.line.split(":")
        if header[0]['toLowerCase()'] == "x-friendly_from":
            print('Test From Name customheader "Is Working" Time : x-friendly_from: pass')
        else:
            print('Test From Name customheader "Is Working" Time : x-friendly_from: failed')
        if header[1]['toLowerCase()']['trim()'] == os.environ['system_field_from_name']['toLowerCase()']:
            print('Test From Name customheader "Is Working" Time : system_field_from_name: pass')
        else:
            print('Test From Name customheader "Is Working" Time : system_field_from_name: failed')

    if data['key']['toLowerCase()'] === "x-connection_id":
        count8 = count8 + 1
        header = data.line.split(":")
        if header[0]['toLowerCase()'] == "x-connection_id":
            print('Test ConnectionId customheader "Is Working" Time : x-connection_id: pass')
        else:
            print('Test ConnectionId customheader "Is Working" Time : x-connection_id: failed')
        if header[1]['toLowerCase()']['trim()'] == os.environ['connectionId']:
            print('Test ConnectionId customheader "Is Working" Time : connectionId: pass')
        else:
            print('Test ConnectionId customheader "Is Working" Time : connectionId: failed')

    if data['key']['toLowerCase()'] === "x-from_address_domain":
        count9 = count9 + 1
        header = data.line.split(":")
        if header[0]['toLowerCase()'] == "x-from_address_domain":
            print('Test From Address Domin customheader "Is Working" Time : x-from_address_domain: pass')
        else:
            print('Test From Address Domin customheader "Is Working" Time : x-from_address_domain: failed')
        if header[1]['toLowerCase()']['trim()'] == os.environ['system_field_from_address_domain']:
            print('Test From Address Domin customheader "Is Working" Time : system_field_from_address_domain: pass')
        else:
            print('Test From Address Domin customheader "Is Working" Time : system_field_from_address_domain: failed')
        
    if data['key']['toLowerCase()'] === "x-subject":
        count10 = count10 + 1
        header = data.line.split(":")
        if header[0]['toLowerCase()'] == "x-subject":
            print('Test Subject customheader "Is Working" Time : x-subject: pass')
        else:
            print('Test Subject customheader "Is Working" Time : x-subject: failed')
        if header[1]['toLowerCase()']['trim()'] == TestOcxFeedRssData['subject']['toLowerCase()']:
            print('Test Subject customheader "Is Working" Time : Subject customheader: pass')
        else:
            print('Test Subject customheader "Is Working" Time : Subject customheader: failed')

    if data['key']['toLowerCase()'] === "x-contact_id":
        count11 = count11 + 1
        header = data.line.split(":")
        if header[0]['toLowerCase()'] == "x-contact_id":
            print('Test Contact_Id customheader "Is Working" Time : x-contact_id: pass')
        else:
            print('Test Contact_Id customheader "Is Working" Time : x-contact_id: failed')
        if header[1]['toLowerCase()']['trim()'] == os.environ['rc_contact_id']:
            print('Test Contact_Id customheader "Is Working" Time : rc_contact_id: pass')
        else:
            print('Test Contact_Id customheader "Is Working" Time : rc_contact_id: failed')

    if data['key']['toLowerCase()'] === "x-created_date":
        count12 = count12 + 1
        header = data.line.split(":")
        if header[0]['toLowerCase()'] == "x-created_date":
            print('Test Created_Date customheader "Is Working" Time : x-created_date: pass')
        else:
            print('Test Created_Date customheader "Is Working" Time : x-created_date: failed')
        if header[1]['toLowerCase()']['trim()']['toString()']['substring(0,7)'] == os.environ['rc_ocx_created_date']:
            print('Test Created_Date customheader "Is Working" Time : rc_ocx_created_date: pass')
        else:
            print('Test Created_Date customheader "Is Working" Time : rc_ocx_created_date: failed')

    if data['key']['toLowerCase()'] === "x-campaign_name":
        count13 = count13 + 1
        header = data.line.split(":")
        if header[0]['toLowerCase()'] == "x-campaign_name":
            print('Test campaign_Name customheader "Is Working" Time : x-campaign_name: pass')
        else:
            print('Test campaign_Name customheader "Is Working" Time : x-campaign_name: failed')
        if header[1]['toLowerCase()']['trim()'] == "transactional content html campaign"['toLowerCase()']:
            print('Test campaign_Name customheader "Is Working" Time : transactional content html campaign: pass')
        else:
            print('Test campaign_Name customheader "Is Working" Time : transactional content html campaign: failed'))

    if count != 1:
        if [''] == "Static":
            print('Test Static ID customheader "Is equals to" Time : Static: pass')
        else:
            print('Test Static ID customheader "Is equals to" Time : Static: failed')
    if count2 != 1:
        if [''] == "Esp ID":
            print('Test Esp ID customheader "Is equals to" Time : Esp ID: pass')
        else:
            print('Test Esp ID customheader "Is equals to" Time : Esp ID: failed')
    if count3 != 1:
        if [''] == "List ID":
            print('Test List ID customheader "Is equals to" Time : List ID: pass')
        else:
            print('Test List ID customheader "Is equals to" Time : List ID: failed')
    if count4 != 1:
        if [''] == "Mailing ID":
            print('Test Mailing ID customheader "Is equals to" Time : Mailing ID: pass')
        else:
            print('Test Mailing ID customheader "Is equals to" Time : Mailing ID: failed')
    if count6 != 1:
        if [''] == "From Address":
            print('Test From Address customheader "Is equals to" Time : From Address: pass')
        else:
            print('Test From Address customheader "Is equals to" Time : From Address: failed')
    if count7 != 1:
        if [''] == "From Name":
            print('Test From Name customheader "Is equals to" Time : From Name: pass')
        else:
            print('Test From Name customheader "Is equals to" Time : From Name: failed')
    if count8 != 1:
        if [''] == "ConnectionId":
            print('Test ConnectionId customheader "Is equals to" Time : ConnectionId: pass')
        else:
            print('Test ConnectionId customheader "Is equals to" Time : ConnectionId: failed')
    if count9 != 1:
        if [''] == "From Address Domin":
            print('Test From Address Domin customheader "Is equals to" Time : From Address Domin: pass')
        else:
            print('Test From Address Domin customheader "Is equals to" Time : From Address Domin: failed')
    if count10 != 1:
        if [''] == "Subject":
            print('Test subject customheader "Is equals to" Time : Subject: pass')
        else:
            print('Test subject customheader "Is equals to" Time : Subject: failed')
    if count11 != 1:
        if [''] == "contact_Id":
            print('Test contact_Id customheader "Is equals to" Time : contact_Id: pass')
        else:
            print('Test contact_Id customheader "Is equals to" Time : contact_Id: failed')
    if count12 != 1:
        if [''] == "created_date":
            print('Test Created_Date customheader "Is equals to" Time : created_date: pass')
        else:
            print('Test Created_Date customheader "Is equals to" Time : created_date: failed')
    if count13 != 1:
        if [''] == "campaign_Name":
            print('Test campaign_Name customheader "Is equals to" Time : campaign_Name: pass')
        else:
            print('Test campaign_Name customheader "Is equals to" Time : campaign_Name: failed')
    
else:
    TestOcxFeedRss1Data = Test_Ocx-Feed_Rss1()
    TestOcxFeedRss1 = TestOcxFeedRss1Data.json()
    print("Test Ocx Feed Rss 1 : ",  json.dumps(TestOcxFeedRss1, indent=4))
    count = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    count10 = 0
    count11 = 0
    count12 = 0
    count13 = 0
    fieldValue = TestOcxFeedRss1.split("~!@#~")
    ocxRSSTitle = fieldValue[1]
    ocxRSSLink = fieldValue[2]
    ocxRSSDesc = fieldValue[3]

    if TestOcxFeedRss1Data.status_code == 200:
        if ocxRSSTitle == os.environ['ocx_rss_title']:
            print('Test Notify Transactional content HTML in ocx_rss with title "Is equals to" Time : ocx_rss_title: pass')
        else:
            print('Test Notify Transactional content HTML in ocx_rss with title "Is equals to" Time : ocx_rss_title: failed')
        if ocxRSSLink == os.environ['ocx_rss_link']:
            print('Test Notify Transactional content HTML in ocx_rss with link "Is equals to" Time : ocx_rss_link: pass')
        else:
            print('Test Notify Transactional content HTML in ocx_rss with link "Is equals to" Time : ocx_rss_link: failed')
        if ocxRSSDesc == os.environ['ocx_rss_desc']:
            print('Test Notify Transactional content HTML in ocx_rss with description "Is equals to" Time : ocx_rss_desc: pass')
        else:
            print('Test Notify Transactional content HTML in ocx_rss with description "Is equals to" Time : ocx_rss_desc: failed')

        jsonFields = JSON.parse(fieldValue[4])

        if jsonFields['dyanmic_field']['zip1'] == "SiDev3":
            print('Test Notify Transactional content HTML message_dynamic_fields_per_recipient in String field "Is equals to" Time : SiDev3: pass')
        else:
            print('Test Notify Transactional content HTML message_dynamic_fields_per_recipient in String field "Is equals to" Time : SiDev3: failed')
        if parse(jsonFields['dyanmic_field']['sr_no']) == "123":
            print('Test Notify Transactional content HTML message_dynamic_fields_per_recipient in numeric field "Is equals to" Time : 123: pass')
        else:
            print('Test Notify Transactional content HTML message_dynamic_fields_per_recipient in numeric field "Is equals to" Time : 123: failed')
        if jsonFields['dyanmic_field']['dob'] == "01/01/2020":
            print('Test Notify Transactional content HTML message_dynamic_fields_per_recipient in Date field "Is equals to" Time : 01/01/2020: pass')
        else:
            print('Test Notify Transactional content HTML message_dynamic_fields_per_recipient in Date field "Is equals to" Time : 01/01/2020: failed')

        TestOcxFeedRss1Data.headerLines.forEach(def(data, index)

        if data['key']['toLowerCase()'] === "customheader":
            count = count + 1
            header = data.line.split(":")
            if header[0]['toLowerCase()'] == "customheader":
                print('Test Static customheader "Is Working" Time : customheader: pass')
            else:
                print('Test Static customheader "Is Working" Time : customheader: failed')
            if header[1]['toLowerCase()']['trim()'] == "test":
                print('Test Static customheader "Is Working" Time : test: pass')
            else:
                print('Test Static customheader "Is Working" Time : test: failed')

        if data['key']['toLowerCase()'] === "x-esp_id":
            count2 = count2 + 1
            header = data.line.split(":")
            if header[0]['toLowerCase()'] == "x-esp_id":
                print('Test Esp ID customheader "Is Working" Time : x-esp_id: pass')
            else:
                print('Test Esp ID customheader "Is Working" Time : x-esp_id: failed')
            if header[1]['toLowerCase()']['trim()'] == "espId":
                print('Test Esp ID customheader "Is Working" Time : espId: pass')
            else:
                print('Test Esp ID customheader "Is Working" Time : espId: failed')

        if data['key']['toLowerCase()'] === "x-list_id":
            count3 = count3 + 1
            header = data.line.split(":")
            if header[0]['toLowerCase()'] == "x-list_id":
                print('Test List ID customheader "Is Working" Time : x-list_id: pass')
            else:
                print('Test List ID customheader "Is Working" Time : x-list_id: failed')
            if header[1]['toLowerCase()']['trim()'] == "list_id":
                print('Test List ID customheader "Is Working" Time : list_id: pass')
            else:
                print('Test List ID customheader "Is Working" Time : list_id: failed')
            
        if data['key']['toLowerCase()'] === "x-mailing_id":
            count4 = count4 + 1
            header = data.line.split(":")
            if header[0]['toLowerCase()'] == "x-mailing_id":
                print('Test Mailing ID customheader "Is Working" Time : x-mailing_id: pass')
            else:
                print('Test Mailing ID customheader "Is Working" Time : x-mailing_id: failed')
            if header[1]['toLowerCase()']['trim()'] == parse(os.environ['nt_html_id_maling_id']):
                print('Test Mailing ID customheader "Is Working" Time : nt_html_id_maling_id: pass')
            else:
                print('Test Mailing ID customheader "Is Working" Time : nt_html_id_maling_id: failed')
        
        if data['key']['toLowerCase()'] === "x-from_address":
            count6 = count6 + 1
            header = data.line.split(":")
            if header[0]['toLowerCase()'] == "x-from_address":
                print('Test From Address customheader "Is Working" Time : x-from_address: pass')
            else:
                print('Test From Address customheader "Is Working" Time : x-from_address: failed')
            if header[1]['toLowerCase()']['trim()'] == os.environ['system_field_from_address']:
                print('Test From Address customheader "Is Working" Time : system_field_from_address: pass')
            else:
                print('Test From Address customheader "Is Working" Time : system_field_from_address: failed')

        if data['key']['toLowerCase()'] === "x-friendly_from":
            count7 = count7 + 1
            header = data.line.split(":")
            if header[0]['toLowerCase()'] == "x-friendly_from":
                print('Test From Name customheader "Is Working" Time : x-friendly_from: pass')
            else:
                print('Test From Name customheader "Is Working" Time : x-friendly_from: failed')
            if header[1]['toLowerCase()']['trim()'] == os.environ['system_field_from_name']['toLowerCase()']:
                print('Test From Name customheader "Is Working" Time : system_field_from_name: pass')
            else:
                print('Test From Name customheader "Is Working" Time : system_field_from_name: failed')

        if data['key']['toLowerCase()'] === "x-connection_id":
            count8 = count8 + 1
            header = data.line.split(":")
            if header[0]['toLowerCase()'] == "x-connection_id":
                print('Test ConnectionId customheader "Is Working" Time : x-connection_id: pass')
            else:
                print('Test ConnectionId customheader "Is Working" Time : x-connection_id: failed')
            if header[1]['toLowerCase()']['trim()'] == os.environ['connectionId']:
                print('Test ConnectionId customheader "Is Working" Time : connectionId: pass')
            else:
                print('Test ConnectionId customheader "Is Working" Time : connectionId: failed')

        if data['key']['toLowerCase()'] === "x-from_address_domain":
            count9 = count9 + 1
            header = data.line.split(":")
            if header[0]['toLowerCase()'] == "x-from_address_domain":
                print('Test From Address Domin customheader "Is Working" Time : x-from_address_domain: pass')
            else:
                print('Test From Address Domin customheader "Is Working" Time : x-from_address_domain: failed')
            if header[1]['toLowerCase()']['trim()'] == os.environ['system_field_from_address_domain']:
                print('Test From Address Domin customheader "Is Working" Time : system_field_from_address_domain: pass')
            else:
                print('Test From Address Domin customheader "Is Working" Time : system_field_from_address_domain: failed')
            
        if data['key']['toLowerCase()'] === "x-subject":
            count10 = count10 + 1
            header = data.line.split(":")
            if header[0]['toLowerCase()'] == "x-subject":
                print('Test Subject customheader "Is Working" Time : x-subject: pass')
            else:
                print('Test Subject customheader "Is Working" Time : x-subject: failed')
            if header[1]['toLowerCase()']['trim()'] == TestOcxFeedRssData['subject']['toLowerCase()']:
                print('Test Subject customheader "Is Working" Time : Subject customheader: pass')
            else:
                print('Test Subject customheader "Is Working" Time : Subject customheader: failed')

        if data['key']['toLowerCase()'] === "x-contact_id":
            count11 = count11 + 1
            header = data.line.split(":")
            if header[0]['toLowerCase()'] == "x-contact_id":
                print('Test Contact_Id customheader "Is Working" Time : x-contact_id: pass')
            else:
                print('Test Contact_Id customheader "Is Working" Time : x-contact_id: failed')
            if header[1]['toLowerCase()']['trim()'] == os.environ['rc_contact_id']:
                print('Test Contact_Id customheader "Is Working" Time : rc_contact_id: pass')
            else:
                print('Test Contact_Id customheader "Is Working" Time : rc_contact_id: failed')

        if data['key']['toLowerCase()'] === "x-created_date":
            count12 = count12 + 1
            header = data.line.split(":")
            if header[0]['toLowerCase()'] == "x-created_date":
                print('Test Created_Date customheader "Is Working" Time : x-created_date: pass')
            else:
                print('Test Created_Date customheader "Is Working" Time : x-created_date: failed')
            if header[1]['toLowerCase()']['trim()']['toString()']['substring(0,7)'] == os.environ['rc_ocx_created_date']:
                print('Test Created_Date customheader "Is Working" Time : rc_ocx_created_date: pass')
            else:
                print('Test Created_Date customheader "Is Working" Time : rc_ocx_created_date: failed')

        if data['key']['toLowerCase()'] === "x-campaign_name":
            count13 = count13 + 1
            header = data.line.split(":")
            if header[0]['toLowerCase()'] == "x-campaign_name":
                print('Test campaign_Name customheader "Is Working" Time : x-campaign_name: pass')
            else:
                print('Test campaign_Name customheader "Is Working" Time : x-campaign_name: failed')
            if header[1]['toLowerCase()']['trim()'] == "transactional content html campaign"['toLowerCase()']:
                print('Test campaign_Name customheader "Is Working" Time : transactional content html campaign: pass')
            else:
                print('Test campaign_Name customheader "Is Working" Time : transactional content html campaign: failed'))

        if count != 1:
            if [''] == "Static":
                print('Test Static ID customheader "Is equals to" Time : Static: pass')
            else:
                print('Test Static ID customheader "Is equals to" Time : Static: failed')
        if count2 != 1:
            if [''] == "Esp ID":
                print('Test Esp ID customheader "Is equals to" Time : Esp ID: pass')
            else:
                print('Test Esp ID customheader "Is equals to" Time : Esp ID: failed')
        if count3 != 1:
            if [''] == "List ID":
                print('Test List ID customheader "Is equals to" Time : List ID: pass')
            else:
                print('Test List ID customheader "Is equals to" Time : List ID: failed')
        if count4 != 1:
            if [''] == "Mailing ID":
                print('Test Mailing ID customheader "Is equals to" Time : Mailing ID: pass')
            else:
                print('Test Mailing ID customheader "Is equals to" Time : Mailing ID: failed')
        if count6 != 1:
            if [''] == "From Address":
                print('Test From Address customheader "Is equals to" Time : From Address: pass')
            else:
                print('Test From Address customheader "Is equals to" Time : From Address: failed')
        if count7 != 1:
            if [''] == "From Name":
                print('Test From Name customheader "Is equals to" Time : From Name: pass')
            else:
                print('Test From Name customheader "Is equals to" Time : From Name: failed')
        if count8 != 1:
            if [''] == "ConnectionId":
                print('Test ConnectionId customheader "Is equals to" Time : ConnectionId: pass')
            else:
                print('Test ConnectionId customheader "Is equals to" Time : ConnectionId: failed')
        if count9 != 1:
            if [''] == "From Address Domin":
                print('Test From Address Domin customheader "Is equals to" Time : From Address Domin: pass')
            else:
                print('Test From Address Domin customheader "Is equals to" Time : From Address Domin: failed')
        if count10 != 1:
            if [''] == "Subject":
                print('Test subject customheader "Is equals to" Time : Subject: pass')
            else:
                print('Test subject customheader "Is equals to" Time : Subject: failed')
        if count11 != 1:
            if [''] == "contact_Id":
                print('Test contact_Id customheader "Is equals to" Time : contact_Id: pass')
            else:
                print('Test contact_Id customheader "Is equals to" Time : contact_Id: failed')
        if count12 != 1:
            if [''] == "created_date":
                print('Test Created_Date customheader "Is equals to" Time : created_date: pass')
            else:
                print('Test Created_Date customheader "Is equals to" Time : created_date: failed')
        if count13 != 1:
            if [''] == "campaign_Name":
                print('Test campaign_Name customheader "Is equals to" Time : campaign_Name: pass')
            else:
                print('Test campaign_Name customheader "Is equals to" Time : campaign_Name: failed')

            else:
            print('Ocx Feed RSS Mail not received : Mail Not Received')

TestDistinctCaseData = Test_Distinct_Case()
TestDistinctCase = TestDistinctCaseData.json()
print("Test Distinct Case : ",  json.dumps(TestDistinctCase, indent=4))
fieldValue = TestDistinctCase.split("<br>")

if TestDistinctCaseData.status_code == 200:
    if fieldValue[2] == " Regular name:Hilton Distinct name: - Location:NYC ":
        print('Test Notify Transactional Send Content HTML Id Distinct Case "Is Working" Time :  Regular name:Hilton Distinct name: - Location:NYC : pass')
    else:
        print('Test Notify Transactional Send Content HTML Id Distinct Case "Is Working" Time :  Regular name:Hilton Distinct name: - Location:NYC : failed')
    if fieldValue[4] == " Regular name:Hilton Distinct name: - Location:LA ":
        print('Test Notify Transactional Send Content HTML Id Distinct Case "Is Working" Time :  Regular name:Hilton Distinct name: - Location:LA : pass')
    else:
        print('Test Notify Transactional Send Content HTML Id Distinct Case "Is Working" Time :  Regular name:Hilton Distinct name: - Location:LA : failed')
    if fieldValue[6] == " Regular name:Hilton Distinct name: - Location:SF ":
        print('Test Notify Transactional Send Content HTML Id Distinct Case "Is Working" Time :  Regular name:Hilton Distinct name: - Location:SF : pass')
    else:
        print('Test Notify Transactional Send Content HTML Id Distinct Case "Is Working" Time :  Regular name:Hilton Distinct name: - Location:SF : failed')
    if fieldValue[8] == " Regular name:Holiday Inn Distinct name: - Location:LA ":
        print('Test Notify Transactional Send Content HTML Id Distinct Case "Is Working" Time :  Regular name:Holiday Inn Distinct name: - Location:LA : pass')
    else:
        print('Test Notify Transactional Send Content HTML Id Distinct Case "Is Working" Time :  Regular name:Holiday Inn Distinct name: - Location:LA : failed')

else:
    TestDistinctCase1Data = Test_Distinct_Case_1()
    TestDistinctCase1 = TestDistinctCase1Data.json()
    print("Test Distinct Case 1 : ",  json.dumps(TestDistinctCase1, indent=4))
    fieldValue = TestDistinctCase.split("<br>")

    if TestDistinctCase1Data.status_code == 200:
        if fieldValue[2] == " Regular name:Hilton Distinct name: - Location:NYC ":
            print('Test Notify Transactional Send Content HTML Id Distinct Case "Is Working" Time :  Regular name:Hilton Distinct name: - Location:NYC : pass')
        else:
            print('Test Notify Transactional Send Content HTML Id Distinct Case "Is Working" Time :  Regular name:Hilton Distinct name: - Location:NYC : failed')
        if fieldValue[4] == " Regular name:Hilton Distinct name: - Location:LA ":
            print('Test Notify Transactional Send Content HTML Id Distinct Case "Is Working" Time :  Regular name:Hilton Distinct name: - Location:LA : pass')
        else:
            print('Test Notify Transactional Send Content HTML Id Distinct Case "Is Working" Time :  Regular name:Hilton Distinct name: - Location:LA : failed')
        if fieldValue[6] == " Regular name:Hilton Distinct name: - Location:SF ":
            print('Test Notify Transactional Send Content HTML Id Distinct Case "Is Working" Time :  Regular name:Hilton Distinct name: - Location:SF : pass')
        else:
            print('Test Notify Transactional Send Content HTML Id Distinct Case "Is Working" Time :  Regular name:Hilton Distinct name: - Location:SF : failed')
        if fieldValue[8] == " Regular name:Holiday Inn Distinct name: - Location:LA ":
            print('Test Notify Transactional Send Content HTML Id Distinct Case "Is Working" Time :  Regular name:Holiday Inn Distinct name: - Location:LA : pass')
        else:
            print('Test Notify Transactional Send Content HTML Id Distinct Case "Is Working" Time :  Regular name:Holiday Inn Distinct name: - Location:LA : failed')



















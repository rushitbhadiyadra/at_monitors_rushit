from fixtures.delay import *
from fixtures.get_contact_info import *
from fixtures.get_last_mail_by_subject import *
from fixtures.behaviour_stats import *
from All_Esps_AB_Winner_Dynamic_Ocx_feed.change_contact_status import *
from All_Esps_AB_Winner_Dynamic_Ocx_feed.test_dynamic_feeds import *
from All_Esps_AB_Winner_Dynamic_Ocx_feed.create_and_send_campaign import *

changeContactStatusData = change_contact_status()
changeContactStatus = changeContactStatusData.json()
print("Change Contact Status : ", json.dumps(changeContactStatus, indent=4) )

##Get Contact Info 1
getContactInfoData = get_contact_info('ae_abw_dy_of_htm1@hoohem.com')
getContactInfo = getContactInfoData.json()
print("Get Contact Info 1 : ae_abw_dy_of_htm1@hoohem.com : ", json.dumps(getContactInfo, indent=4) )

if getContactInfoData.status_code == 200:
    os.environ['ab_winner_all_esp_list_field_first_name1'] = getContactInfo['payload']['first_name']
    os.environ['ab_winner_all_esp_list_field_address1'] = getContactInfo['payload']['address']
else:
    print("Get Contact Info 1 : ae_abw_dy_of_htm1@hoohem.com : Failed")

##Get Contact Info 2
getContactInfoData2 = get_contact_info('ae_abw_dy_of_htm2@hoohem.com')
getContactInfo2 = getContactInfoData2.json()
print("Get Contact Info 2 : ae_abw_dy_of_htm2@hoohem.com : ", json.dumps(getContactInfo2, indent=4) )

if getContactInfoData2.status_code == 200:
    os.environ['ab_winner_all_esp_list_field_first_name2'] = getContactInfo2['payload']['first_name']
    os.environ['ab_winner_all_esp_list_field_address2'] = getContactInfo2['payload']['address']
else:
    print("Get Contact Info 2 : ae_abw_dy_of_htm2@hoohem.com : Failed")

##Get Contact Info 3
getContactInfoData3 = get_contact_info('ae_abw_dy_of_htm2@hoohem.com')
getContactInfo3 = getContactInfoData3.json()
print("Get Contact Info 3 : ae_abw_dy_of_htm3@hoohem.com : ", json.dumps(getContactInfo3, indent=4) )

if getContactInfoData3.status_code == 200:
    os.environ['ab_winner_all_esp_list_field_first_name3'] = getContactInfo3['payload']['first_name']
    os.environ['ab_winner_all_esp_list_field_address3'] = getContactInfo3['payload']['address']
else:
    print("Get Contact Info 3 : ae_abw_dy_of_htm3@hoohem.com : Failed")

test_dynamic_feeds(1)

##Create_and_send_campaign_Dynamic_ocx_feed
create_and_send_campaign_dynamic_ocx_feedData = create_and_send_campaign('All Esp AB Winner Dynamic Ocx Feed', int(os.environ['msg_id_ab_win_send_dynamic_ocx_feed']), int(os.environ['all_esp_segment_id_ab_winner_dynamic_ocx_feed']))
create_and_send_campaign_dynamic_ocx_feed = create_and_send_campaign_dynamic_ocx_feedData.json()
print("Create_and_send_campaign_Dynamic_ocx_feed : ", json.dumps(create_and_send_campaign_dynamic_ocx_feed, indent=4) )

if create_and_send_campaign_dynamic_ocx_feedData.status_code == 200:
    os.environ['all_esp_ab_winner_dynamic_ocx_feed_content_delivery_campaign_id_'+os.environ['connectionId']] =  str(create_and_send_campaign_dynamic_ocx_feed['payload']['id'])
    os.environ['all_esp_ab_winner_dynamic_ocx_feed_content_delivery_campaign_name_'+os.environ['connectionId']] =  str(create_and_send_campaign_dynamic_ocx_feed['payload']['name'])
else:
    print("Create_and_send_campaign_Dynamic_ocx_feed : Failed send campaign")

##Create and send campaign Dynamic ocx feed html
create_and_send_campaign_dynamic_ocx_feed_html_data = create_and_send_campaign('All Esp AB Winner Dynamic Ocx Feed HTML', int(os.environ['msg_id_ab_win_send_dynamic_ocx_feed_html']), int(os.environ['all_esp_segment_id_ab_winner_dynamic_ocx_feed_html']))
create_and_send_campaign_dynamic_ocx_feed_html = create_and_send_campaign_dynamic_ocx_feed_html_data.json()
print("Create and send campaign Dynamic ocx feed html : ", json.dumps(create_and_send_campaign_dynamic_ocx_feed_html, indent=4) )

if create_and_send_campaign_dynamic_ocx_feed_html_data.status_code == 200:
    os.environ['all_esp_ab_winner_dynamic_ocx_feed_html_content_delivery_campaign_id_'+os.environ['connectionId']] =  str(create_and_send_campaign_dynamic_ocx_feed_html['payload']['id'])
    os.environ['all_esp_ab_winner_dynamic_ocx_feed_html_content_delivery_campaign_name_'+os.environ['connectionId']] =  str(create_and_send_campaign_dynamic_ocx_feed_html['payload']['name'])
else:
    print("Create and send campaign Dynamic ocx feed html : Failed send campaign")

##Create and send campaign ocx feed html
create_and_send_campaign_ocx_feed_html_data = create_and_send_campaign('All Esp AB Winner Ocx Feed HTML', int(os.environ['msg_id_ab_win_send_ocx_feed_html']), int(os.environ['all_esp_segment_id_ab_winner_ocx_feed_html']))
create_and_send_campaign_ocx_feed_html = create_and_send_campaign_ocx_feed_html_data.json()
print("Create and send campaign ocx feed html : ", json.dumps(create_and_send_campaign_ocx_feed_html, indent=4) )

if create_and_send_campaign_ocx_feed_html_data.status_code == 200:
    os.environ['all_esp_ab_winner_ocx_feed_html_content_delivery_campaign_id_'+os.environ['connectionId']] =  str(create_and_send_campaign_ocx_feed_html['payload']['id'])
    os.environ['all_esp_ab_winner_ocx_feed_html_content_delivery_campaign_name_'+os.environ['connectionId']] =  str(create_and_send_campaign_ocx_feed_html['payload']['name'])
else:
    print("Create and send campaign ocx feed html : Failed send campaign")

##Create and send campaign ocx feed
create_and_send_campaign_ocx_feed_data = create_and_send_campaign('All Esp AB Winner Ocx Feed', int(os.environ['msg_id_ab_win_send_ocx_feed']), int(os.environ['all_esp_segment_id_ab_winner_ocx_feed']))
create_and_send_campaign_ocx_feed = create_and_send_campaign_ocx_feed_data.json()
print("Create and send campaign ocx feed : ", json.dumps(create_and_send_campaign_ocx_feed, indent=4) )

if create_and_send_campaign_ocx_feed_data.status_code == 200:
    os.environ['all_esp_ab_winner_ocx_feed_content_delivery_campaign_id_'+os.environ['connectionId']] =  str(create_and_send_campaign_ocx_feed['payload']['id'])
    os.environ['all_esp_ab_winner_ocx_feed_content_delivery_campaign_name_'+os.environ['connectionId']] =  str(create_and_send_campaign_ocx_feed['payload']['name'])
else:
    print("Create and send campaign ocx feed : Failed send campaign")

##Create and send campaign ocx feed rss
create_and_send_campaign_ocx_feed_rss_data = create_and_send_campaign('All Esp AB Winner Ocx Feed rss', int(os.environ['msg_id_ab_win_send_ocx_feed_rss']), int(os.environ['all_esp_segment_id_ab_winner_ocx_feed_rss']))
create_and_send_campaign_ocx_feed_rss = create_and_send_campaign_ocx_feed_rss_data.json()
print("Create and send campaign ocx feed rss : ", json.dumps(create_and_send_campaign_ocx_feed_rss, indent=4) )

if create_and_send_campaign_ocx_feed_rss_data.status_code == 200:
    os.environ['all_esp_ab_winner_ocx_feed_rss_content_delivery_campaign_id_'+os.environ['connectionId']] =  str(create_and_send_campaign_ocx_feed_rss['payload']['id'])
    os.environ['all_esp_ab_winner_ocx_feed_rss_content_delivery_campaign_name_'+os.environ['connectionId']] =  str(create_and_send_campaign_ocx_feed_rss['payload']['name'])
else:
    print("Create and send campaign ocx feed rss : Failed send campaign")

delay(29)
delay(29)
delay(29)
delay(29)
delay(29)
delay(29)

test_dynamic_feeds(2)

openlink(str(os.environ['all_esp_ab_winner_dynamic_ocx_feed'+os.environ['connectionId']]))
openlink(str(os.environ['all_esp_ab_winner_dynamic_ocx_feed_html'+os.environ['connectionId']]))
openlink(str(os.environ['all_esp_ab_winner_ocx_feed_html'+os.environ['connectionId']]))
openlink(str(os.environ['all_esp_ab_winner_ocx_feed'+os.environ['connectionId']]))
openlink(str(os.environ['all_esp_ab_winner_ocx_feed_rss'+os.environ['connectionId']]))

del os.environ['all_esp_ab_winner_dynamic_ocx_feed'+os.environ['connectionId']]
del os.environ['all_esp_ab_winner_dynamic_ocx_feed_html'+os.environ['connectionId']]
del os.environ['all_esp_ab_winner_ocx_feed_html'+os.environ['connectionId']]
del os.environ['all_esp_ab_winner_ocx_feed'+os.environ['connectionId']]
del os.environ['all_esp_ab_winner_ocx_feed_rss'+os.environ['connectionId']]
del os.environ['all_esp_ab_winner_dynamic_ocx_feed_content_delivery_campaign_id_'+os.environ['connectionId']]
del os.environ['all_esp_ab_winner_dynamic_ocx_feed_content_delivery_campaign_name_'+os.environ['connectionId']]
del os.environ['all_esp_ab_winner_dynamic_ocx_feed_html_content_delivery_campaign_id_'+os.environ['connectionId']]
del os.environ['all_esp_ab_winner_dynamic_ocx_feed_html_content_delivery_campaign_name_'+os.environ['connectionId']]
del os.environ['all_esp_ab_winner_ocx_feed_html_content_delivery_campaign_id_'+os.environ['connectionId']]
del os.environ['all_esp_ab_winner_ocx_feed_html_content_delivery_campaign_name_'+os.environ['connectionId']]
del os.environ['all_esp_ab_winner_ocx_feed_content_delivery_campaign_id_'+os.environ['connectionId']]
del os.environ['all_esp_ab_winner_ocx_feed_content_delivery_campaign_name_'+os.environ['connectionId']]
del os.environ['all_esp_ab_winner_ocx_feed_rss_content_delivery_campaign_id_'+os.environ['connectionId']]
del os.environ['all_esp_ab_winner_ocx_feed_rss_content_delivery_campaign_name_'+os.environ['connectionId']]
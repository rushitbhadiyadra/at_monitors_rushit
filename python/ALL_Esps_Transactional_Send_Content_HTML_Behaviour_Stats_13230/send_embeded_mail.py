from env.config import *

def send_embeded_mail():

    url = '{api_domain}/{list_id}/api/transactional/send_embed_content'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id']
    )

    payload = json.dumps({
        "recipients": [
            "ae_trnsl_sd_htm_bs_"+os.environ['connectionId']+"@hoohem.com",
            "ae_trnsl_sd_htm_bs_1_"+os.environ['connectionId']+"@hoohem.com",
            "ae_trnsl_sd_htm_bs_2_"+os.environ['connectionId']+"@hoohem.com",
            "ae_trnsl_sd_htm_bs_3_"+os.environ['connectionId']+"@hoohem.com"
        ],
        "sending_connection_id": int(os.environ['connectionId']),
        "campaign_id": int(os.environ['all_esps_transactionsl_send_content_html_behaviour_stats_campaign_id']),
        "message":{
            "subject": "Test Transactional Send Content HTML Behavioral Stats-"+os.environ['connectionId']+"-"+os.environ['env'],
            "content_html": "<html><head><title></title><meta content='text/html; charset=utf-8' http-equiv='Content-Type' /></head><body><p><a data-title='Link' href='https://www.lipsum.com/'>Link</a></p></body></html>",
            "unsubscribe_default_link": True,
            "unsubscribe_confirmation_html_active": True,
            "unsubscribe_confirmation_html": "~!@#~To confirm you want to unsubscribe, please click the button below~!@#~ ",
            "unsubscribe_confirmation_button": "Unsubscribe",
            "frequency_active": False,
            "frequency_field_id": "",
            "unsubscribe_success_html_active": True,
            "unsubscribe_success_page": "text",
            "unsubscribe_success_html": "~!@#~You have been successfully unsubscribed~!@#~",
            "addresses": {
                "from_name": os.environ['system_field_from_name'],
                "from_address": os.environ['system_field_from_address'],
                "reply_address": os.environ['system_field_from_address']
            }
        },
    })

    return requests.request("POST", url, headers=headers, data=payload)
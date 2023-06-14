from env.config import *

def sendMail():

    url = '{api_domain}/{list_id}/api/transactional/send'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id']
    )

    payload = json.dumps({
        "recipients": [
            "ae_trnsl_sd_mail_bs_"+os.environ['connectionId']+"@hoohem.com",
            "ae_trnsl_sd_mail_bs_1_"+os.environ['connectionId']+"@hoohem.com",
            "ae_trnsl_sd_mail_bs_2_"+os.environ['connectionId']+"@hoohem.com",
            "ae_trnsl_sd_mail_bs_3_"+os.environ['connectionId']+"@hoohem.com"
        ],
        "message_id": int(os.environ['all_esp_behavioural_stats1']),
        "campaign_id": int(os.environ['all_esps_transactional_send_message_id_behaviour_stats_campaign_id']),
        "sending_connection_id": int(os.environ['connectionId']),
        "create_contact": False
    })

    return requests.request("POST", url, headers=headers, data=payload)
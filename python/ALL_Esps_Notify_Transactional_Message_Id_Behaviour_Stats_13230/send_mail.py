from env.config import *

def sendMail():

    url = '{api_domain}/{list_id}/api/notify_transactions'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id']
    )

    payload = json.dumps({
        "recipients": [
            "ae_nf_trnsl_msg_bs_"+os.environ['connectionId']+"@hoohem.com",
            "ae_nf_trnsl_msg_bs_1_"+os.environ['connectionId']+"@hoohem.com",
            "ae_nf_trnsl_msg_bs_2_"+os.environ['connectionId']+"@hoohem.com",
            "ae_nf_trnsl_msg_bs_3_"+os.environ['connectionId']+"@hoohem.com"
        ],
        "email_message_id": os.environ['all_esp_behavioural_stats1'],
        "campaign_id": os.environ['all_esps_notify_transactionsl_message_id_behaviour_stats_campaign_id'],
        "distribution": [
            {
                "esp_connection_id": os.environ['connectionId'],
                "domain": "default"
            }
        ]
    })

    return requests.request("POST", url, headers=headers, data=payload)
from env.config import *

def generate_contact_activity_report():

    current_GMT = time.time()
    current_date = round(current_GMT)   
    pre_date = round(current_GMT - (24*60*60))

    url = '{api_domain}/{list_id}/api/contact_activity'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id']
    )

    payload = json.dumps({
        "title": "Active gmail contacts",
        "selected_fields": [
            "email",
            "ocx_created_date",
            "ocx_status",
            "sent",
            "opens",
            "clicks",
            "ocx_unsubscribe_date",
            "ocx_resubscribe_date",
            "ocx_bounce_date",
            "ocx_complaint_date",
            "last_sent_date",
            "last_open_date"
        ],
        "filters": {
            "criteria": [
                {
                    "field_name": "sent",
                    "type": "behavioral",
                    "operator": "=",
                    "operand": {
                        "mailing_ids": [ os.environ['all_esps_transactional_send_message_id_behaviour_stats_campaign_id'] ]
                    },
                    "case_sensitive": 0,
                    "condition": "and"
                }
            ],
            "from_date": str(pre_date),
            "to_date": str(current_date)
        }
    })

    return requests.request("POST", url, headers=headers, data=payload)
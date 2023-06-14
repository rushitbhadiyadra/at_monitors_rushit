from env.config import *

def create_and_send_campaign(title, email_message_id,  segmentId):

    url = '{api_domain}/api/mailings/'.format(
        api_domain = os.environ['api_domain']
    )

    time_30 = round(time.time()) + 30

    payload = json.dumps({
        "name": str(title),
        "type": "split",
        "list_id": os.environ['list_id'],
        "split_type": "email",
        "email_message": [ 
            email_message_id,  
            os.environ['all_esp_ab_winner_common_message']
        ],
        "segments": [ str(segmentId) ],
        "distribution": [
            {
                "esp_connection_id": os.environ['connectionId'],
                "percent": 100
            }
        ],
        "schedule_date": time_30,
        "notify_onlaunch": "0",
        "notify_onfaile d": "0",
        "notify_oncomplete": "0",
        "has_winner_settings": True,
        "winner_is_quota_percent":"0",
        "winner_quota_value":"1",
        "winner_conversion_field":"unique_opens",
        "winner_send_after_hours":"1"
    })

    return requests.request("POST", url, headers=headers, data=payload)
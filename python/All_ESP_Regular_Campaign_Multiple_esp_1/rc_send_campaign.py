from env.config import *

def rc_send_campaign():

    time_30 = round(time.time()) + 30

    url = '{api_domain}/{list_id}/api/mailings/'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id']
    )
    
    payload = json.dumps(
        {
        "name": "All ESP Multipl Esp Regular Campaign",
        "list_id": os.environ['list_id'],
        "email_message": os.environ['ae_rc_multi_message_id'],
        "segments": [
            os.environ['all_esps_regular_campaign_segment_id_multiple_esp']
        ],
        "distribution": [
            {
                "esp_connection_id": os.environ['connectionId'],
                "percent": "50"
            },
            {
                "esp_connection_id": os.environ['connectionId1'],
                "percent": "50"
            }
        ],
        "schedule_date": time_30
        }
    )
    return requests.request("POST", url, headers=headers, data=payload)

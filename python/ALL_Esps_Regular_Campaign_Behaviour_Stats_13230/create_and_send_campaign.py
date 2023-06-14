from env.config import *

def create_and_send_campaign():

    time_30 = round(time.time()) + 30

    url = '{api_domain}/api/mailings'.format(
        api_domain = os.environ['api_domain']
    )

    payload = json.dumps({
        "name": "RC-Behaviour-Stats"+os.environ['connectionId'],
        "list_id": os.environ['list_id'],
        "email_message": os.environ['all_esp_rc_stats'],
        "segments": [ os.environ['segment_id_all_esps_regular_campaign_behavioural_stat'] ],
        "distribution": [
            {
                "esp_connection_id": os.environ['connectionId'],
                "percent": 100
            }
        ],
        "schedule_date": time_30
    })

    return requests.request("POST", url, headers=headers, data=payload)
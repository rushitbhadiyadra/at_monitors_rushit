from env.config import *

def rc_send_campaign():

    time_30 = round(time.time()) + 30

    url = '{api_domain}/{list_id}/api/mailings/'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id']
    )
    
    payload = json.dumps(
        {
        "name": "All ESP And Segment Level Distribution-"+os.environ['connectionId'],
        "list_id": os.environ['list_id'],
        "email_message": os.environ['msg_id_ae_ab_split_multi_esp'],
        "segments": [
            os.environ['all_esps_segment_id_esp_domin_test']
        ],
        "distribution": [
            {
                "esp_connection_id": os.environ['connectionId1'],
                "percent": "100",
                "domain": "gmail.com"
            },
            {
                "esp_connection_id": os.environ['connectionId'],
                "percent": "100",
                "domain": "hoohem.com"
            },
            {
                "esp_connection_id": os.environ['connectionId1'],
                "percent": "100",
                "domain": "default"
            }
        ],
        "schedule_date": time_30
        }
    )
    return requests.request("POST", url, headers=headers, data=payload)

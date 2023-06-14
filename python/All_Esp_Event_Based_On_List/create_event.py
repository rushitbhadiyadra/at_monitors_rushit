from env.config import *

def create_event(all_esps_event_and_trigger_based_list_segment_id,event_list_hours,event_list_minutes):

    url = '{api_domain}/{list_id}/api/events'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id']
    )

    payload = json.dumps({
        "name": "All ESP Event and trigger based list "+os.environ['connectionId'],
        "description": "",
        "event_type": "event_list",
        "based_on": "recurring",
        "ongoing_event": True,
        "status": True,
        "segments": [
            all_esps_event_and_trigger_based_list_segment_id
        ],
        "distribution": [
            {
            "esp_connection_id": os.environ['connectionId'],
            "domain": "default",
            "percent": "100"
            }
        ],
        "triggers": [
            {
            "based_on": "list",
            "email_messages": [
                "131545"
            ],
            "recurrence": {
                "pattern": "daily"
            },
            "operator": "after",
            "schedule_hour": event_list_hours,
            "schedule_minute": event_list_minutes
            }
        ]
    })
    
    return requests.request("POST", url, headers=headers, data=payload)
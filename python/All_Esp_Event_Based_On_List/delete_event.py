from env.config import *

def delete_event(event_id_event_bsed_on_list):

    url = '{api_domain}/{list_id}/api/events/{event_id_event_bsed_on_list}'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id'],
        event_id_event_bsed_on_list = os.environ['event_id_event_bsed_on_list']
    )

    payload = ""
    
    return requests.request("DELETE", url, headers=headers, data=payload)
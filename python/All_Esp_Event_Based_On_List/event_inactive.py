from env.config import *

def event_inactive():

    url = '{api_domain}/{list_id}/api/events/{event_id_event_bsed_on_list}/status'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id'],
        event_id_event_bsed_on_list = os.environ['event_id_event_bsed_on_list']
    )

    payload = ""
    
    return requests.request("PUT", url, headers=headers, data=payload)
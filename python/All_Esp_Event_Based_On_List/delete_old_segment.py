from env.config import *

def delete_old_segment(old_segment_id_event_list):

    url = '{api_domain}/{list_id}/api/segments/{old_segment_id_event_list}'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id'],
        old_segment_id_event_list = old_segment_id_event_list
    )

    payload = ""

    return requests.request("DELETE", url, headers=headers, data=payload)
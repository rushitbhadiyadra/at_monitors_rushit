from env.config import *

def delete_segment():

    url = '{api_domain}/{list_id}/api/segments/{all_esps_event_and_trigger_based_list_segment_id}'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id'],
        all_esps_event_and_trigger_based_list_segment_id = os.environ['all_esps_event_and_trigger_based_list_segment_id']
    )

    payload = ""

    return requests.request("DELETE", url, headers=headers, data=payload)
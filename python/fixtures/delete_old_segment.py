from env.config import *

def delete_old_segment(old_segment_id_bh_state):

    url = '{api_domain}/{list_id}/api/segments/{old_segment_id_bh_state}'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id'],
        old_segment_id_bh_state = old_segment_id_bh_state
    )

    payload = ""

    return requests.request("DELETE", url, headers=headers, data=payload)
from env.config import *

def get_old_segment():

    url = '{api_domain}/{list_id}/api/segments?limit=500'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id']
    )

    payload = ""

    return requests.request("GET", url, headers=headers, data=payload)
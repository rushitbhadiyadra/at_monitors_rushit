from env.config import *

def get_old_event():

    url = '{api_domain}/{list_id}/api/events'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id']
    )

    payload = ""

    return requests.request("GET", url, headers=headers, data=payload)
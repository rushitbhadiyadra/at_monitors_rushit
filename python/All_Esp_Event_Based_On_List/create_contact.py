from env.config import *

def create_contact():

    url = '{api_domain}/{list_id}/api/v2/contacts'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id']
    )

    payload = json.dumps({
        "email": "ae_rc_event_base_on_list"+os.environ['connectionId']+"@hoohem.com"
    })
    
    return requests.request("POST", url, headers=headers, data=payload)
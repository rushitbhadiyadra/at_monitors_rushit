from env.config import *

def create_contact():

    url = '{api_domain}/{list_id}/api/v2/contacts'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id']
    )

    payload = json.dumps([
    {
        "email": "ae_rc_multi_esp_1@hoohem.com"
    },
    {
        "email": "ae_rc_multi_esp_2@hoohem.com"
    }
    ])
    
    return requests.request("POST", url, headers=headers, data=payload)
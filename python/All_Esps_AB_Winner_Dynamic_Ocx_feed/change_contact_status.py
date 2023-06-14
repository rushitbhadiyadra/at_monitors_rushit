from env.config import *

def change_contact_status():

    url = '{api_domain}/{list_id}/api/v2/contacts/change_status'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id']
    )

    payload = json.dumps({
        "list_id": os.environ['list_id'],
        "change_to": "resubscribe",
        "emails": [
            "ae_abw_dy_of1@hoohem.com",
            "ae_abw_dy_of2@hoohem.com",
            "ae_abw_dy_of3@hoohem.com"
        ]
    })

    return requests.request("POST", url, headers=headers, data=payload)
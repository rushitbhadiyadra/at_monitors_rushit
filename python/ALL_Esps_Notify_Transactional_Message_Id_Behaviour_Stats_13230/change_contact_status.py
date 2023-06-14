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
            "ae_nf_trnsl_msg_bs_"+os.environ['connectionId']+"@hoohem.com",
            "ae_nf_trnsl_msg_bs_1_"+os.environ['connectionId']+"@hoohem.com",
            "ae_nf_trnsl_msg_bs_2_"+os.environ['connectionId']+"@hoohem.com",
            "ae_nf_trnsl_msg_bs_3_"+os.environ['connectionId']+"@hoohem.com"
        ]
    })

    return requests.request("POST", url, headers=headers, data=payload)
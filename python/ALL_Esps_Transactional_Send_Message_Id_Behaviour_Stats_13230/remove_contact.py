from env.config import *

def remove_contact():

    url = '{api_domain}/{list_id}/api/v2/contacts/change_status'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id']
    )

    payload = json.dumps({
        "list_id": os.environ['list_id'],
        "change_to": "remove",
        "emails": [
            "ae_trnsl_sd_mail_bs_"+os.environ['connectionId']+"@hoohem.com",
            "ae_trnsl_sd_mail_bs_1_"+os.environ['connectionId']+"@hoohem.com",
            "ae_trnsl_sd_mail_bs_2_"+os.environ['connectionId']+"@hoohem.com",
            "ae_trnsl_sd_mail_bs_3_"+os.environ['connectionId']+"@hoohem.com"
        ]
    })

    return requests.request("POST", url, headers=headers, data=payload)
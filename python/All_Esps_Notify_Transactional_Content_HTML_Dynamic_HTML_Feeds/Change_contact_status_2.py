from env.config import *

def delete_mail_by_id_and_subject():

    url = '{api_domain}/{list_id}/api/v2/contacts/change_status'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id']
    )

    payload = json.dumps({
      "list_id": os.environ['list_id'],
      "change_to": "unsubscribe",
      "emails": [
        "ae_nt_sd_htm_dy_of1@hoohem.com"
      ]
    })
    headers = {
      'X_USERNAME': 'bhushan.stepin@gmail.com',
      'X_PASSWORD': 'Bhushan@123',
      'X_ACCOUNT_CODE': 'stepin76',
      'Content-Type': 'application/json'
    }

    return requests.request("POST", url, headers=headers, data=payload)
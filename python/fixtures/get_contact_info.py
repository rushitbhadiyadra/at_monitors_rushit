from env.config import *

def get_contact_info(emailById):

    url = '{api_domain}/{list_id}/api/contacts/by_email/{emailId}'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id'],
        emailId = emailById
    )

    payload = ""

    return requests.request("GET", url, headers=headers, data=payload)
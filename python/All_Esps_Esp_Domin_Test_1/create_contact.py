from env.config import *

def create_contact():

    url = '{api_domain}/{list_id}/api/v2/contacts'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id']
    )

    payload = json.dumps([
    {
        "email": "ae_isp_domin@hoohem.com",
        "country": "India",
        "city": "bhavnagar"
    },
    {
        "email": "ongageqa.t443@gmail.com",
        "country": "India",
        "city": "bhavnagar"
    }
    ])
    
    return requests.request("POST", url, headers=headers, data=payload)
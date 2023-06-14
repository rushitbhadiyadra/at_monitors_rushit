from env.config import *

def create_transactional_campaign(name, description):

    url = '{api_domain}/api/transactional'.format(
        api_domain = os.environ['api_domain']
    )

    payload = json.dumps({
        "name": name,
        "description": description,
        "list_id": os.environ['list_id'],
        "message_type": "email"
    })
    
    return requests.request("POST", url, headers=headers, data=payload)
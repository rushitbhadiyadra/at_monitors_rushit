from env.config import *

def delete_mail_by_id_and_subject(username, subject):

    url = str(os.environ['maildbURL'])
    
    payload = json.dumps({
        "username": str(username),
        "subject": str(subject)
    })

    headers = {
        'Content-Type': 'application/json'
    }
    
    return requests.request("POST", url, headers=headers, data=payload)
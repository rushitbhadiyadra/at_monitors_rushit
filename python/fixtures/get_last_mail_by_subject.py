from env.config import *

def get_last_mail_by_subject(subject, timeout):

    url = os.environ['getLastMailBySubject']

    payload = json.dumps({
        "subject": str(subject),
        "timeout": timeout
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': str(os.environ['authorization'])
    }

    return requests.request("POST", url, headers=headers, data=payload)
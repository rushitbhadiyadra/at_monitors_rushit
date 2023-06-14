from env.config import *

def delete_mail_by_id_and_subject():

    url = str(os.environ['adMailURL'])

    payload = json.dumps({
      "username": "ae_nt_sd_htm_dy_of@hoohem.com",
      "subject": "Test Notify Transactional Send Content HTML Ocx Feed Html-"+os.environ['connectionId']+"-"+str(os.environ['env']),
      "timeout": 100000
    })
    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Basic cHJveHk6b25nYWdlcWE4Ng=='
    }

    return requests.request("POST", url, headers=headers, data=payload)
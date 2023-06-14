from env.config import *

def delete_mail_by_id_and_subject():

    url = str(os.environ['adMailURL'])

    payload = json.dumps({
      "username": "ae_nt_sd_htm_distinct@hoohem.com",
      "subject": "Test Notify Transactional Send Content Html Distinct Case-"+os.environ['connectionId']+,
      "timeout": 200000
    })
    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Basic cHJveHk6b25nYWdlcWE4Ng=='
    }

    return requests.request("POST", url, headers=headers, data=payload)
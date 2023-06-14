from env.config import *

def delete_mail_by_id_and_subject():

    url = str(os.environ['maildbURL'])

    payload = json.dumps({
      "username": "ae_nt_sd_htm_dy_of@hoohem.com",
      "subject": "Test Notify Transactional Send Content HTML Ocx Feed Rss-"+os.environ['connectionId']+"-"+str(os.environ['env'])
    })
    headers = {
      'Content-Type': 'application/json'
    }

    return requests.request("POST", url, headers=headers, data=payload)
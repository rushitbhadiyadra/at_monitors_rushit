from env.config import *

def delete_mail():

    url = 'https://automated_tests-l2.ongage.net/app/mail_db/mbox/subject/delete/ALl Esp Mirror Page-43766'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id']
    )

    payload = ""

    return requests.request("GET", url, headers=headers, data=payload)
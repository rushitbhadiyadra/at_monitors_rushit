from env.config import *

def contact_activity_report_result():

    url = '{api_domain}/{list_id}/api/contact_activity/{nt_message_id_behaviour_report_id}/result'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id'],
        nt_message_id_behaviour_report_id = os.environ['nt_message_id_behaviour_report_id']
    )

    payload = ""
    return requests.request("GET", url, headers=headers, data=payload)
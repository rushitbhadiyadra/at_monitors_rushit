from env.config import *

def contact_activity_report_result(report_id):

    url = '{api_domain}/{list_id}/api/contact_activity/{report_id}/result'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id'],
        report_id = report_id
    )

    payload = ""

    return requests.request("GET", url, headers=headers, data=payload)
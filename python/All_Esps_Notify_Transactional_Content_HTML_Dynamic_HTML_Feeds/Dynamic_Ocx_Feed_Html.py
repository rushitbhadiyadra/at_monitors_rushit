from env.config import *

def delete_mail_by_id_and_subject():

    url = '{api_domain}/{list_id}/api/notify_transactions'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id']
    )

    payload = "{\n    \"recipients\": [\n        \"ae_nt_sd_htm_dy_of@hoohem.com\"\n    ],\n    \"check_status\": true,\n    \"email_message\": {\n        \"subject\": \"Test Notify Transactional Send Content HTML Dynamic Ocx Feed Html-"+os.environ['connectionId']+"-"+str(os.environ['env'])"\",\n        \"content_html\": \"<html><head><title></title><meta content='text/html; charset=utf-8' http-equiv='Content-Type' /></head><body><p>~!@#~{{ocx_feed_dynamic_html{url=http://ongageqa.site/campaign_automated_test/bvn_test.html?dummy1={{first_name}}&dummy2={{address}}}}}~!@#~</p></body></html>\",\n        \"addresses\": [\n            {\n                \"from_name\": \"SiDev1\",\n                \"from_address\": \"sidev1@stepin-solutions.com\",\n                \"reply_address\": \"sidev1@stepin-solutions.com\",\n                \"esp_connection_id\": "+os.environ['connectionId']+"\n            }\n        ]\n    },\n    \"schedule_date\": ,\n    \"distribution\": [\n        {\n            \"esp_connection_id\": \""+os.environ['connectionId']+"\",\n            \"domain\": \"default\",\n            \"percent\": 100\n        }\n    ]\n}"
    headers = {
      'X_USERNAME': 'bhushan.stepin@gmail.com',
      'X_PASSWORD': 'Bhushan@123',
      'X_ACCOUNT_CODE': 'stepin76',
      'Content-Type': 'application/json'
    }

    return requests.request("POST", url, headers=headers, data=payload)
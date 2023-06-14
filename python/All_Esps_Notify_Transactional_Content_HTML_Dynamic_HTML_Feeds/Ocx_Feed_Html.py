from env.config import *

def delete_mail_by_id_and_subject():

    url = '{api_domain}/{list_id}/api/notify_transactions'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id']
    )

    payload = json.dumps({
      "recipients": [
        "ae_nt_sd_htm_dy_of@hoohem.com"
      ],
      "check_status": True,
      "email_message": {
        "subject": "Test Notify Transactional Send Content HTML Ocx Feed Html-"+os.environ['connectionId']+"-"+str(os.environ['env']),
        "content_html": "<html><head><title></title><meta content='text/html; charset=utf-8' http-equiv='Content-Type' /></head><body><span>~!@#~{{ocx_feed_html{url=http://ongageqa.site/campaign_automated_test/ocx_feed_html.html}}}~!@#~</span></body></html>",
        "addresses": [
          {
            "from_name": "SiDev1",
            "from_address": "sidev1@stepin-solutions.com",
            "reply_address": "sidev1@stepin-solutions.com",
            "esp_connection_id": os.environ['connectionId']
          }
        ]
      },
      "delay_send": 300,
      "distribution": [
        {
          "esp_connection_id": os.environ['connectionId'],
          "domain": "default",
          "percent": 100
        }
      ]
    })
    headers = {
      'X_USERNAME': 'bhushan.stepin@gmail.com',
      'X_PASSWORD': 'Bhushan@123',
      'X_ACCOUNT_CODE': 'stepin76',
      'Content-Type': 'application/json'
    }

    return requests.request("POST", url, headers=headers, data=payload)
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
      "campaign_id": 1091507448,
      "email_message": {
        "subject": "Test Notify Transactional Send Content HTML Ocx Feed Rss-"+os.environ['connectionId']+,
        "content_html": "<html><head><title></title><meta content=\"text/html; charset=utf-8\" http-equiv=\"Content-Type\" /></head><body> <span>~!@#~{{ocx_rss:%2Frss%2Fchannel%2Fitem%5B2%5D%2Ftitle:http%3A%2F%2Fongageqa.site%2Fcampaign_automated_test%2Focx_rss.xml}}~!@#~{{ocx_rss:%2Frss%2Fchannel%2Fitem%5B2%5D%2Flink:http%3A%2F%2Fongageqa.site%2Fcampaign_automated_test%2Focx_rss.xml}}~!@#~{{ocx_rss:%2Frss%2Fchannel%2Fitem%5B2%5D%2Fdescription:http%3A%2F%2Fongageqa.site%2Fcampaign_automated_test%2Focx_rss.xml}}~!@#~{&quot;dyanmic_field&quot;:{&quot;zip1&quot;:&quot;{{zip1}}&quot;,&quot;sr_no&quot;:&quot;{{sr_no}}&quot;,&quot;dob&quot;:&quot;{{dob}}&quot;}}~!@#~</span></body></html>",
        "addresses": [
          {
            "from_name": "SiDev1",
            "from_address": "sidev1@stepin-solutions.com",
            "reply_address": "sidev1@stepin-solutions.com",
            "esp_connection_id": os.environ['connectionId']
          }
        ]
      },
      "message_dynamic_fields_per_recipient": [
        {
          "recipient": "ae_nt_sd_htm_dy_of@hoohem.com",
          "key_value_collection": {
            "zip1": "SiDev3",
            "sr_no": 123,
            "dob": "01/01/2020"
          }
        }
      ],
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
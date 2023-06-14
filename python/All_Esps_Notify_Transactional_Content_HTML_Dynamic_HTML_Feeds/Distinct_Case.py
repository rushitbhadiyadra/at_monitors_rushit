from env.config import *

def delete_mail_by_id_and_subject():

    url = '{api_domain}/{list_id}/api/notify_transactions'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id']
    )

    payload = json.dumps({
      "recipients": [
        "ae_nt_sd_htm_distinct@hoohem.com"
      ],
      "check_status": True,
      "email_message": {
        "subject": "Test Notify Transactional Send Content Html Distinct Case-"+os.environ['connectionId']+,
        "content_html": "<html>\n\n <head>\n <meta content=\"text/html; charset=utf-8\" http-equiv=\"Content-Type\">\n <title></title>\n </head>\n\n <body data-gr-ext-disabled=\"forever\" data-gr-ext-installed=\"\" data-new-gr-c-s-check-loaded=\"14.1031.0\">{{ocx_feed{param=dynamic_feed}}}<br> {{ocx_loop{block=hotels}}} <br> Regular name:Harsh(Default) Distinct name: - Location:{{location}} <br>\n {{ocx_loop_end}}</body>\n\n</html>",
        "addresses": [
          {
            "from_name": "SiDev1",
            "from_address": "sidev1@stepin-solutions.com",
            "reply_address": "sidev1@stepin-solutions.com",
            "esp_connection_id": os.environ['list_id']
          }
        ]
      },
      "message_dynamic_fields": {
        "dynamic_feed": "<feed><mailing><blocks><block><name>hotels</name><items><item><variables><variable><key>name</key><value>Hilton</value></variable><variable><key>location</key><value>NYC</value></variable></variables></item><item><variables><variable><key>name</key><value>Hilton</value></variable><variable><key>location</key><value>LA</value></variable></variables></item><item><variables><variable><key>name</key><value>Hilton</value></variable><variable><key>location</key><value>SF</value></variable></variables></item><item><variables><variable><key>name</key><value>Holiday Inn</value></variable><variable><key>location</key><value>LA</value></variable></variables></item></items></block></blocks></mailing></feed>"
      },
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
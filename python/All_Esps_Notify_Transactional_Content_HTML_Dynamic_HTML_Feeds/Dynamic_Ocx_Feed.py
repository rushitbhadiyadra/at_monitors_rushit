from env.config import *

def delete_mail_by_id_and_subject():

    url = '{api_domain}/{list_id}/api/notify_transactions'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id']
    )

payload = json.dumps({
  "recipients": [
    "ae_nt_sd_htm_dy_of@hoohem.com",
    "ae_nt_sd_htm_dy_of1@hoohem.com"
  ],
  "check_status": True,
  "email_message": {
    "subject": "Test Notify Transactional Send Content HTML Dynamic Ocx Feed-"+os.environ['connectionId']+"-"+str(os.environ['env']),
    "content_html": "<html><head><title></title><meta content='text/html; charset=utf-8' http-equiv='Content-Type' /></head><body>{{timecur}}<span>~!@#~{{ocx_feed_dynamic{url=http://ongageqa.site/campaign_automated_test/dynamic_feed_creator/get_dynamic_feed.php?key={{city}}&feed_type=xml}}}<table border=1><tbody><tr><td>Hotel Name</td><td>Location</td><td>Rooms</td></tr>{{ocx_loop{block=jobs}}}<tr><td>Harsh(Default)</td><td>{{location}}</td><td><table border=1><tbody><tr><td>Room Type</td><td>Count</td></tr>{{ocx_loop{block=rooms}}}<tr><td>{{type}}</td><td>{{count}}</td></tr>{{ocx_loop_end}}</tbody></table></td></tr>{{ocx_loop_end}}</tbody></table>~!@#~</span></body></html>",
    "addresses": [
      {
        "from_name": "SiDev1",
        "from_address": "sidev1@stepin-solutions.com",
        "reply_address": "sidev1@stepin-solutions.com",
        "esp_connection_id": os.environ['connectionId']
      }
    ]
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
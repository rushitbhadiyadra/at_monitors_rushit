from env.config import *
import time

def generate_aggregated_report():

    url = '{api_domain}/{list_id}/api/reports/query'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id']
    )

    payload = json.dumps({
        "select": [
            "mailing_name",
            "mailing_type",
            "split_type",
            "mailing_name_id",
            [
                "MAX(`stats_date`)",
                "stats_date"
            ],
            [
                "MAX(`delivery_timestamp`)",
                "delivery_timestamp"
            ],
            [
                "schedule_date",
                "schedule_date"
            ],
            "sum(`targeted`)",
            "sum(`sent`)",
            "sum(`success`)",
            "sum(`failed`)",
            "sum(`opens`)",
            "sum(`unique_opens`)",
            "sum(`unsubscribes`)",
            "sum(`complaints`)",
            "sum(`clicks`)",
            "sum(`unique_clicks`)",
            "sum(`soft_bounces`)",
            "sum(`hard_bounces`)",
            "mailing_id",
            "sum(`post_back_clicks`)"
        ],
        "from": "mailing",
        "group": [
            "mailing_id"
        ],
        "order": [
            [
                "delivery_timestamp",
                "desc"
            ]
        ],
        "filter": [
            [
                "mailing_id",
                "IN",
                [ str(os.environ['all_esps_regular_campaign_behaviour_campaign_id']) ]
            ]
        ]
    })

    return requests.request("POST", url, headers=headers, data=payload)
from env.config import *

def create_segment_event_and_trigger():

    url = '{api_domain}/{list_id}/api/segments'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id']
    )

    payload = json.dumps({
        "name": "All ESP Event & trigger based list "+os.environ['connectionId'],
        "type": "Active",
        "description": "",
        "included_segment_cache": None,
        "excluded_segment_cache": None,
        "is_whitelist": False,
        "criteria": [
            {
            "condition": "and",
            "group": "",
            "field_id": "387951",
            "field_name": "",
            "type": "email",
            "position": 0,
            "is_external_operand": False,
            "operator": "=",
            "operand": [
                "ae_rc_event_base_on_list43766@hoohem.com"
            ],
            "is_external_operand_exists": "0",
            "left_parenthesis": 0,
            "right_parenthesis": 0
            }
        ],
        "default_whitelist_segment": False,
        "default_exclude_segment": 0,
        "default_include_segment": 0
    })
    
    return requests.request("POST", url, headers=headers, data=payload)
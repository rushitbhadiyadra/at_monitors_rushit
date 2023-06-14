from env.config import *

def create_contact():

    url = '{api_domain}/{list_id}/api/v2/contacts'.format(
        api_domain = os.environ['api_domain'],
        list_id = os.environ['list_id']
    )

    payload = json.dumps([
        {
            "email": "ae_trnsl_sd_htm_bs_"+os.environ['connectionId']+"@hoohem.com",
            "address": "ahmedabad",
            "country": "India",
            "first_name": "Si",
            "last_name": "Dev2",
            "gender": "Male",
            "ip": "50.18.254.253",
            "job_title": "LPN",
            "language": "English",
            "phone": "1234567890",
            "os": "Linux",
            "product_id": 123,
            "dob": "03/10/2020",
            "city": "bhavnagar",
            "street_name": "Radha and Krishana",
            "society_name": "Radha & Krishana",
            "middle_name": "ongage's",
            "state": "Gujarat",
            "query": "sales",
            "location": "78759",
            "industry": "sales",
            "keyword": "marketing",
            "zip": "63090",
            "search": "sales",
            "userip": "108.200.249.191",
            "s1": "ong166",
            "useragent": "useragent",
            "zip1": "95050"
        },
        {
            "email": "ae_trnsl_sd_htm_bs_1_"+os.environ['connectionId']+"@hoohem.com",
            "address": "ahmedabad",
            "country": "India",
            "first_name": "Si",
            "last_name": "Dev2",
            "gender": "Male",
            "ip": "50.18.254.253",
            "job_title": "LPN",
            "language": "English",
            "phone": "1234567890",
            "os": "Linux",
            "product_id": 123,
            "dob": "03/10/2020",
            "city": "bhavnagar",
            "street_name": "Radha and Krishana",
            "society_name": "Radha & Krishana",
            "middle_name": "ongage's",
            "state": "Gujarat",
            "query": "sales",
            "location": "78759",
            "industry": "sales",
            "keyword": "marketing",
            "zip": "63090",
            "search": "sales",
            "userip": "108.200.249.191",
            "s1": "ong166",
            "useragent": "useragent",
            "zip1": "95050"
        },
        {
            "email": "ae_trnsl_sd_htm_bs_2_"+os.environ['connectionId']+"@hoohem.com",
            "address": "ahmedabad",
            "country": "India",
            "first_name": "Si",
            "last_name": "Dev2",
            "gender": "Male",
            "ip": "50.18.254.253",
            "job_title": "LPN",
            "language": "English",
            "phone": "1234567890",
            "os": "Linux",
            "product_id": 123,
            "dob": "03/10/2020",
            "city": "bhavnagar",
            "street_name": "Radha and Krishana",
            "society_name": "Radha & Krishana",
            "middle_name": "ongage's",
            "state": "Gujarat",
            "query": "sales",
            "location": "78759",
            "industry": "sales",
            "keyword": "marketing",
            "zip": "63090",
            "search": "sales",
            "userip": "108.200.249.191",
            "s1": "ong166",
            "useragent": "useragent",
            "zip1": "95050"
        },
        {
            "email": "ae_trnsl_sd_htm_bs_3_"+os.environ['connectionId']+"@hoohem.com",
            "address": "ahmedabad",
            "country": "India",
            "first_name": "Si",
            "last_name": "Dev2",
            "gender": "Male",
            "ip": "50.18.254.253",
            "job_title": "LPN",
            "language": "English",
            "phone": "1234567890",
            "os": "Linux",
            "product_id": 123,
            "dob": "03/10/2020",
            "city": "bhavnagar",
            "street_name": "Radha and Krishana",
            "society_name": "Radha & Krishana",
            "middle_name": "ongage's",
            "state": "Gujarat",
            "query": "sales",
            "location": "78759",
            "industry": "sales",
            "keyword": "marketing",
            "zip": "63090",
            "search": "sales",
            "userip": "108.200.249.191",
            "s1": "ong166",
            "useragent": "useragent",
            "zip1": "95050"
        }
    ])
    
    return requests.request("POST", url, headers=headers, data=payload)
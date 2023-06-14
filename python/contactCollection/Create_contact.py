from env.config import *

def create_contact():
  
  url = '{api_domain}/{list_id}/api/v2/contacts'.format(
    api_domain = os.environ['api_domain'],
    list_id = os.environ['list_id']
  )

  payload = json.dumps([
    {
      "email": "github_test_45058@hoohem.com",
      "address": "ahmedabad"
    }
  ])

  response = requests.request("POST", url, headers= headers, data=payload)

  jsonResponseValue = response.json()

  os.environ['contact_id_github_test'] = 'github_test_45058@hoohem.com'

  if response.status_code == 200 :
    print('\nSuccessfully created contact')
  else:
    print('\nFailed creating contact')
    print(jsonResponseValue['payload']['code'])
    print(jsonResponseValue['payload']['message'])

  print("Contact Create Response\n")
  print (json.dumps(jsonResponseValue, indent=2))
  print("\n")
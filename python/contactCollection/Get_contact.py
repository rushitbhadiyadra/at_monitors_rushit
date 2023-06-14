from env.config import *

def get_contact():

  url = '{api_domain}/{list_id}/api/contacts/by_email/{contact_id_github_test}'.format(
    api_domain = os.environ['api_domain'],
    list_id = os.environ['list_id'],
    contact_id_github_test = os.environ['contact_id_github_test']
  )

  payload = ""
  response = requests.request("GET", url, headers=headers, data=payload)

  jsonResponseValue = response.json()

  if response.status_code == 200 :
    print('\nPassed')
  else:
    print('\nFailed getting contact')
    print(jsonResponseValue['payload']['code'])
    print(jsonResponseValue['payload']['message'])
  
  print("\nContact Details\n")
  print (json.dumps(jsonResponseValue, indent=2))
  print("\n")

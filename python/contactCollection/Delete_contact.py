from env.config import *

def delete_contact():
  url = '{api_domain}/{list_id}/api/contacts/change_status'.format(
    api_domain = os.environ['api_domain'],
    list_id = os.environ['list_id']
  )

  payload = json.dumps({
    "change_to": "remove",
    "emails": [ os.environ['contact_id_github_test'] ]
  })

  response = requests.request("POST", url, headers=headers, data=payload)

  jsonResponseValue = response.json()

  if response.status_code == 200 :
    print('\nPassed')
  else:
    print('\nFailed deleting contact')
    print(jsonResponseValue['payload']['code'])
    print(jsonResponseValue['payload']['message'])
  
  print("\nDelete Contact Details\n")
  print (json.dumps(jsonResponseValue, indent=2))
  print("\n")

  del os.environ['contact_id_github_test']

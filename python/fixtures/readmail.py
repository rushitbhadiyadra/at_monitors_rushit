from env.config import *

def read_mail(username, subject, timeout):

  url = '{readMailURL}'.format(
    readMailURL = os.environ['readMailURL']
  )

  payload = json.dumps({
    "username": str(username),
    "subject": str(subject),
    "timeout": timeout
  })
  
  headers = {
    'Content-Type': 'application/json',
    'Authorization': str(os.environ['authorization'])
  }

  return requests.request("POST", url, headers=headers, data=payload)
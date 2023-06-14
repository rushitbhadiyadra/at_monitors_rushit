from env.config import *

def delay(delayParam=29):

  delay = '{delayURL}{seconds}'.format(
    delayURL = os.environ['delayURL'],
    seconds = delayParam
  )

  payload={}

  response = requests.request("GET", delay, headers=headersDelay, data=payload)

  print('Delay', delayParam, 'Seconds')
  print(response.text)

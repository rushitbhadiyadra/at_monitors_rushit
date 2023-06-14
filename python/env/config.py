import requests
import json
from dotenv import load_dotenv
import os
import time
import xmltodict
from datetime import datetime

load_dotenv('python/env/local.env')
load_dotenv('python/env/global.env')


headers = {
  'X_USERNAME': str(os.environ['headerUsername']),
  'X_PASSWORD': str(os.environ['headerPassword']),
  'X_ACCOUNT_CODE': str(os.environ['headerAccountCode']),
  'Content-Type': 'application/json'
}

headersDelay = {
  'Authorization': str(os.environ['authorization'])
}
from email import header
import json
import os
from urllib import request
import requests
import time
from json import JSONDecodeError
import re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

localEnvJson = open(os.path.join(__location__, '../env/All-Esps-Dev-28299.environment.json'),'r')
localEnvJsonLoad = json.load(localEnvJson)

globalEnvJson = open(os.path.join(__location__, '../env/global.environment.json'),'r')
globalEnvJsonLoad = json.load(globalEnvJson)
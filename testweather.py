from os import closerange
import requests
import time
from datetime import datetime, timedelta
from requests.api import request
import json
from requests.models import Response
c = open('config.txt','r')
config = c.readlines()
url = "https://api.openweathermap.org/data/2.5/onecall?lat="+config[1][0:-1]+"&lon="+config[2][0:-1]+"&exclude=clear&appid="+config[3]
response = requests.request("GET",url)
tempmin=(response.json()["daily"][0]["temp"]["min"])-273.15
tempmax=(response.json()["daily"][0]["temp"]["max"])-273.15
avgtemp = round((tempmin+tempmax)/2,3)
print(avgtemp)
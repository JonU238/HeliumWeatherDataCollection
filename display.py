from os import closerange
import requests
import time
from datetime import datetime, timedelta

from requests.api import request
import json
from requests.models import Response
def reward(n=30):
    min_time = (datetime.now() - timedelta(days=n))
    url = "https://api.helium.io/v1/hotspots/112WCXDccMb9jZ8bNKmdBWKxQ9FAmS8b3iGqBidc1uUq3L1rWqhM/rewards/sum?max_time="+datetime.now().isoformat()+"Z&min_time="+min_time.isoformat()+"Z"
    response = requests.request("GET",url)
    return(response.json())
def wittnesed():
    url = "https://api.helium.io/v1/hotspots/112WCXDccMb9jZ8bNKmdBWKxQ9FAmS8b3iGqBidc1uUq3L1rWqhM/witnessed"
    response = requests.request("GET",url)
    return(response.json())
    

def weather(num):
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=42.291961&lon=-71.329079&exclude=hourly,daily&appid=c1d004a0d2bb3ed438de79e02b00d6c3"
    response = requests.request("GET",url)
    if num==1:
        return response.json()["current"]["temp"]
    elif num==2:
        return "Temp: " + str(round((response.json()["current"]["temp"]-273.15)*(9/5)+32,2)) +"\n"+"Wind speed: "+ str(response.json()["current"]["wind_speed"]) +"\n"+"Wind Gust: "+ str(response.json()["current"]["wind_gust"])
#weather data part
url = "https://api.openweathermap.org/data/2.5/onecall?lat=42.291961&lon=-71.329079&exclude=hourly,daily&appid=c1d004a0d2bb3ed438de79e02b00d6c3"
response = requests.request("GET",url)
f = open('testing.txt','a')
f.write(str(datetime.now())+"&")
f.write(str(round(response.json()["current"]["temp"]-273.15,3))+"&")
f.write(str((response.json()["current"]["weather"]))+"&")
#weather data end
#helium data start
data = wittnesed()
for i in range(1,len(data["data"]),):
    print((data["data"][i]["status"]["timestamp"]))
    if (data["data"][i]["status"]["timestamp"])[0:10]==str(datetime.now().isoformat())[0:10]:
        print("das ist dastag")
        print(str(datetime.now().isoformat())[0:10])
        f.write(str(data["data"][i]["status"]["timestamp"]+"&"))
        f.write(str(data["data"][i]["gain"])+"&")
#end of helium data
f.write("\n")
f.close()
#print(response.json()["current"])




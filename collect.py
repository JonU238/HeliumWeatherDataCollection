from os import closerange
import requests
import time
from datetime import datetime, timedelta
from requests.api import request
import json
from requests.models import Response
c = open('config.txt','r')
config = c.readlines()

#reward takes a int representing the number of days you want to colect over ie. 30==over the last 30days 
def reward(n=30):
    min_time = (datetime.now() - timedelta(days=n))
    url = "https://api.helium.io/v1/hotspots/"+config[0]+"/rewards/sum?max_time="+datetime.now().isoformat()+"Z&min_time="+min_time.isoformat()+"Z"
    response = requests.request("GET",url)
    return(response.json())

#wittnesed returned the responce.json from the helium api witnessed for hotspot
def wittnesed():
    url = "https://api.helium.io/v1/hotspots/"+config[0][0:-1]+"/witnessed"
    response = requests.request("GET",url)
    return(response.json())

#weather returns eather the current weather dict if passed a 1 or a human string if a 2 is passed to it, default is 1
def weather(num=1):
    url = "https://api.openweathermap.org/data/2.5/onecall?lat="+config[1][0:-1]+"&lon="+config[2][0:-1]+"&exclude=hourly,daily&appid="+config[3]
    response = requests.request("GET",url)
    if num==1:
        return response.json()["current"]
    elif num==2:
        return "Temp: " + str(round((response.json()["current"]["temp"]-273.15)*(9/5)+32,2)) +"\n"+"Wind speed: "+ str(response.json()["current"]["wind_speed"]) +"\n"+"Wind Gust: "+ str(response.json()["current"]["wind_gust"])
#weather data part
#collect is the important part
#it writes all the data to the file its really scuffed because the data is parsed by & symbols. Im hoping this may make my life easer when parsing the data but this is defently not the best way to do it.
def collect():
    url = "https://api.openweathermap.org/data/2.5/onecall?lat="+config[1][0:-1]+"&lon="+config[2][0:-1]+"&exclude=clear&appid="+config[3]
    response = requests.request("GET",url)
    f = open('testing.txt','a')
    f.write(str(datetime.now())+"&")
    #average temprature
    tempmin=(response.json()["daily"][0]["temp"]["min"])-273.15
    tempmax=(response.json()["daily"][0]["temp"]["max"])-273.15
    avgtemp = round((tempmin+tempmax)/2,3)
    
    f.write(str(avgtemp)+"&")
    f.write(str((response.json()["current"]["weather"]))+"&")
    #weather data end
    #helium data start
    data = wittnesed()
    for i in range(1,len(data["data"])):
        print((data["data"][i]["status"]["timestamp"]))
        if (data["data"][i]["status"]["timestamp"])[0:10]==str(datetime.now().isoformat())[0:10]:
            f.write(str(data["data"][i]["status"]["timestamp"]+"&"))
            f.write(str(data["data"][i]["gain"])+"&")
    #end of helium data
    f.write("\n")
    f.close()
collect()


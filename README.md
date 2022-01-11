# HeliumWeatherDataColletion

## The Goals:
-  Collect data on the way the weather affects signal propigation on the helium network.
-  Have a way to generate a really cool graph of the data.

## My hypothesis:
I think that the network will preform differently in different weather conditions. To test this this program records data about the weather condition("Temp", "Clear/Fog/Windy/etc.",persipitation)
This data is stored in the testing.txt file in the format
(Timestamp)&(temp)&(weather description)&(timestamp of wittness)&(gain)

## Use
To use the weather collection you need to run the installer.py this just puts the required data into the config.txt
It will ask for your helium hotspot address
from the hotspot address it gets your lat and lng
It will also ask for your api key from https://openweathermap.org/
Everytime you call the collect() it records a data point over the last calendar day(not 24hours(coming soon)) so idealy you would call it once a day at 11:59pm (this will also be changing soon)

## Next steps
After I have collected enough data I will write and publish a script to turn the data into a cool graph to see if there is a coralation.

#! python3
# quickWeather.py - Prints the weather for a location from the command line.
import json, requests, sys

print ('This is the name of the script: ', sys.argv[0])
print ('Number of arguments: ', len(sys.argv))
print ('The arguments are: ' , str(sys.argv))
location = ' '.join(sys.argv[1:])
print (location)


# Compute location from command line arguments.
if len(sys.argv) < 2:
 print('Usage: quickWeather.py location')
 sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.

url ='http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=0432b0950f9276e38a52f8e1efc7f614' % (location)
print(url)
response = requests.get(url)
response.raise_for_status()


# Load JSON data into a Python variable.

wData = json.loads(response.text)
print (wData)

print ()
print ("Clima actual en %s:" %location)
print (wData['weather'][0]['main'])
print (wData['weather'][0]['description'])
print()
print("Temperaturas")
print ("Actual, ",wData['main']['temp']-273)
print ("Máxima, ",wData['main']['temp_max']-273)
print ("Mínima, ",wData['main']['temp_min']-273)
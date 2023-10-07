#!/usr/bin/python3

import requests
import json

stationID = "YOUR_STATION_ID"
tempestToken ="YOUR_TEMPEST_TOKEN"

file = open("forecast.txt", "w")

tempestURL = "https://swd.weatherflow.com/swd/rest/better_forecast?station_id={}&units_temp=f&units_wind=mph&units_pressure=inhg&units_precip=in&units_distance=mi&token={}".format(stationID, tempestToken)

r = requests.get(tempestURL)
r_data = r.json()

highTemp = r_data['forecast']['daily'][0]['air_temp_high']
precipProb = r_data['forecast']['daily'][0]['precip_probability']

output = "Hello Anywhere High School.  Today's high temperature is going to be {} degrees.\n  There will be a {} percent chance of precipitation".format(highTemp, precipProb)

file.write(output)
file.close()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

def getWeather(key, cityCode):
    url = "https://restapi.amap.com/v3/weather/weatherInfo?key={}&extensions=all&city={}".format(key, cityCode)
    response = json.loads(requests.get(url=url).text)
    cityName = response["forecasts"][0]["province"]
    if response["forecasts"][0]["casts"][0]["dayweather"] == response["forecasts"][0]["casts"][0]["nightweather"]:
      cityWeather = response["forecasts"][0]["casts"][0]["dayweather"]
    else:
      cityWeather = "{}转{}".format(response["forecasts"][0]["casts"][0]["dayweather"], response["forecasts"][0]["casts"][0]["nightweather"])
    cityTemperature = "{}～{}".format(response["forecasts"][0]["casts"][0]["nighttemp"], response["forecasts"][0]["casts"][0]["daytemp"])
    return "{} {} {}°C".format(cityName, cityWeather, cityTemperature)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import yaml
from datetime import datetime


def get_now_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def config():
    params = yaml.load(open(os.path.join("config.yml"), 'r', encoding='utf-8').read(), Loader=yaml.SafeLoader)
    return params

def get_robot_webhook():
    if os.environ.get('ROBOT_WEB_HOOK') is None:
        RobotWebHook = config()["RobotInfoList"]["RobotWebHook"]
    else:
        RobotWebHook = os.environ.get('ROBOT_WEB_HOOK')
    return RobotWebHook

def get_robot_sign():
    if os.environ.get('ROBOT_SIGN') is None:
        RobotSign = config()["RobotInfoList"]["RobotSign"]
    else:
        RobotSign = os.environ.get('ROBOT_SIGN')
    return RobotSign

def get_amap_key():
    if os.environ.get('AMAP_KEY') is None:
        AmapKey = config()["Weather"]["GaodeKEY"]
    else:
        AmapKey = os.environ.get('AMAP_KEY')
    return AmapKey

def get_city_code():
    if os.environ.get('CITY_CODE') is None:
        CityCode = config()["Weather"]["CityCode"]
    else:
        CityCode = os.environ.get('CITY_CODE')
    return CityCode

def get_juhe_key():
    if os.environ.get('JUHE_KEY') is None:
        JuheKey = config()["Holiday"]["JuheKey"]
    else:
        JuheKey = os.environ.get('JUHE_KEY')
    return JuheKey

def get_robot_info_list():
    if os.environ.get('ROBOT_INFO_LIST') is None:
        RobotInfoList = config()['RobotInfoList']
    else:
        RobotInfoList = os.environ.get('ROBOT_INFO_LIST')
    return RobotInfoList
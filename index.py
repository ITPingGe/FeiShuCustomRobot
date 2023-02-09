# -*- coding: utf8 -*-
import os.path
import yaml
import requests
import time
import hashlib
import base64
import hmac
# import curlify

import HolidayCountdown
import GetWeather
import settings

from GetGuShiCi import GetGushici


def gen_sign(timestamp, secret):
    # 拼接timestamp和secret
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    hmac_code = hmac.new(string_to_sign.encode("utf-8"), digestmod=hashlib.sha256).digest()

    # 对结果进行base64处理
    sign = base64.b64encode(hmac_code).decode('utf-8')

    return sign

def RunGushici(RobotWebHook, RobotSign):
    GetGuShiCi = GetGushici()
    GetGuShiCi.GetObjectIdList()
    GetGuShiCi.GetBody()
    timestamp = int(time.time())
    sign = gen_sign(timestamp, RobotSign)

    header = {"Content-Type": "application/json"}
    req_url = RobotWebHook
    req_data = {"timestamp": str(timestamp),
                "sign": str(sign),
                "msg_type": "interactive",
                "card": {
                    "config": {
                        "wide_screen_mode": True
                    },
                    "header": {
                        "title": {
                            "content": "%s" % GetGuShiCi.GetTitle(),
                            "tag": "plain_text"
                        }
                    },
                    "i18n_elements": {
                        "zh_cn": [{
                                "fields": [{
                                    "is_short": True,
                                    "text": {
                                        "content": "**[%s]%s**" % (GetGuShiCi.GetDynasty(), GetGuShiCi.GetAuthorName()),
                                        "tag": "lark_md"
                                    }
                                }],
                                "tag": "div"
                            },
                            {
                                "tag": "markdown",
                                "content": "\n%s" % GetGuShiCi.GetContent()
                            },
                            {
                                "tag": "markdown",
                                "content": "\n**译文：**\n%s" % GetGuShiCi.GetTranslation()
                            },
                            {
                                "tag": "markdown",
                                "content": "\n**倒计时：**\n{}\n{}".format(HolidayCountdown.NextRestCountdown(settings.get_now_time()), HolidayCountdown.HolidayDesc(settings.get_juhe_key()))
                            },
                            {
                                "tag": "hr"
                            },
                            {
                                "tag": "note",
                                "elements": [{
                                    "tag": "plain_text",
                                    "content": "每日诗词鉴赏温馨提示：{}".format(GetWeather.getWeather(settings.get_amap_key(), settings.get_city_code()))
                                }]
                            }
                        ]
                    }
                }
            }
    response = requests.post(url=req_url, json=req_data, headers=header, verify=False)
    # print(curlify.to_curl(response.request))
    return response

def SendAll(event=None, context=None):
    for robotInfo in settings.get_robot_info_list():
        robotWebHook = robotInfo["RobotWebHook"]
        robotSign = robotInfo["RobotSign"]
        RunGushici(robotWebHook, robotSign)

if __name__ == "__main__":
    SendAll(event=None, context=None)
    # RunGushici('webhook', 'sign')   # 失败手动补偿
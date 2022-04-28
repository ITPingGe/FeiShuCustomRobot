# -*- coding: utf8 -*-
import json
import requests
import time
import hashlib
import base64
import hmac

import HolidayCountdown
import GetWeather

from GetGuShiCi import GetGushici

SIGN = "XXXXXXXXXXXXXXXXX"
WEBHOOK = "https://open.feishu.cn/open-apis/bot/v2/hook/XXXXXXXXXXXXXXXXXXX"
cityCode = 110108   # 城市编码，在https://lbs.amap.com/api/webservice/download查询

def gen_sign(timestamp, secret):
    # 拼接timestamp和secret
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    hmac_code = hmac.new(string_to_sign.encode("utf-8"), digestmod=hashlib.sha256).digest()

    # 对结果进行base64处理
    sign = base64.b64encode(hmac_code).decode('utf-8')

    return sign

def RunGushici(event, context):
    GetGuShiCi = GetGushici()
    GetGuShiCi.GetObjectIdList()
    GetGuShiCi.GetBody()
    timestamp = int(time.time())
    sign = gen_sign(timestamp, SIGN)

    header = {"Content-Type": "application/json"}
    req_url = WEBHOOK
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
                                "content": "\n**假期倒计时：**\n{}\n{}".format(HolidayCountdown.NextRestCountdown(), HolidayCountdown.HolidayDesc())
                            },
                            {
                                "tag": "hr"
                            },
                            {
                                "tag": "note",
                                "elements": [{
                                    "tag": "plain_text",
                                    "content": "每日诗词鉴赏温馨提示：{}".format(GetWeather.getWeather(cityCode))
                                }]
                            }
                        ]
                    }
                }
                }
    requests.post(url=req_url, json=req_data, headers=header, verify=False)
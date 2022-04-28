#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import requests
import json
from datetime import datetime

calendar_error_code = {
    "217702": "参数格式错误",
    "10001": "错误的请求KEY",
    "10002": "该KEY无请求权限",
    "10003": "KEY过期",
    "10004": "错误的OPENID",
    "10005": "应用未审核超时，请提交认证",
    "10007": "未知的请求源",
    "10008": "被禁止的IP",
    "10009": "被禁止的KEY",
    "10011": "当前IP请求超过限制",
    "10012": "请求超过次数限制",
    "10013": "测试KEY超过请求限制",
    "10014": "系统内部异常(调用充值类业务时，请务必联系客服或通过订单查询接口检测订单，避免造成损失)",
    "10020": "接口维护",
    "10021": "接口停用"
}

def TimestampConversion(time_sj):   # 将标准时间转换为时间戳
    data_sj = time.strptime(time_sj,"%Y-%m-%d %H:%M:%S")       #定义格式
    time_int = int(time.mktime(data_sj))
    return time_int

# def DayCountdown(day): # 获取距离指定日期还有多少天，day传入示例：2022-03-18
#     DayTime = TimestampConversion("{}-{} 00:00:00".format(datetime.now().year, day))
#     return (DayTime - int(time.time())) //86400 + 1

"""获取距离指定日期还有多少天，day为时间戳"""
def dayCountdown(day):
    return (day - int(time.time())) // 86400 + 1

"""
获取距离目标日期还有多少天
接口文档：http://timor.tech/api/holiday
"""
def GetNextHolidayCountdown():  # 放假倒计时
    response = json.loads(requests.get('http://timor.tech/api/holiday/next/$data?type=Y&week=Y').text)
    return "距离放假还有{}天；".format(response["holiday"]["rest"])

def GetNextWorkdayCountdown():  # 上班倒计时
    response = json.loads(requests.get('http://timor.tech/api/holiday/workday/next/$date').text)
    return "距离上班还有{}天；".format(response["workday"]["rest"])

def NextRestCountdown():        # 先判断今天是否上班，再确定使用什么文案
    response = json.loads(requests.get('http://timor.tech/api/holiday/info/$date').text)
    if response['code'] == 0:
        if response['type']['type'] == 0 or response['type']['type'] == 3:
            nextRest = GetNextHolidayCountdown()
        else:
            nextRest = GetNextWorkdayCountdown()
    elif response['code'] == -1:
        nextRest = "服务出错"
    else:
        nextRest = "未知错误"
    return nextRest

"""
获取某一年的节假日时间
查看下方API文档获取并替换key
接口文档：https://www.juhe.cn/docs/api/id/177
"""
def FestivalTime(year):
    url = "http://v.juhe.cn/calendar/year"
    params = (
        ('year', year),
        ('key', 'XXXXXXXXXXXXXXXX'),
    )
    return requests.get(url, params=params).text

# def WeekendCountdown():
#     dayOfWeek = datetime.now().isoweekday() ###返回数字1-7代表周一到周日
#     return "距离周六还有{}天；".format(6 - dayOfWeek)

def Desc(year):
    desc = ""
    response = json.loads(FestivalTime(year))
    if response["error_code"] == 0:
        for festival_info in response["result"]["data"]["holiday_list"]:
            festival_time = int(TimestampConversion("{} 00:00:00".format(festival_info["startday"])))
            festival_name = festival_info["name"]
            if festival_time > int(time.time()):
                desc += "距离{}还有{}天；\n".format(festival_name,dayCountdown(festival_time))
    elif response["error_code"] == 217701:
        desc = "{}年的节假日已经过完了，祝愿你在这一年剩余的日子里每天都开心(^_^)".format(datetime.now().year)
    elif str(response["error_code"]) in calendar_error_code.keys():
        desc = calendar_error_code[str(response["error_code"])]
    else:
        desc = "未知错误"
    return desc

# 当今年的节假日过完时，获取下一年的节假日
def HolidayDesc():
    if Desc(datetime.now().year) == "":
        holidayDesc = Desc(datetime.now().year + 1)
    else:
        holidayDesc = Desc(datetime.now().year)
    return holidayDesc

# 调试代码
# if __name__ == "__main__":
#     print(HolidayDesc(), GetNextHolidayCountdown())
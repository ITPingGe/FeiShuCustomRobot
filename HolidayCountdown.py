#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from datetime import datetime

NewYearsDay = "01-01"               # 元旦
SpringFestival = "01-31"            # 春节
TombSweepingDay = "04-03"           # 清明节假期开始时间
MayDay = "04-30"                    # 五一假期
TheDragonBoatFestival = "06-03"     # 端午节
TheMidAutumnFestival = "09-10"      # 中秋节
NationalDay = "10-01"               # 国庆节

def TimestampConversion(time_sj):   # 将标准时间转换为时间戳
    data_sj = time.strptime(time_sj,"%Y-%m-%d %H:%M:%S")       #定义格式
    time_int = int(time.mktime(data_sj))
    return time_int

def WeekendCountdown():
    dayOfWeek = datetime.now().isoweekday() ###返回数字1-7代表周一到周日
    return "距离周六还有{}天；".format(5 - dayOfWeek)

def DayCountdown(day): # 获取距离指定日期还有多少天
    DayTime = TimestampConversion("{}-{} 00:00:00".format(datetime.now().year, day))
    return (DayTime - int(time.time())) //86400

def Countdown():
    CountdownList = []
    if DayCountdown(NewYearsDay) > 0:
        CountdownList.append("距离春节还有{}天；".format(DayCountdown(NewYearsDay)))

    if DayCountdown(SpringFestival) > 0:
        CountdownList.append("距离春节还有{}天；".format(DayCountdown(SpringFestival)))

    if DayCountdown(TombSweepingDay) >0:
        CountdownList.append("距离清明节还有{}天；".format(DayCountdown(TombSweepingDay)))

    if DayCountdown(MayDay) > 0:
        CountdownList.append("距离五一还有{}天；".format(DayCountdown(MayDay)))
    if DayCountdown(TheDragonBoatFestival) > 0:
        CountdownList.append("距离端午节还有{}天；".format(DayCountdown(TheDragonBoatFestival)))

    if DayCountdown(TheMidAutumnFestival) > 0:
        CountdownList.append("距离中秋节还有{}天；".format(DayCountdown(TheMidAutumnFestival)))

    if DayCountdown(NationalDay) > 0:
        CountdownList.append("距离国庆节还有{}天。".format(DayCountdown(NationalDay)))
    return CountdownList

# if __name__ == "__main__":
#     print(WeekendCountdown(), Countdown())
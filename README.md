# 飞书自定义机器人

####机器人介绍：每天推荐一首古诗词

####开发语言：Python3

##使用教程

**准备工具：飞书、腾讯云函数**

1、飞书自定义机器人使用教程：https://open.feishu.cn/document/ukTMukTMukTM/ucTM5YjL3ETO24yNxkjN

2、腾讯云函数：https://serverless.cloud.tencent.com/start?c=scf

**操作步骤：**

1、在飞书群聊中添加一个自定义机器人，将机器人**安全校验**设置为**签名校验**。

2、在下方提到的文件中搜索对应的字段并进行修改

**index.py**

```angular2html
webhook：
    WEBHOOK = "https://open.feishu.cn/open-apis/bot/v2/hook/6*******-****-****-****-***********6"
签名：
    SIGN = "q2*****************4g"
城市编码：
    cityCode = 110108
```
**GetWeather.py**

```angular2html
高德应用Key:
    url = "https://restapi.amap.com/v3/weather/weatherInfo?key=XXXXXXXXXXXXXXXXXXXXXX&extensions=all&city={}".format(cityCode)
```

**HolidatCountdown.py**

```angular2html
节假日接口应用key：
    'key', 'XXXXXXXXXXXXXXXX'
```

3、在腾讯云函数创建一个Python3版本的HelloWord空白模版函数，然后将修改后的代码部署在上边，最后根据个人喜好设置定时触发即可,建议将函数超时时间设置为30s。

**飞书机器人发送卡片消息样式可根据个人喜好自行定制，详情可参考：https://open.feishu.cn/document/ukTMukTMukTM/uczM3QjL3MzN04yNzcDN**
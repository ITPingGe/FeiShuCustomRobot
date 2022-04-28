# -*- coding: utf-8 -*-
import requests
import json
import random
import time

class GetGushici:

    def __init__(self):
        """请求所用到的header"""
        self.headers = {
            'authority': 'avoscloud.com',
            'x-lc-ua': 'LeanCloud-JS-SDK/3.15.0 (Browser)',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
            'content-type': 'application/json;charset=UTF-8',
            'x-lc-sign': '826f2e0504a2809a3ecc382de04c0f1c,1639200943599',
            'x-lc-id': '9pq709je4y36ubi10xphdpovula77enqrz27idozgry7x644',
            'x-lc-prod': '1',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'accept': '*/*',
            'origin': 'http://m.xichuangzhu.com',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'http://m.xichuangzhu.com/',
            'accept-language': 'en-VI,en;q=0.9,ar-AE;q=0.8,ar;q=0.7,zh-CN;q=0.6,zh;q=0.5,fa-AF;q=0.4,fa;q=0.3,en-US;q=0.2',
        }
        self.objectIdList = []                   # 用于存储诗单ID的空列表
        self.place = int
        self.body = {}
        self.ShowOrder = str
        self.KindCN = str
        self.Dynasty = str
        self.AuthorName = str
        self.Title = str
        self.Content = str
        self.Annotation = str
        self.Translation = str
        self.Intro = str
        self.MasterComment = str

    def GetObjectIdList(self):
        data = '{"page":%d,"perPage":100}' %random.randint(0,9)
        response = requests.post('https://avoscloud.com/1.1/call/getSelectedLists', headers=self.headers, data=data)
        josn1 = json.loads(response.text)
        if len(josn1["result"]) > 0:
            for x in range(0, len(josn1["result"])):
                objectId = josn1["result"][x]["objectId"]
                self.objectIdList.append(objectId)
        return self.objectIdList

    def GetBody(self):
        while True:
            data1 = '{"listId":"%s","page":%d,"perPage":100}' %(self.objectIdList[random.randint(0, len(self.objectIdList)-1)], random.randint(0,9))
            response = requests.post('https://avoscloud.com/1.1/call/getListWorks', headers=self.headers, data=data1)
            self.body = json.loads(response.text)
            if len(self.body["result"]) > 0:
                self.place = random.randint(0, len(self.body["result"])-1)
                return self.place, self.body
            else:
                continue

    def GetShowOrder(self):    # 诗词ID
        self.ShowOrder = self.body["result"][self.place]["showOrder"]
        return self.ShowOrder

    def GetKindCN(self):       # 类型：诗或者词或曲
        self.KindCN = self.body["result"][self.place]["work"]["kindCN"]
        return self.KindCN

    def GetDynasty(self):      # 朝代
        self.Dynasty = self.body["result"][self.place]["work"]["dynasty"]
        return self.Dynasty

    def GetAuthorName(self):   # 作者
        self.AuthorName = self.body["result"][self.place]["work"]["authorName"]
        return self.AuthorName

    def GetTitle(self):        # 诗的标题
        self.Title = str(self.body["result"][self.place]["work"]["title"])
        return self.Title

    def GetContent(self):      # 诗的正文
        self.Content = str(self.body["result"][self.place]["work"]["content"])
        return self.Content

    def GetAnnotation(self):   # 注释
        self.Annotation = str(self.body["result"][self.place]["work"]["annotation"])
        return self.Annotation

    def GetTranslation(self):  # 译文
        Translation = str(self.body["result"][self.place]["work"]["translation"])
        if Translation.strip() != "":
            self.Translation = Translation
        else:
            self.Translation = "无"
        return self.Translation

    def GetIntro(self):        # 评析
        self.Intro = str(self.body["result"][self.place]["work"]["intro"])
        return self.Intro

    def GetMasterComment(self):# 辑评
        self.MasterComment = str(self.body["result"][self.place]["work"]["masterComment"])
        return self.MasterComment
#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-20 and 12:35
FileName:20190920_07_接口获取天气预报.py
Description：...
第七题
访问天气预报接口http://www.weather.com.cn/data/sk/101190408.html
返回城市名和温度，对应的字段分别是city和temp
要求使用requests模块，返回信息不能是乱码
'''

# 导入接口测试专用库
import requests
# 导入编码检查专用库
import chardet

# 获取接口地址
weatherUrl = r"http://www.weather.com.cn/data/sk/101190408.html"
response = requests.get(url=weatherUrl)
res = response.text
response = response.json()

# 直接转码要出现乱码，可以转码到非unicode，再转回来即刻显示中文
city = response['weatherinfo']['city'].encode('raw_unicode_escape').decode("utf-8")
temp = response['weatherinfo']['temp']
print(f"当前返回：{res.encode('raw_unicode_escape').decode('utf-8')}")
print(f"编码格式：{chardet.detect(res.encode('utf-8'))}")
print(f"当前城市：{city}，当前温度：{temp}")

# -- 结果：
# 当前返回：{"weatherinfo":{"city":"太仓","cityid":"101190408","temp":"22.8","WD":"东风","WS":"小于3级","SD":"81%","AP":"1005.5hPa","njd":"暂无实况","WSE":"<3","time":"17:55","sm":"3.2","isRadar":"0","Radar":""}}
# 编码格式：{'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
# 当前城市：太仓，当前温度：22.8

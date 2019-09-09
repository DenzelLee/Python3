#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:lihao
Date&Time:2019-07-19 and 23:15
FileName:
'''
'''
请到如下网址下载最新Chrome浏览器 的 web driver 驱动
https://chromedriver.storage.googleapis.com/index.html

pip 安装Selenium Web driver Python 客户端库
1. 访问天气查询网站（网址如下），查询江苏省天气 
http://www.weather.com.cn/html/province/jiangsu.shtml

2. 获取江苏所有城市的天气，并找出其中每天最低气温最低的城市，显示出来，比如 
温度最低为12℃, 城市有连云港 盐城 
'''
from selenium import webdriver
import time
driver = webdriver.Chrome(r"D:\TestFiles\Python3\chromedriver.exe")
driver.get("http://www.weather.com.cn/html/province/jiangsu.shtml")
strList = driver.find_element_by_id("forecastID")
# print(strList.text)
dls = strList.find_elements_by_tag_name("dl")
count = 0
weather = 0
cityList = []
cityDic = {}
for dl in dls:
    name = dl.find_element_by_tag_name("dt").text
    w1 = dl.find_element_by_tag_name("span").text
    w2 = dl.find_element_by_tag_name("b").text
    w1 = str(w1).replace("℃","")
    w2 = str(w2).replace("℃", "")
    count +=1
    res ="序号：{},名称：{}，温度：{}，温度：{}".format(count, name, w1, w2)
    # print(res)
    if weather == 0 or int(min(int(w1),int(w2)))<int(weather):
        weather = min(w1, w2)
    # print("序号：{},名称：{}，最低温度：{}".format(count, name, weather))
    elif min(w1,w2) == weather:
        cityList.append(name)
print("名称：{}，最低温度：{}".format(cityList, weather))


driver.quit()






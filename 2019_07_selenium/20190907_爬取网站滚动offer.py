#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-07 and 10:38
FileName:20190907_爬取网站滚动offer.py
Description：...
'''
import time, datetime

# 获取当前格式化-年月日：时分秒
nowTimee = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://vip.ytesting.com/loginController.do?login")
driver.find_element_by_id("userName").send_keys("K201906125518")
driver.find_element_by_id("password").send_keys("270981551")
driver.maximize_window()
input("...")
print("---- 登录成功 ----")
driver.switch_to.frame("iframe0")
time.sleep(3)
offers = driver.find_elements_by_css_selector(".col-sm-12 .flot-chart #marqueediv5>p")
print(f"---- 定位成功 ----{offers}")
for i in offers:
    print(i.text)
    # print("---- 打印成功 ----")

#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-04 and 12:09
FileName:2019080_xpath多多计算器.py
Description：...
1 找到一个安卓设备（没有可以向朋友借用一下），将其连接到电脑上，根据课堂视频指导，确保可以被命令 adb devices -l 检测到
2 安装多多计算器（怎么装？自己想办法）
3 练习用 Appium Desktop中的 inspector查看界面。
4 将上次作业，用xpath方式定位元素，再实现一遍
'''
from appium import webdriver
import time,traceback

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5',
    'deviceName': '127.0.0.1:62001',
    # 'app': r'd:\apk\toutiao.apk',
    'appPackage': 'com.ibox.calculators',
    'appActivity': 'com.ibox.calculators.SplashActivity',
    'unicodeKeyboard': True,
    'resetKeyboard':True,
    'noReset': True, # 初始化，True为了避免每次打开APP都提问你是否获取权限
    'newCommandTimeout': 6000,
    'automationName':'uiautomator2'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(15)

# 定义定位函数
def calcc(d):
    driver.find_element_by_xpath(d).click()
    print(driver.find_element_by_xpath(d).text)

# 1+100=101
calcc("//*[@resource-id='com.ibox.calculators:id/digit1']")
calcc("//*[@resource-id='com.ibox.calculators:id/plus']")
calcc("//*[@resource-id='com.ibox.calculators:id/digit1']")
calcc("//*[@resource-id='com.ibox.calculators:id/digit0']")
calcc("//*[@resource-id='com.ibox.calculators:id/digit0']")

# 通过坐标点击“=”
driver.tap([(805, 1483), (1040, 1778)], 100)

# 101*100=10100
calcc("//*[@resource-id='com.ibox.calculators:id/mul']")
calcc("//*[@resource-id='com.ibox.calculators:id/digit1']")
calcc("//*[@resource-id='com.ibox.calculators:id/digit0']")
calcc("//*[@resource-id='com.ibox.calculators:id/digit0']")

# 10100/2=5050
calcc("//*[@resource-id='com.ibox.calculators:id/div']")
calcc("//*[@resource-id='com.ibox.calculators:id/digit2']")
driver.tap([(805, 1483), (1040, 1778)], 100)


result = driver.find_elements_by_xpath("//*[@resource-id='com.ibox.calculators:id/cv']/android.widget.TextView")[1]
print(result.text)
if result.text == "5050":
    print("pass!")
else:
    print("fail!")
driver.quit()

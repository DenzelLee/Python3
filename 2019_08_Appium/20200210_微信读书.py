#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2020/2/9 and 13:56
Project:Python3
FileName:20200210_微信读书
Description：...
1.失败案例，无法连接小米手机
'''

from appium import webdriver
import time
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '8.0',
    'deviceName': 'test',
    'app': r'D:\Myprogram\Appium\apk\weixindushu_10141765.apk',
    'appPackage': 'com.tencent.weread',
    'appActivity': 'com.tencent.weread.LauncherActivity',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True,
    'newCommandTimeout': 6000,
    'automationName':'uiautomator2'
}
driver = webdriver.Remote(r'http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
time.sleep(3)
# sq = driver.find_element_by_accessibility_id("songqin recommend")
# sqLocation = sq.location['y']
# size = driver.get_window_size()
# print(size)
# startX = size['width']*0.5
# endX = size['width']*0.5
# startY = size['height']*0.8
# endY = size['height']*0.5
# print(f"{startX}{endX}{startY}{endY}")
# count = 0
# while True:
#     count +=1
#     driver.swipe(startX,startY,endX,endY,800)
#     time.sleep(1.5)
#     # print()
#     bests = driver.find_elements_by_xpath("//*[@content-desc='best reputation']")
#     if bests:
#         print(f"第{count}次移动，目标已出现")
#         break
#     else:
#         print(f"第{count}次移动，目标还未出现")
# time.sleep(1.5)
# bestList = driver.find_elements_by_xpath("//android.widget.ScrollView//android.widget.ImageView/following-sibling::android.widget.TextView[1] | //*[@content-desc='best reputation']")
# driver.swipe(startX, bests[0].location['y'], endX, sqLocation+100, 3000)
# for i in bestList:
#     print(i.text)
#
#
# input("...")
# driver.quit()


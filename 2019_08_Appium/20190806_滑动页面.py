#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-06 and 13:20
FileName:20190806_滑动页面.py
Description：...
'''
from appium import webdriver
import time
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5',
    'deviceName': '127.0.0.1:62001',
    # 'app': r'D:\TestFiles\Appium\Apk\sqauto.apk',
    'appPackage': 'com.sqauto',
    'appActivity': 'com.sqauto.MainActivity',
    'unicodeKeyboard': True,
    'resetKeyboard':True,
    'noReset': True, # 初始化，True为了避免每次打开APP都提问你是否获取权限
    'newCommandTimeout': 6000,
    'automationName':'uiautomator2'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
time.sleep(3)
sq = driver.find_element_by_accessibility_id("songqin recommend")
sqLocation = sq.location['y']
size = driver.get_window_size()
print(size)
startX = size['width']*0.5
endX = size['width']*0.5
startY = size['height']*0.8
endY = size['height']*0.5
print(f"{startX}{endX}{startY}{endY}")
count = 0
while True:
    count +=1
    driver.swipe(startX,startY,endX,endY,800)
    time.sleep(1.5)
    # print()
    bests = driver.find_elements_by_xpath("//*[@content-desc='best reputation']")
    if bests:
        print(f"第{count}次移动，目标已出现")
        break
    else:
        print(f"第{count}次移动，目标还未出现")
time.sleep(1.5)
bestList = driver.find_elements_by_xpath("//android.widget.ScrollView//android.widget.ImageView/following-sibling::android.widget.TextView[1] | //*[@content-desc='best reputation']")
driver.swipe(startX, bests[0].location['y'], endX, sqLocation+100, 3000)
for i in bestList:
    print(i.text)


input("...")

driver.quit()



# from appium import webdriver
# import time
#
#
# desired_caps = {
#     'platformName': 'Android',
#     'platformVersion': '8',
#     'deviceName': 'xxx',
#     'appPackage': 'com.sqauto',
#     'appActivity': 'com.sqauto.MainActivity',
#     'noReset': True,
#     'newCommandTimeout': 6000,
# }
#
#
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC
# driver.implicitly_wait(10)
#
# target = driver.find_element_by_accessibility_id('songqin recommend')
# targetY = target.location['y']
#
# ele = driver.find_element_by_accessibility_id('cramp fast')
# yPos = ele.location['y']
# xPos = ele.location['x']
#
# driver.implicitly_wait(0)
# while True:
#     driver.swipe(xPos, yPos, xPos, yPos - 300, 800)
#     eles = driver.find_elements_by_accessibility_id('best reputation')
#
#     # 口碑最佳 还没出现
#     if not eles:
#         continue
#
#     # 口碑最佳出现了,将当前位置移到 目标位置
#     driver.swipe(xPos, eles[0].location['y'], xPos, targetY, 5000)
#     break
#
# driver.implicitly_wait(10)
#
#
#
# xpath = "//android.widget.ScrollView//android.widget.ImageView/following-sibling::android.widget.TextView[1] | //*[@content-desc='best reputation']"
#
# eles = driver.find_elements_by_xpath(xpath)
# for ele in eles:
#     print(ele.text)
#
#
# eleTexts = [ele.text for ele in eles]
# start = eleTexts.index('口碑最佳')
# print('\n\n口碑最佳应用为：\n' + '\n'.join(eleTexts[start+1:start+1+5]))

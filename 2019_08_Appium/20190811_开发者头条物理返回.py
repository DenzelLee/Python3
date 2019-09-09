#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-11 and 11:51
FileName:20190811_开发者头条物理返回.py
Description：...
1 安装开发者头条应用
2 打开该应用，在阅读标签页中，点击 精选文章的第一篇，验证确实能打开同名文章
3 按返回键， 验证能够正确返回 阅读标签页
'''

from selenium import webdriver
from time import sleep

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5',
    'deviceName': '127.0.0.1:62001',
    # 'app': r'D:\TestFiles\Appium\Apk\sqauto.apk',
    'appPackage': 'io.manong.developerdaily',
    'appActivity': 'io.toutiao.android.ui.activity.LaunchActivity',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True,
    'newCommandTimeout': 6000,
    'automationName': 'uiautomator2'

}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(20)


driver.find_element_by_xpath("//*[@text='订阅']").click()
sleep(5)
# print(f"当前订阅页面标题：{driver.title}")
sleep(5)

driver.find_element_by_xpath("//*[@text='精选']").click()
sleep(5)
# print(f"当前精选标题：{driver.title}")
sleep(5)

eles = driver.find_elements_by_xpath('//android.widget.RelativeLayout/android.widget.TextView[@ resource-id="io.manong.developerdaily:id/tv_title"]')
eTitle = eles[0].text
print(eTitle)
eles[0].click()
sleep(1)
# print(f"当前文章页面标题：{driver.title}")

cTitle = driver.find_element_by_xpath("//*[@resource-id='io.manong.developerdaily:id/tv_title']")
sleep(5)
print(cTitle.text)
if cTitle.text == eTitle:
    print("pass!")
else:
    print("fail!")
sleep(1)
driver.find_element_by_xpath("//*[@resource-id='io.manong.developerdaily:id/toolbar']/android.widget.ImageButton").click()
sleep(5)
eles2 = driver.find_elements_by_xpath\
    ("//android.widget.RelativeLayout/android.widget.LinearLayout[@resource-id='io.manong.developerdaily:id/ll_tap']/android.widget.TextView[@resource-id='io.manong.developerdaily:id/tv_tab_title']")
sleep(5)
for j in eles2:
    print(j.text)
sleep(5)

# 打开通知栏
# driver.open_notifications()
# sleep(5)

# 物理返回键
# driver.press_keycode(4)
sleep(1)
input("...")
driver.quit()


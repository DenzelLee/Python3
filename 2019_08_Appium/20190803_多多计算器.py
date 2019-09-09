#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-03 and 14:00
FileName:20190803_多多计算器.py
Description：------

1 到如下网址下载 多多计算器
http://android.myapp.com/myapp/detail.htm?apkName=com.ibox.calculators&ADTAG=mobile
2 用 aapt.exe 命令查看 apk包的 appPackage 信息和 主 Activity 信息
3 用 UIAutomator Viewer 查看应用界面元素信息
4 编写python程序，完成一个 计算 3+9 ，结果 再乘以5 的自动化功能. 最后判断计算结果是否为60，如果是，测试通过；否则测试不通过

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
driver.implicitly_wait(10)
time.sleep(8)
try:
    # 123456789
    ele0 = driver.find_element_by_id("com.ibox.calculators:id/digit0")
    ele1 = driver.find_element_by_id("com.ibox.calculators:id/digit1")
    ele2 = driver.find_element_by_id("com.ibox.calculators:id/digit2")
    ele3 = driver.find_element_by_id("com.ibox.calculators:id/digit3")
    ele4 = driver.find_element_by_id("com.ibox.calculators:id/digit4")
    ele5 = driver.find_element_by_id("com.ibox.calculators:id/digit5")
    ele6 = driver.find_element_by_id("com.ibox.calculators:id/digit6")
    ele7 = driver.find_element_by_id("com.ibox.calculators:id/digit7")
    ele8 = driver.find_element_by_id("com.ibox.calculators:id/digit8")
    ele9 = driver.find_element_by_id("com.ibox.calculators:id/digit9")
    # +
    eleadd = driver.find_element_by_id("com.ibox.calculators:id/plus")
    # *
    eleMultiply = driver.find_element_by_id("com.ibox.calculators:id/mul")
    # /
    elediv = driver.find_element_by_id("com.ibox.calculators:id/div")
    # =
    eleqeual = driver.find_element_by_id("com.ibox.calculators:id/equal")

    # print(f"{ele3.text},{ele9.text},{ele5.text}")
    # 1+100
    ele1.click()
    time.sleep(1)
    eleadd.click()
    ele1.click()
    ele0.click()
    ele0.click()
    eleqeual.click()
    # *100
    eleMultiply.click()
    ele1.click()
    ele0.click()
    ele0.click()
    # /2
    elediv.click()
    ele2.click()
    # =
    eleqeual.click()
    time.sleep(2)

    # result checkout
    elesultfather = driver.find_element_by_id("com.ibox.calculators:id/cv")
    elesultson =elesultfather.find_elements_by_class_name("android.widget.TextView")

    eleStr = elesultson[1].text
    print(eleStr)
    if eleStr == "5050":
        print('Pass!')
    else:
        print('False!')

except Exception as e:
    print(f"ErrorInfo:{e}")
input(...)
driver.quit()



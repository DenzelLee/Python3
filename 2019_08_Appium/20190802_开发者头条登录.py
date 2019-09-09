#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-02 and 21:04
FileName:20190802_开发者头条_夜神模拟器.py
Description：...
'''
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,traceback

desired_caps = {}
desired_caps['platformName'] = "Android"         # 声明是ios还是Android系统
desired_caps['platformVersion'] = '5'        # Android内核版本号，可以在夜神模拟器设置中查看
desired_caps['deviceName'] = '127.0.0.1:62001'   # 连接的设备名称
# desired_caps['appPackage'] = r'D:\TestFiles\Appium\Apk\toutiao.apk'    # apk的包名
desired_caps['appPackage'] = 'io.manong.developerdaily'
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'  # apk的launcherActivity

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)          # 建立 session

# 下面的操作是自动化一个用户登录的过程，大家课后自己尝试的时候，需要先注册用户
# 怎么注册演示给大家看看， 怎么登录也演示给大家看看，
# 最后别忘了要退出登录，一遍自动化可以执行
try:
    # 和Selenium含义一样，问问大家还记得吗？
    driver.implicitly_wait(10)

    # 根据id找到元素，并点击，id和 html 元素的id不同，
# 和appiumserver、设备之间的消息流程类似于 selenium，和
    driver.find_element_by_id("io.manong.developerdaily:id/tab_bar_plus").click()
    time.sleep(1)
    driver.find_element_by_id("io.manong.developerdaily:id/btn_email").click()
    time.sleep(1)

    # 输入用户名、密码
    ele = driver.find_element_by_id("io.manong.developerdaily:id/edt_email")
    ele.send_keys('jcyrss@163.com')
    ele = driver.find_element_by_id("io.manong.developerdaily:id/edt_password")
    ele.send_keys('sdfsdf')

    time.sleep(2)
    # 点击登录
    driver.find_element_by_id('io.manong.developerdaily:id/btn_login').click()
    pass

except:
    print (traceback.format_exc())


input('**** Press to quit..')
driver.quit()
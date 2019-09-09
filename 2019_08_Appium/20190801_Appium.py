#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-01 and 0:58
FileName:20190801_Appium测试案例.py
Description：...
'''
from appium import webdriver
import time,traceback
# 【检查appium连接】
# adb devices -l
# 【启动虚拟机】
# nox_adb.exe connect 127.0.0.1:62001
# #【安装apk】
# adb install -r 测试程序名.apk
# 【获取包名】
# aapt dump badging D:\TestFiles\Appium\Apk\com.ibox.calculators_3.0.6_1306.apk
# 【获取active名】
# adb shell dumpsys activity recents | find "intent={" > D:\TestFiles\Appium\info.txt && D:\TestFiles\Appium\info.txt


# 这里定义的 desired_capabilities，作为下面 webdriver.Remote
# 初始化一个webdriver的参数。
# 这些键值对告诉appium server 测试程序希望进行的是什么什么样的测试
# 比如下面 platformName  和 platformVersion 两个配置项
desired_caps = {}
desired_caps['platformName'] = 'Android'  #测试平台,不能写错
desired_caps['platformVersion'] = '6.0'   #平台版本,不能写错
# 设备名称，其实没有太大的用处，只是给测试程序使用的，苹果手机一定要有
desired_caps['deviceName'] = 'test'
#apk 文件路径名，如果设备还没有此应用，则会安装。 什么是apk文件？
# android application package 安卓移动App安装包
desired_caps['app'] = r'd:\apk\toutiao.apk'
# app package名，一定要有，是开发者给app取的名字，可以唯一标识这个app
# 安卓上运行某个app，不是根据它的路径而是appid ，也就是这package name
# 怎么获取？后面会讲
desired_caps['appPackage'] = 'io.manong.developerdaily'
# app默认Activity，也是必须的参数。Activity 的概念后面会讲述，
# 目前我们就理解为一个用户操作界面就可以了
# 怎么获取？后面会讲
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'
# 一定要有该参数，否则测试过程中无法输入中文
# 加上这个参数会新加一种unicode输入法
desired_caps['unicodeKeyboard']  = True
# 保证了app 测试前不会清除应用数据，缺省是会清除数据的，
desired_caps['noReset'] = True
# appium server 认为 和客户端之间 无响应最大时间，超过这个时间就会停止服务
desired_caps['newCommandTimeout'] = 6000
# appium server 在这个URI上接收 客户端发送的rest API请求
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

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
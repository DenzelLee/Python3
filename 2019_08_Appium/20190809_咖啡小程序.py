#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-09 and 22:11
FileName:20190809_咖啡小程序.py
Description：...
小程序：成都购房助手
如何查看微信webview中的元素
1、手机打开【开发者模式】
2、app必须是debug模式。
3、手机通过USB连接电脑，且能够识别出来手机。
4、可以科学上网。

如何配置微信desired_caps环境参数
1、打开微信，在任意对话框中输入debugx5.qq.com。
2、点击发送成功的debugx5.qq.com，稍等片刻点击进入设置页面
3、切换到【seeting】，勾选【是否打开tbs内核】，保存退出
4、退出设置，重启微信端
5、开启谷歌浏览器的科学上网模式
6、打开chrome，地址栏输入chrome://inspect/#devices，可以看到设备介绍
7、接下来就可以轻松识别元素了，和用f12查看元素没有区别，请开始你的表演

代码实战（由于我没有安卓手机，只能用模拟器，模拟器没有网络，遂只能做到基础应用）：
上面这些搞定了，在Appium里写代码就简单了，先说下关键的几个点：
1、#必须加上此句desired_caps['chromeOptions']={'androidProcess': 'com.tencent.mm:tools'}
   #微信的package name=com.tencent.mm，activity=com.tencent.mm.ui.LauncherUI。
2、#可以通过下面的语句输出webview的名称
contexts=driver.contexts
print('contexts=',contexts)
3、#使用下面的语句切换到指定的webview里
driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
4、切换到webview里面，剩下的定位方式和web一模一样，就是上面讲的元素识别方法
5、#如果想返回原生态的view，可以用下面的语句
'''
from appium import webdriver
from time import sleep
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5',
    'deviceName': '127.0.0.1:62001',
    # 'app': r'D:\TestFiles\Appium\Apk\sqauto.apk',
    'appPackage': 'com.tencent.mm',
    'appActivity': 'com.tencent.mm.ui.LauncherUI',
    'unicodeKeyboard': True,
    'resetKeyboard':True,
    'noReset': True, # 初始化，True为了避免每次打开APP都提问你是否获取权限
    'newCommandTimeout': 6000,
    'automationName':'uiautomator2'
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
driver.implicitly_wait(20)
sleep(10)

text1 = driver.contexts
currentText = driver.current_context
print(f"全部上下文：{text1}，当前上下文：{currentText}")

# 微信顶部标题栏
title = driver.find_element_by_id("com.tencent.mm:id/qh")
print(f"当前标题栏：{title.text}")
sleep(15)

# 点击搜索按钮
driver.find_element_by_id("com.tencent.mm:id/qi").click()
sleep(10)

# 输入星巴克搜索
driver.find_element_by_id("com.tencent.mm:id/li").send_keys("星巴克\n")
sleep(3)
driver.find_element_by_id("com.tencent.mm:id/c2h").click()
sleep(10)

# 网络异常打印title
print(driver.find_element_by_accessibility_id("当前所在页面,搜一搜").text)
sleep(5)

# 返回主页
driver.find_element_by_accessibility_id("返回").click()
sleep(5)
driver.find_element_by_accessibility_id("返回").click()
sleep(5)

# 初始化坐标
size = driver.get_window_size()
print(size)
startx = size["width"]*0.5
starty = size["height"]*0.2
endy = size["height"]*0.8
sleep(5)

# 下拉显示小程序
driver.swipe(startx, starty, startx, endy, 500)
sleep(5)

# 打印小程序名称
name = driver.find_element_by_xpath("//android.widget.TextView[@text='成都购房顾问']")
print("小程序名称为：%s" %(name.text))

# # 微信底部菜单栏
# wechat = driver.find_element_by_id("com.tencent.mm:id/b9g")
# print(wechat.text)

input("Press anykey to quit...")
driver.quit()


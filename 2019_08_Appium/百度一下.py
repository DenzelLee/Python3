#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-05 and 12:52
FileName:百度一下.py
Description：...
'''
from appium import webdriver
import time
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5',
    'deviceName': '127.0.0.1:62001',
    # 'app': r'd:\apk\toutiao.apk',
    'appPackage': 'com.tencent.padbrowser',
    'appActivity': 'com.tencent.padbrowser.SplashActivity',
    'unicodeKeyboard': True,
    'resetKeyboard':True,
    'noReset': True, # 初始化，True为了避免每次打开APP都提问你是否获取权限
    'newCommandTimeout': 6000,
    'automationName':'uiautomator2'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
time.sleep(8)

eles = driver.find_elements_by_xpath("//*[@resource-id='com.tencent.padbrowser:id/quicklink_container']/android.widget.RelativeLayout")
print(eles)
driver.tap([(8,512),(215,645)],100)

# for w in eles:
#     print(w.text)
#     if r"百度" in w.text:
#         w.click()
time.sleep(8)
# mainWindows = driver.current_window_handle
driver.find_element_by_xpath("//*[@resource-id='kw']").send_keys("香港\n")
# for i in driver.window_handles:
#     driver.switch_to.window(i)
#     if i != driver.window_handles[0]:
#         print('已经切换到新窗口')
#         break
print(f"新窗口名称：{driver.title}")
driver.quit()





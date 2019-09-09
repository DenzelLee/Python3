#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-07-28 and 12:34
FileName:20190728_文件上传.py
Description：...
'''
'''
写一个程序实现如下的自动化过程
- 登录   https://tinypng.com/ 
- 点击 上传文件的虚线框
- 选择 插图，在本地目录中选择一张准备好的图片 , 查看是否能够上传图片成功
'''
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://tinypng.com/")
driver.implicitly_wait(30)

# 截图完整网页（必须以png格式保存，否则会报错）
driver.get_screenshot_as_file(r"D:\test2.png")

# 截图单个元素（必须以png格式保存，否则会报错）
ele = driver.find_element_by_css_selector("img[src='/images/example-orig.png']")
ele.screenshot_as_png
ele.screenshot(r"D:\test1.png")

# 打印url地址
driver.find_element_by_css_selector(".icon").click()
print(driver.title)
print(driver.current_url)
sleep(3)

# 上传文件，导入上传文件包
import win32com.client
shell = win32com.client.Dispatch("WScript.Shell")
sleep(1)

# 末尾必须加\n或者\r\n来确认提交
shell.Sendkeys(r"D:\test1.png"+"\r\n")






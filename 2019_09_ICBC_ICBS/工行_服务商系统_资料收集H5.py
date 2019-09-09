#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-29 and 15:27
FileName:工行_服务商系统_资料收集H5.py
Description：...
使用说明：
1.文件上传的路径，需要修改为本机的路径，不能带中文，否则编码错误，会报错。
2.文件上传的过程，由于调取本地的控件，禁止操作鼠标，否则会识别不到控件，找不到上传的文件。
3.脚本的定位过程，由于时间关系，没有做css优化，用的xpath路径，如果要长期使用，建议改为CSS相对路径。
预期结果：
----1.资料收集----
----2.文件上传----
----3.文本提交----
----4.打印单号----
商户信息: 单号
商户信息: 1298
'''

from time import *
from selenium import webdriver
import win32com.client
import time
# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y%m%d%S', time.localtime(time.time()))
# 打开浏览器
driver = webdriver.Chrome()
driver.get("http://icbc-isv.wangtest.cn/merchant-h5/?partner_no=P019002666&sales_employees_id=130#/")
driver.implicitly_wait(15)

# 封装操作函数
def addpicture(xppath,ppath):
    driver.find_element_by_xpath(f"{xppath}").click()
    shell = win32com.client.Dispatch("WScript.Shell")
    sleep(1.5)
    shell.Sendkeys(f"{ppath}"+"\r\n")
    return
def sendtext(xspath,stext):
    driver.find_element_by_xpath(xspath).send_keys(stext)
    return

print("----1.资料收集----")
# 门店名称
sendtext("/html[1]/body[1]/div[1]/div[1]/section[1]/div[2]/input[1]","门店名称%s" %(nowTime))
# 银行卡号
sendtext("/html[1]/body[1]/div[1]/div[1]/section[6]/div[2]/input[1]","6222803800010001010")
# 开户行
sendtext("/html[1]/body[1]/div[1]/div[1]/section[7]/div[2]/input[1]","中国工商银行")
# 法人手机号
sendtext("/html[1]/body[1]/div[1]/div[1]/section[8]/div[2]/input[1]","18583990001")
# 联系人姓名
sendtext("/html[1]/body[1]/div[1]/div[1]/section[9]/div[2]/input[1]","联系人姓名%s" %(nowTime))
# 联系人手机号
sendtext("/html[1]/body[1]/div[1]/div[1]/section[10]/div[2]/input[1]","18583990001")
# 联系人邮箱
sendtext("/html[1]/body[1]/div[1]/div[1]/section[11]/div[2]/input[1]","270980001@qq.com")

print("----2.文件上传----")
# 营业执照号
addpicture("/html[1]/body[1]/div[1]/div[1]/section[3]/div[3]/div[1]/div[1]/div[1]/input[1]","D:\\picture\\1yyzz.jpg")
# 身份证正面
addpicture("/html[1]/body[1]/div[1]/div[1]/section[4]/div[3]/div[1]/div[1]/div[1]/input[1]","D:\\picture\\2sfz1.jpg")
# 身份证反面
addpicture("/html[1]/body[1]/div[1]/div[1]/section[4]/div[3]/div[2]/div[1]/div[1]/input[1]","D:\\picture\\3sfz2.jpg")
# 开户许可证
addpicture("/html[1]/body[1]/div[1]/div[1]/section[5]/div[3]/div[1]/div[1]/div[1]/input[1]","D:\\picture\\4khxkz1.jpg")

print("----3.文本提交----")
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/button[1]").click()
sleep(1)
driver.find_element_by_xpath("//a[contains(text(),'确定')]").click()

print("----4.打印单号----")
stores = driver.find_elements_by_css_selector(".bottom-section>p")
for s in stores:
    print("商户信息:",s.text)
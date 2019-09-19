#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-18 and 15:08
FileName:pythonApi.py
Description：...
1.清除所有课程、老师、培训班、培训班期
2.新增课程、老师、培训班、培训班期
3.列出课程、老师、培训班、培训班期
4.删除课程、老师、培训班、培训班期
5.检查课程、老师、培训班、培训班期

'''
from selenium import webdriver
from pprint import pprint
from time import sleep
import datetime, time
from random import randint
import sys
sys.path.append(r'D:\MyTest\Python3\Tmp\GitFile\2019_09_Robotframwork\20190919Addclass')
from config import *


# 获取当前格式化-年月日：时分秒
nowTimee = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))

class Webadmin():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    # driver = webdriver.Chrome()
    url = inurl
    # driver.implicitly_wait(10)
    rnum = randint(1,100)

    # 打开浏览器、登录账户
    def setupWeb(self,drivertype="chrome"):
        print("----准备启动驱动程序----")
        self.driver == None
        if drivertype == "chrome":
            self.driver = webdriver.Chrome()
        elif drivertype == "firefox":
            self.driver = webdriver.Firefox()
        else:
            raise Exception(f"\nCan not find driverqudong :{drivertype}\n")
        print("----打开浏览器----")
        self.driver.get(self.url)
    # 关闭浏览器
    def tearDown(self):
        print("----关闭浏览器----")
        self.driver.close()
    # 登录账户
    def loginWeb(self):
        print("----登录账户----")
        self.driver.get(self.url)
        self.driver.find_element_by_id("username").send_keys("auto")
        self.driver.find_element_by_id("password").send_keys("sdfsdfsdf")
        sleep(0.5)
        self.driver.find_element_by_css_selector(".btn.btn-success").click()
        sleep(1)
    # 添加课程
    def addcourseWeb(self):
        print("----添加课程----")
        self.driver.find_element_by_css_selector('*[ng-click="showAddOne=true"]').click()
        self.driver.find_element_by_css_selector('*[ng-model="addData.name"]').send_keys(f"语文课{self.rnum}")
        self.driver.find_element_by_css_selector('*[ng-model="addData.desc"]').send_keys("语文描述")
        self.driver.find_element_by_css_selector('*[ng-model="addData.display_idx"]').clear()
        self.driver.find_element_by_css_selector('*[ng-model="addData.display_idx"]').send_keys(self.rnum)
        self.driver.find_element_by_css_selector('*[ng-click="addOne()"]').click()
        sleep(1)
    # 列出课程
    def listcourseWeb(self):
        print("----列出课程----")
        courses = self.driver.find_elements_by_css_selector('tr>td:nth-child(2)')
        print(f"课程列表：{courses}")
        for one in courses:
            print(f"课程名称：{one.text}")
    # 清除所有课程
    def deleteallcourseWeb(self):
        print("----清除所有课程----")
        while True:
            courses = self.driver.find_elements_by_css_selector('tbody>tr')
            if courses == [] or len(courses) == 1:
               break
            else:
                self.driver.find_elements_by_css_selector('tbody>tr *[ng-click="delOne(one)"]')[1].click()
                sleep(0.5)
                self.driver.find_element_by_css_selector(".btn.btn-primary").click()
                sleep(1)
                print("----删除课程成功----")
if __name__=='__main__':
    w = Webadmin()
    w.setupWeb("chrome")
    w.loginWeb()
    w.addcourseWeb()
    w.listcourseWeb()
    w.deleteallcourseWeb()

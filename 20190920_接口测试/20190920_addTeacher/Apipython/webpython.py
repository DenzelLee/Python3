#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-20 and 15:08
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
from selenium.webdriver.support.ui import Select
# 获取当前格式化-年月日：时分秒
nowTimee = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))

# 导入自定义配置文件
import sys
sys.path.append(r'D:\MyTest\Python3\Tmp\Python3\20190920_接口测试\20190920_addTeacher')
from config import *

# 自定义UI测试库
class Webadmin():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    rnum = randint(1,100)
    # 打开浏览器、登录账户
    def startWeb(self,drivertype="chrome"):
        print("----准备启动驱动程序----")
        # self.driver == None
        if drivertype == "chrome":
            self.driver = webdriver.Chrome()
        elif drivertype == "firefox":
            self.driver = webdriver.Firefox()
        else:
            raise Exception(f"\nCan not find driverqudong :{drivertype}\n")
        print("----打开浏览器----")
        self.driver.get(insideUrl)
        self.driver.implicitly_wait(5)
    # 关闭浏览器
    def endWeb(self):
        print("----关闭浏览器----")
        self.driver.quit()
    # 登录账户
    def loginWeb(self):
        print("----登录账户----")
        self.driver.get(insideUrl)
        self.driver.find_element_by_id("username").send_keys(insideUserinfo["username"])
        self.driver.find_element_by_id("password").send_keys(insideUserinfo["password"])
        sleep(0.5)
        self.driver.find_element_by_css_selector(".btn.btn-success").click()
        sleep(1)

# 1----课程管理
    def selectcourseTab(self):
        print("----跳转课程页面----")
        self.driver.find_element_by_css_selector('*[href="#/"]').click()
        sleep(0.5)
    # 添加课程
    def addcourseWeb(self,coursename,coursedesc,coursenum=rnum):
        print("----添加课程----")
        self.driver.find_element_by_css_selector('*[ng-click="showAddOne=true"]').click()
        self.driver.find_element_by_css_selector('*[ng-model="addData.name"]').clear()
        self.driver.find_element_by_css_selector('*[ng-model="addData.name"]').send_keys(coursename)
        self.driver.find_element_by_css_selector('*[ng-model="addData.desc"]').clear()
        self.driver.find_element_by_css_selector('*[ng-model="addData.desc"]').send_keys(coursedesc)
        self.driver.find_element_by_css_selector('*[ng-model="addData.display_idx"]').clear()
        self.driver.find_element_by_css_selector('*[ng-model="addData.display_idx"]').send_keys(coursenum)
        self.driver.find_element_by_css_selector('*[ng-click="addOne()"]').click()
        sleep(1)
    # 列出课程
    def listcourseWeb(self):
        print("----列出课程----")
        courses = self.driver.find_elements_by_css_selector('tr>td:nth-child(2)')
        print(f"课程列表：{[i.text for i in courses]}")
        for one in courses:
            print(f"课程名称：{one.text}")
        return f"课程列表：{[i.text for i in courses]}"
    # 清除所有课程
    def deleteallcourseWeb(self):
        print("----清除所有课程----")
        self.driver.implicitly_wait(3)
        while True:
            courses = self.driver.find_elements_by_css_selector('tbody>tr')
            if courses == [] or len(courses) == 1:
               break
            else:
                # 我的系统第一条数据，删除时会报错，无法修复，所以这里和后面都只能用索引[1]，从第二位开始删除，不影响程序
                self.driver.find_elements_by_css_selector('tbody>tr *[ng-click="delOne(one)"]')[1].click()
                sleep(0.5)
                self.driver.find_element_by_css_selector(".btn.btn-primary").click()
                sleep(1)
                print("----删除课程成功----")
        self.driver.implicitly_wait(5)

# 2----老师管理
    def selectteacherTab(self):
        print("----跳转老师页面----")
        self.driver.find_element_by_css_selector('*[href="#/teacher"]').click()
        sleep(0.5)
    # 添加老师
    def addteacherWeb(self,teachername,loginname,teacherdesc,lesson,teachernum=rnum):
        print("----添加老师----")
        self.driver.find_element_by_css_selector('*[ng-click="showAddOne=true"]').click()
        self.driver.find_element_by_css_selector('*[ng-model="addEditData.realname"]').clear()
        self.driver.find_element_by_css_selector('*[ng-model="addEditData.realname"]').send_keys(teachername)
        self.driver.find_element_by_css_selector('*[ng-model="addEditData.username"]').clear()
        self.driver.find_element_by_css_selector('*[ng-model="addEditData.username"]').send_keys(loginname)
        self.driver.find_element_by_css_selector('*[ng-model="addEditData.desc"').clear()
        self.driver.find_element_by_css_selector('*[ng-model="addEditData.desc"]').send_keys(teacherdesc)
        self.driver.find_element_by_css_selector('*[ng-model="addEditData.display_idx"]').clear()
        self.driver.find_element_by_css_selector('*[ng-model="addEditData.display_idx"]').send_keys(teachernum)
        # 下拉框元素定位
        select = Select(self.driver.find_element_by_css_selector('*[ng-model="$parent.courseSelected"]'))
        select.select_by_visible_text(lesson)
        sleep(0.5)
        self.driver.find_element_by_css_selector('*[ng-click="addEditData.addTeachCourse()"]').click()
        sleep(0.5)
        self.driver.find_element_by_css_selector('*[ng-click="addOne()"]').click()
        sleep(1)
    # 列出老师
    def listteacherWeb(self):
        print("----列出老师----")
        courses = self.driver.find_elements_by_css_selector('tr>td:nth-child(2)')
        print(f"课程列表：{[i.text for i in courses]}")
        for one in courses:
            print(f"老师名称：{one.text}")
        return f"老师列表：{[i.text for i in courses]}"
    # 清除所有老师
    def deleteallteacherWeb(self):
        print("----清除所有老师----")
        self.driver.implicitly_wait(3)
        while True:
            teachers = self.driver.find_elements_by_css_selector('tbody>tr')
            if teachers == [] or len(teachers) == 1:
               break
            else:
                self.driver.find_elements_by_css_selector('tbody>tr *[ng-click="delOne(one)"]')[1].click()
                sleep(0.5)
                self.driver.find_element_by_css_selector(".btn.btn-primary").click()
                sleep(1)
                print("----删除老师成功----")
        self.driver.implicitly_wait(5)

# 3----培训班管理
    def selectclassTab(self):
        print("----跳转培训班页面----")
        self.driver.find_element_by_css_selector('*[href="#/training"]').click()
        sleep(0.5)
    # 添加培训班
    def addclassWeb(self, classname, classdesc,classnum, *lesson):
        print("----添加培训班----")
        self.driver.find_element_by_css_selector('*[ng-click="showAddOne=true"]').click()
        self.driver.find_element_by_css_selector('*[ng-model="addEditData.name"]').clear()
        self.driver.find_element_by_css_selector('*[ng-model="addEditData.name"]').send_keys(classname)
        self.driver.find_element_by_css_selector('*[ng-model="addEditData.desc"]').clear()
        self.driver.find_element_by_css_selector('*[ng-model="addEditData.desc"]').send_keys(classdesc)
        self.driver.find_element_by_css_selector('*[ng-model="addEditData.display_idx"]').clear()
        self.driver.find_element_by_css_selector('*[ng-model="addEditData.display_idx"]').send_keys(classnum)
        # 下拉框元素定位
        if len(lesson)>0:
            for i in lesson:
                select = Select(self.driver.find_element_by_css_selector(
                    '*[ng-options="course as course.name for course in courseList"]'))
                select.select_by_visible_text(i)
                sleep(0.5)
                self.driver.find_element_by_css_selector('*[ng-click="addEditData.addTeachCourse()"]').click()
                sleep(0.5)
        elif len(lesson)==0:
            pass
        self.driver.find_element_by_css_selector('*[ng-click="addOne()"]').click()
        sleep(1.5)

    # 列出培训班
    def listclassWeb(self):
        print("----列出培训班----")
        classs = self.driver.find_elements_by_css_selector('tr>td:nth-child(2)')
        print(f"培训班列表：{[i.text for i in classs]}")
        for one in classs:
            print(f"培训班名称：{one.text}")
        return f"培训班列表：{[i.text for i in classs]}"

    # 清除所有培训班
    def deleteallclassWeb(self):
        print("----清除所有培训班----")
        self.driver.implicitly_wait(3)
        while True:
            classs = self.driver.find_elements_by_css_selector('tbody>tr')
            if classs == [] or len(classs) == 1:
                break
            else:
                self.driver.find_elements_by_css_selector('tbody>tr *[ng-click="delOne(one)"]')[1].click()
                sleep(0.5)
                self.driver.find_element_by_css_selector(".btn.btn-primary").click()
                sleep(1)
                print("----删除培训班成功----")
        self.driver.implicitly_wait(5)
# 4----培训班期管理
    def selectclassqiTab(self):
        print("----跳转培训班期页面----")
        self.driver.find_element_by_css_selector('*[href="#/traininggrade"]').click()
        sleep(0.5)
    # 添加培训班
    def addclassqiWeb(self, classname, classdesc,classnum, *lesson):
        print("----添加培训班期----")
        self.driver.find_element_by_css_selector('*[ng-click="showAddOne=true"]').click()
        self.driver.find_element_by_css_selector('*[ng-model="addEditData.name"]').clear()
        self.driver.find_element_by_css_selector('*[ng-model="addEditData.name"]').send_keys(classname)
        self.driver.find_element_by_css_selector('*[ng-model="addEditData.desc"]').clear()
        self.driver.find_element_by_css_selector('*[ng-model="addEditData.desc"]').send_keys(classdesc)
        self.driver.find_element_by_css_selector('*[ng-model="addEditData.display_idx"]').clear()
        self.driver.find_element_by_css_selector('*[ng-model="addEditData.display_idx"]').send_keys(classnum)
        # 下拉框元素定位
        if len(lesson)>0:
            for i in lesson:
                select = Select(self.driver.find_element_by_css_selector(
                    '*[ng-model="$parent.addEditData.training_id"]'))
                select.select_by_visible_text(i)
                sleep(0.5)
        elif len(lesson)==0:
            pass
        self.driver.find_element_by_css_selector('*[ng-click="addOne()"]').click()
        sleep(1.5)

    # 列出培训班
    def listclassqiWeb(self):
        print("----列出培训班期----")
        classs = self.driver.find_elements_by_css_selector('tr>td:nth-child(2)')
        print(f"培训班期列表：{[i.text for i in classs]}")
        for one in classs:
            print(f"培训班期名称：{one.text}")
        return f"培训班列表：{[i.text for i in classs]}"

    # 清除所有培训班
    def deleteallclassqiWeb(self):
        print("----清除所有培训班期----")
        self.driver.implicitly_wait(3)
        while True:
            classs = self.driver.find_elements_by_css_selector('tbody>tr')
            if classs == [] or len(classs) == 1:
                break
            else:
                self.driver.find_elements_by_css_selector('tbody>tr *[ng-click="delOne(one)"]')[1].click()
                sleep(0.5)
                self.driver.find_element_by_css_selector(".btn.btn-primary").click()
                sleep(1)
                print("----删除培训班期成功----")
        self.driver.implicitly_wait(5)


if __name__=='__main__':
    w = Webadmin()
    # w.startWeb("chrome")
    # w.loginWeb()
    # w.selectteacherTab()
    # w.addteacherWeb("语文老师1","语文账户1","语文描述1","报错课程_20190908",1)
    # w.listteacherWeb()
    # w.deleteallteacherWeb()
    # w.endWeb()

    # w.startWeb("chrome")
    # w.loginWeb()
    # w.selectclassTab()
    # w.addclassWeb("语文培训1", "语文描述1", 1)
    # w.addclassWeb("语文培训1", "语文描述1", 1, "初中语文","初中数学")
    # w.listclassWeb()
    # w.deleteallclassWeb()
    # w.endWeb()

    w.startWeb("chrome")
    w.loginWeb()
    w.selectclassqiTab()
    # w.addclassqiWeb("语文培训班期1", "语文班期描述1", 1)
    w.addclassqiWeb("语文培训班期1", "语文班期描述1", 100, "1","22")
    w.listclassqiWeb()
    w.deleteallclassqiWeb()
    w.endWeb()
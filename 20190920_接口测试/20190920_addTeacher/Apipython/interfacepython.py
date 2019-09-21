#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-20 and 18:20
FileName:interfacepython.py
Description：...
1.清理老师列表
2.新增课程
3.新增老师
4.列出老师
'''
import datetime, time
from pprint import pprint
import requests
import json
# 导入自定义配置文件
import sys
sys.path.append(r'D:\MyTest\Python3\Tmp\Python3\20190920_接口测试\20190920_addTeacher')
from config import *

# 获取当前格式化-年月日：时分秒
nowTimee = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))


class Interadmin():
    # 登录账户
    def interlogin(self):
        print("----开始登陆----")
        loginurl = f"http://{insideDatabase[0]}:{insideDatabase[1]}/api/mgr/loginReq"
        response = requests.post(url=loginurl, data={"username": "auto", "password": "sdfsdfsdf"})
        res = response.json()
        self.cookies = dict(response.cookies)
        print(self.cookies)
        print(f"----登陆成功：{res}----")
        return res
    # 添加课程
    def interaddcourse(self,cname,cdesc,cnum):
        print("----开始添加课程----")
        addurl = f"http://{insideDatabase[0]}:{insideDatabase[1]}/api/mgr/sq_mgr/"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        payload = {"action": "add_course", "data":f'{{"name":"{cname}","desc":"{cdesc}","display_idx":"{cnum}"}}'}
        response = requests.post(url=addurl, headers=headers, cookies=self.cookies, data=payload)
        res = response.json()
        print(f"----添加课程成功：{res}----")
        return res['id']
    # 列出课程
    def interlistcourse(self,pagenum=1,pagesize=100):
        # get请求(参数用params，不用data）
        print("\n----列出课程----\n")
        url = f"http://{insideDatabase[0]}:{insideDatabase[1]}/api/mgr/sq_mgr/"
        payload = {'action':'list_course','pagenum':pagenum,'pagesize':pagesize}
        # params可以避免参数中包含&等特殊字符
        listHttp = requests.get(url=url, params=payload,cookies=self.cookies)
        listret = listHttp.json()
        # print(type(getret))
        print(str(listret)+"，列出课程信息！")
        return listret
    def intergetcourse(self,pagenum=1,pagesize=100):
        # get请求(参数用params，不用data）
        print("\n----列出课程----\n")
        url = f"http://{insideDatabase[0]}:{insideDatabase[1]}/api/mgr/sq_mgr/"
        payload = {'action':'list_course','pagenum':pagenum,'pagesize':pagesize}
        # params可以避免参数中包含&等特殊字符
        listHttp = requests.get(url=url, params=payload,cookies=self.cookies)
        listret = listHttp.json()
        # print(type(getret))
        print(str(listret)+"，列出课程信息！")
        print(listret['retlist'][1]['id'],listret['retlist'][1]['name'])
        return listret['retlist'][1]['id'],listret['retlist'][1]['name']
    # 删除课程
    def interdeletecourse(self,cid):
        # post请求
        print("\n----删除课程----\n")
        url = f"http://{insideDatabase[0]}:{insideDatabase[1]}/api/mgr/sq_mgr/"
        headers = {"Content-Type":"application/x-www-form-urlencoded"}
        payload = {'action': 'delete_course','id': cid}
        delHttp = requests.delete(url=url, headers=headers, data=payload,cookies=self.cookies)
        deltret = delHttp.json()
        # print(type(postret))
        pprint(str(deltret)+"，删除课程信息！")
        return deltret
    # 清空课程
    def interdeleteallcourse(self):
        print("----开始清空课程----")
        listcourse = self.interlistcourse()['retlist']
        idlist = [i['id'] for i in listcourse]
        print(f"课程数据已清空：{len([self.interdeletecourse(i) for i in idlist])}次")
    def interaddteacher(self,kusername,krealname,kdesc,knum,lessonid,lessonname,password="sq888"):
        print("----开始添加老师----")
        addurl = f"http://{insideDatabase[0]}:{insideDatabase[1]}/api/mgr/sq_mgr/"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        coursel = [{"id":f"{lessonid}","name":f"{lessonname}"}]
        payload = {"action":"add_teacher","data":f'{{"username":"{kusername}","courses":{json.dumps(coursel)},"realname":"{krealname}","desc":"{kdesc}","display_idx":{knum},"password":"{password}"}}'}
        response = requests.post(url=addurl, headers=headers, cookies=self.cookies, data=payload)
        res = response.json()
        print(f"----添加老师成功：{res}----")
        return res
    def interlistteacher(self,page=1,pagesize=100):
        print("----开始列出老师----")
        listurl = f"http://{insideDatabase[0]}:{insideDatabase[1]}/api/mgr/sq_mgr/"
        headers = {"Content-Type":"application/x-www-form-urlencoded"}
        payload = {"action":"list_teacher","pagenum":page,"pagesize":pagesize}
        response = requests.get(url = listurl,headers =headers,params = payload,cookies = self.cookies )
        res = response.json()
        print(f"----列出老师成功：{res}----")
        return res
    def interdeleteteacher(self,cid):
        print("----开始删除老师----")
        deleteurl = f"http://{insideDatabase[0]}:{insideDatabase[1]}/api/mgr/sq_mgr/"
        headers = {"Content-Type":"application/x-www-form-urlencoded"}
        payload = {"action":"delete_teacher","id":cid}
        response = requests.delete(url = deleteurl,headers =headers,data = payload,cookies = self.cookies )
        res = response.json()
        print(f"----删除老师成功：{res}----")
        return res
    def interdeleteallteacher(self):
        print("----开始清空老师----")
        listteacher = self.interlistteacher()['retlist']
        idlist = [i['id'] for i in listteacher]
        print(f"老师数据已清空：{len([self.interdeleteteacher(i) for i in idlist])}次")
if __name__=="__main__":
    i = Interadmin()
    i.interlogin()
    i.interdeleteallcourse()
    i.interaddcourse(f'python{nowTimee}','python1',100)
    lessonid,lessonname = i.intergetcourse()
    i.interaddteacher(f'teacher{nowTimee}',f'teacher{nowTimee}','teacherdesc',100,lessonid,lessonname)
    i.interlistteacher()
    # i.interdeleteteacher(lessonid)
    i.interdeleteallteacher()
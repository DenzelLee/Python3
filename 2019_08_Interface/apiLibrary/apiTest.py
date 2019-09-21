#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-18 and 12:23
FileName:courseAPI.py
Description：...
端口占用：http://vip.ytesting.com:80/qa01Controller.do?articleInfo&id=ff8080816a4c93fc016a4d3f42100046
目的：
1.添加课程
2.列出课程
3.修改课程
4.删除课程
5.增加/删除/查询/修改老师
'''
# 导入接口测试库
import requests,json,time
from pprint import pprint

# 配置fiddler代理,请求后面带上proxies=proxies, verify=False，就可以通过fiddler拦截请求
# proxies = {'http': 'http://localhost:8888', 'https':'http://localhost:8888'}
# response = requests.post(url, data=payload, proxies=proxies, verify=False)

# 测试环境Host（ip等铭感信息建议放在单独的py文件中）
testHost = "127.0.0.1:8066"
# 获取当前时间戳
nowTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

#基本类（后面类都继承并调用该类）
class Basic:
    # 登录账户
    def login(self,username,password):
        # 尽可能少用globa全局变量
        # global cookies
        print("\n----登录账户----\n")
        url = f"http://{testHost}/api/mgr/loginReq"
        payload = {"username":username,"password":password}
        response = requests.post(url, data=payload)
        loginres = dict(response.json())
        self.cookies = dict(response.cookies)
        self.sessionid = response.cookies['sessionid']
        # print(f"登录成功：{loginres}...{cookies}")
        if loginres["retcode"] == 0:
            print(f"登录成功：{loginres}，获取cookeis：{self.cookies}")
        else:
            print(f"登录失败，账号或密码错误!错误信息：{self.cookies}")
        return loginres
# 课程类
class Course(Basic):
    def __init__(self,cookies=None):
        self.cookies = cookies

    # 列出课程
    def list_course(self,pagenum,pagesize):
        # get请求(参数用params，不用data）
        print("\n----列出课程----\n")
        url = f"http://{testHost}/api/mgr/sq_mgr/"
        payload = {'action':'list_course','pagenum':pagenum,'pagesize':pagesize}
        # params可以避免参数中包含&等特殊字符
        listHttp = requests.get(url=url, params=payload,cookies=self.cookies)
        listret = listHttp.json()
        # print(type(getret))
        print(str(listret)+"，列出课程信息！")
        return listret

    # 添加课程
    def add_course(self,name,desc,display_idx):
        # post请求
        print("\n----添加课程----\n")
        url = f"http://{testHost}/api/mgr/sq_mgr/"
        headers = {"Content-Type":"application/x-www-form-urlencoded"}
        # payload data字典中，参数的变量值，也要加引号
        payload = {'action': 'add_course','data': f'{{"name":"{name}","desc":"{desc}","display_idx":{display_idx}}}'}
        # payload = {'action': 'add_course','data': '{"name":"%s","desc":"%s","display_idx":%s}'% (name, desc, display_idx)}
        addHttp = requests.post(url=url, headers=headers, data=payload,cookies=self.cookies)
        addtret = addHttp.json()
        # print(type(postret))
        pprint(str(addtret)+"，添加课程信息！")
        return addtret

    # 删除课程
    def delete_course(self,cid):
        # post请求
        print("\n----删除课程----\n")
        url = f"http://{testHost}/api/mgr/sq_mgr/"
        headers = {"Content-Type":"application/x-www-form-urlencoded"}
        payload = {'action': 'delete_course','id': cid}
        delHttp = requests.delete(url=url, headers=headers, data=payload,cookies=self.cookies)
        deltret = delHttp.json()
        # print(type(postret))
        pprint(str(deltret)+"，删除课程信息！")
        return deltret

    # 修改课程
    def modify_course(self,cid,name,desc,display_idx):
        # post请求
        print("\n----修改课程----\n")
        url = f"http://{testHost}/api/mgr/sq_mgr/"
        headers = {"Content-Type":"application/x-www-form-urlencoded"}
        payload = {'action':'modify_course',
                   'id':cid,
                  'newdata':
                   '''
                  {"name":"%s",
                  "desc":"%s",
                  "display_idx":"%s"
                  }'''%(name,desc,display_idx)
        }
        delHttp = requests.put(url=url, headers=headers, data=payload,cookies=self.cookies)
        deltret = delHttp.json()
        # print(type(postret))
        pprint(str(deltret)+"，修改课程信息！")
        return deltret
#老师类
class Teacher(Basic):
    def list_teacher(self,pagenum="1",pagesize="100"):
        print("\n----列出老师----\n")
        url = f"http://{testHost}/api/mgr/sq_mgr/"
        payload = {"action":"list_teacher","pagenum":pagenum,"pagesize":pagesize}
        response = requests.get(url=url,params=payload,cookies=self.cookies)
        listres = response.json()
        pprint(f"{listres}"+",列出老师信息")
        return listres

    def add_teacher(self,realname,username,desc,display_idx,courses,password='sq888'):
        print("\n----添加老师----\n")
        url = f"http://{testHost}/api/mgr/sq_mgr/"
        headers = {"Content-Type":"application/x-www-form-urlencoded"}
        payload = {"action":"add_teacher",
                   "data":f'''
                          {{"realname":"{realname}","username":"{username}","desc":"{desc}","display_idx":{display_idx},
                          "courses":{json.dumps(courses)},
                          "password":"{password}"}}'''
                   }
        response = requests.post(url=url,headers=headers,data=payload,cookies=self.cookies)
        addres = response.json()
        pprint(str(addres)+",新增老师信息！")
        return addres

    # 删除老师
    def delete_teacher(self, tid):
        # post请求
        print("\n----删除老师----\n")
        url = f"http://{testHost}/api/mgr/sq_mgr/"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        payload = {'action': 'delete_teacher', 'id': tid}
        response = requests.delete(url=url, headers=headers, data=payload, cookies=self.cookies)
        deltret = response.json()
        # print(type(postret))
        pprint(str(deltret) + "，删除老师信息！")
        return deltret

    # 修改老师
    def modify_teacher(self,tid,realname,username,desc,display_idx,courses,password='sq888'):
        # post请求
        print("\n----修改老师----\n")
        url = f"http://{testHost}/api/mgr/sq_mgr/"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        payload = {"action": "modify_teacher",
                   "id":f'{tid}',
                   "newdata":f'''
                          {{"realname":"{realname}","username":"{username}","desc":"{desc}","display_idx":{display_idx},
                          "courses":{json.dumps(courses)},
                          "password":"{password}"}}'''
                   }
        response = requests.put(url=url, headers=headers, data=payload, cookies=self.cookies)
        deltret = response.json()
        # print(type(postret))
        pprint(str(deltret) + "，修改老师信息！")
        return deltret

# 自测函数
if __name__== '__main__':
    # ----测试老师
    test = Teacher()
    # 登录
    loginres= test.login('auto', 'sdfsdfsdf')
    # 新增老师
    test.add_teacher(f"老师姓名{nowTime}",f"登录名称{nowTime}",f"描述{nowTime}",10,
                     [{"id":1198,"name":"测试课程2019-08-24 13:06:14"},{"id":1199,"name":"测试课程2019-08-24 13:06:47"}])
    # 列出老师
    test.list_teacher(1,100)
    # 修改老师
    test.modify_teacher(255,f"老师姓名{nowTime}1",f"登录名称{nowTime}1",f"描述{nowTime}1",10,
                     [{"id":1198,"name":"测试课程2019-08-24 13:06:14"},{"id":1199,"name":"测试课程2019-08-24 13:06:47"}])
    # 列出老师
    test.list_teacher(1,100)
    # 批量循环删除老师
    test.delete_teacher(254)
    tlist = test.list_teacher(1,100)
    newlist = []
    for id in tlist['retlist']:
        newlist.append(id['id'])
    for i in newlist:
        test.delete_teacher(i)

    # # #----测试课程
    # # 子类继承父类，可以调用父类的方法
    # test = Course()
    # # 登录账户
    # loginres= test.login('auto', 'sdfsdfsdf')
    # # 列出课程
    # test.list_course(1,20)
    # # 添加课程
    # addcourse = test.add_course(f'语文课{nowTime}1','语文描述',5)
    # ccid = addcourse['id']
    # # 修改课程
    # test.modify_course(ccid,f'语文课{nowTime}2','语文描述',5)
    # # 删除课程
    # test.delete_course(ccid)







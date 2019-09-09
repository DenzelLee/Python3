#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
Author:lihao
Date&Time:2019-06-30 and 22:09
FileName:手机号检测器
Description of parameters：Mobile移动, Unicom联通, Telecom电信
"""
# 题目1：1.接收一个数字字符串；2.判断其运营商；3.判断其长度；4.判断其是否数字类型；
# Mobile移动, Unicom联通, Telecom电信
# ----------------------------------
mList = [135,134,136,137,138,139,147,150,151,152,157,158,159,172,178,182,183,184,187,188,198]
uList = [130,131,132,145,155,156,166,171,175,176,185,186]
tList = [133,149,153,173,177,180,181,189,191,199]
getPhone=input("请输入您的电话号码：")
nList = list(range(10))#定义一个数字列表，判断号码是否位数字
sum=0
for i in getPhone[0:12]:
    if int(i) in nList:
        sum+=1
    else:
        print(i+"is not number")
print("当前手机号中数字个数为："+str(sum))
if sum ==11:
    getPhones = getPhone[0:0+3]
    print("您的运营商号码为："+getPhones+"\n")
    if int(getPhones) in mList:
        print("尊敬的"+str(getPhones)+"移动客户，欢迎您！")
    elif int(getPhones) in uList:
        print("尊敬的" + str(getPhones) + "联通客户，欢迎您！")
    elif int(getPhones) in tList:
        print("尊敬的"+str(getPhones)+"电信客户，欢迎您！")
    else:
        print("当前手机号是黑号，公安民警5分钟抵达现场！谢谢。")
else:
    print("亲，您输入的电话号码长度有误！请重新输入。")


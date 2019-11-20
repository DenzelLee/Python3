#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-26 and 21:09
FileName:20190827_案例_调用外部程序.py
Description：...
'''
import time
import os
import glob
from pprint import pprint
import subprocess
nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

# 如果打印乱码，进入setting-editor-file encoding 设置为gbk和gbk，即可解码为肉眼可见的字符

# print("---- 1.默认阻塞式调用 ----")
# os.system("for %i in (1, 2, 3) do @echo %i")
#
# print("---- 2.加start关键字，非阻塞式调用 ----")
# testFile = os.system("start for %i in (1, 2, 3) do @echo %i")
# print("1.返回0成功；2.返回1失败；3.返回2系统错误；\n--当前结果：",testFile)

# print("---- 3.阻塞式调用:获取本地ip地址 ----")
# # subprocess.check_output(["echo", "hello python"])
# ip = subprocess.check_output("ipconfig", encoding="gbk")
# # print(type(ip), "\n")
# pprint(((ip.split("本地链接 IPv6 地址. . . . . . . . : fe80::8050:a90f:c2"
#     "d8:12bd%15")[1]).split("子网掩码  . . . . . . . . . . . . : 255.255.255.0")[0]).strip())

# print("---- 4.加wait（）方法，非阻塞式调用 ----")
# child = subprocess.Popen(["ping","www.baidu.com"])
# # wait()方法等待子进程结束，主进程才执行
# child.wait()
# print("\n--wait（）方法等待子进程结束，主进程才执行")



# ----subprocess io输入输出实例
# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/8/26
import subprocess

data = subprocess.check_output("mspaint")
print(data)

# 使用示范
subprocess.Popen("ipconfig")
print("after")

# 得到外部程序的输出
popen = subprocess.Popen(
    "ipconfig",
    stdout=subprocess.PIPE, # 标准输出文件文件
    encoding="gbk",
)
out, err = popen.communicate()
print("out =", out)
print(err)

# 调用外部程序，并获取其输入和输出，进行控制
popen = subprocess.Popen(
    "python",
    stdin=subprocess.PIPE, # 标准输入文件
    stdout=subprocess.PIPE, # 标准输出文件文件
    stderr=subprocess.PIPE, # 标准错误文件
    encoding="utf8",
)

inputList = ["hello", "world", "java", "python"]

out, err = popen.communicate("\n".join(inputList))

print(out)
print(err)
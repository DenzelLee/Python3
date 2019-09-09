#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-03 and 10:39
FileName:20190903_客户端.py
Description：...
'''
import time, datetime

# 获取当前格式化-年月日：时分秒
nowTimee = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))

import socket
# 创建客户端socket
usk = socket.socket()

# 建立服务器连接
usk.connect(("127.0.0.1",12001))

# 发送连接请求
usk.sendall(bytes("---- Client:Usk用户请求连接 ----", encoding="utf8"))

# 接收响应信息
response = usk.recv(1024)
print(str(response,"utf8"))

usk.close()
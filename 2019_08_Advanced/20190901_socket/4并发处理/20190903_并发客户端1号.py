#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-03 and 15:35
FileName:20190903_并发客户端1号.py
Description：...
'''
import time, datetime

# 获取当前格式化-年月日：时分秒
nowTimee = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))

import socket
ip_port = (("127.0.0.1",18000))
sk = socket.socket()
sk.connect(ip_port)
print("\n---- 启动客户端 ----")

while True:
    inp = input("客户端1号>>>")
    inp = "".join(["-客户端1号：",inp,"\n"])
    sk.sendall(bytes(inp,"utf8"))
    if inp =='exit':
        break
    server_response = sk.recv(1024)
    print("客户端收到：",str(server_response,encoding="utf8"))
sk.close()
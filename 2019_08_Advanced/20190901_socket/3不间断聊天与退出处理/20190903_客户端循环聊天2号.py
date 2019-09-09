#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-03 and 15:01
FileName:20190903_客户端循环聊天2号.py
Description：...
'''
import time, datetime

# 获取当前格式化-年月日：时分秒
nowTimee = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))

import socket
ip_port = ("127.0.0.1",14003)
usk = socket.socket()
usk.connect(ip_port)
while True:
    send_data = input("用户输入>>>")
    usk.sendall(bytes(send_data, encoding="utf8"))
    print("发出的消息：", send_data)

    recv_data = usk.recv(1024)
    print("收到的消息：", str(recv_data, encoding="utf8"))

usk.close()
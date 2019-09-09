#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-03 and 10:39
FileName:20190903_服务器.py
Description：...
'''
import time, datetime

# 获取当前格式化-年月日：时分秒
nowTimee = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))

import socket

ip_port = ("127.0.0.1",12001)

# 创建一个socket对象
sk = socket.socket()
print("---- 1.服务器对象创建成功 ----")

# 绑定ip和端口,ip参数必须是元组形式
sk.bind(ip_port)
print("---- 2.绑定地址成功 ----")

# 启动监听
sk.listen(5)
print("---- 3.启动监听成功:等待连接 ----")


# 创建子窗口
conn,addr = sk.accept()
print("---- 4.子窗口创建成功 ----")

# 等待接收客户端数据
client_data = conn.recv(1024)
print("---- 5.已接收道德客户端数据 ----\n")
print(str(client_data, "utf8"))

# 返回接收成功
conn.sendall(bytes("Service:Usk用户连接成功",encoding="utf8"))
print("\n---- 6.客户端数据接收成功，返回响应 ----")

print("---- 成功通讯！----")
sk.close()


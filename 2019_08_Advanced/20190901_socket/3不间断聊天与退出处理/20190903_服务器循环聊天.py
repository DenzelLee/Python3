#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-03 and 13:21
FileName:20190903_服务器循环聊天.py
Description：...
'''
import time, datetime

# 获取当前格式化-年月日：时分秒
nowTimee = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))

import socket
ip_port = ("127.0.0.1",14003)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

print("---- 服务器已启动 ----")
while True:
    conn, addr = sk.accept()
    print(f"--用户信息：{addr}")
    # 获取一个用户，完成多次聊天
    while True:
        recv_data = str(conn.recv(1024), encoding="utf8")
        if recv_data == " ":
            print("收到的消息：", "-- 消息为空 --")
        elif recv_data == None:
            print("收到的消息：", "-- 消息为None --")
        elif recv_data == "null":
            print("收到的消息：", "-- 消息为null --")
        elif recv_data:
            print("收到的消息：", recv_data, )
        else:
            # 收到消息，bytes解码展示
            raise Exception("收到的消息：","--未知异常")

        # 发送消息，str编码展示
        send_data = input("服务器发出>>>")
        conn.sendall(bytes(send_data, encoding="utf8"))
        print("发出的消息：", send_data)

conn.close()
sk.close()





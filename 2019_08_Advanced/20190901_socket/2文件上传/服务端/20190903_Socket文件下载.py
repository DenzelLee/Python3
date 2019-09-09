#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-03 and 11:38
FileName:20190903_Socket文件下载.py
Description：...
'''
import time, datetime

# 获取当前格式化-年月日：时分秒
nowTimee = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))

import socket,os
ip_post = ("127.0.0.1",13000)
dsk = socket.socket()
dsk.bind(ip_post)
dsk.listen(5)
print("---- 服务器已启动，等待接收连接：")


def get_file(conn_obj):
    """
    接受文件
    :param sk_obj: socket 对象
    :return:
    """
    # 接收文件大小
    file_size = int(conn_obj.recv(1024).decode("utf8"))
    # 发送用str
    conn_obj.sendall(str(f"---- 文件大小接收成功:{file_size} ").encode("utf8"))

    file_name = conn_obj.recv(1024).decode("utf8")
    conn_obj.sendall(str(f"---- 文件姓名接收成功:{file_name} ").encode("utf8"))

    # 循环接收文件
    with open("./%s" %file_name,"wb") as f:
        while file_size > 0:
            f.write(conn_obj.recv(1024))
            file_size -= 1024
            print("--写入成功")

conn,addr = dsk.accept()
get_file(conn)

conn.close()
dsk.close()
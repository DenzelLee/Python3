#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-03 and 11:37
FileName:20190903_Socket文件上传.py
Description：...
'''
import time, datetime

# 获取当前格式化-年月日：时分秒
nowTimee = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
import socket,os

# ip地址
ip_post = ("127.0.0.1",13000)

# 创建客户端socket
usk = socket.socket()

# 建立服务器连接
usk.connect(ip_post)

# 发送连接请求
def post_file(conn_obj,ppath):
    """
    上传文件
    :param sk_obj:  socket 对象
    :param file_path:  文件的路径
    :return:
    """
    # Os方法执行路径，获取文件大小的值
    file_size = os.stat(ppath).st_size
    conn_obj.sendall(str(file_size).encode("utf8"))
    conn_obj.recv(1024)

    # file_name = os.path.basename(ppath)
    conn_obj.sendall(os.path.split(ppath)[1].encode("utf8"))
    conn_obj.recv(1024)

    with open(ppath,"rb") as f:
        while file_size > 0:
            conn_obj.sendall(f.read(1024))
            file_size -= 1024
            print("--发送成功")

upath = r"D:\MyTest\Python3\Tmp\2019_08_Advanced\20190901_socket\2文件上传\客户端\picture.png"
post_file(usk,upath)
usk.close()



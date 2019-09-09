#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-03 and 15:35
FileName:20190903_并发服务器.py
Description：...
'''
import time, datetime

# 获取当前格式化-年月日：时分秒
nowTimee = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))

import socketserver

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        print("\n---- 多线程服务器已启动 ----")
        # 获取客户端ip地址和端口号
        while True:
            client_port = self.client_address
            print("--客户端ip信息：", client_port, "\n")
            while True:
                print("服务端接收到：\n", str(self.request.recv(1024), encoding="utf8"))
                print("服务器发送出：", self.request.sendall(bytes(input("服务器 >>>"), encoding="utf8")))
            self.request.close()

server = socketserver.ThreadingTCPServer(("127.0.0.1",18000),Myserver)
print("-- 服务器已上线 --")
server.serve_forever()

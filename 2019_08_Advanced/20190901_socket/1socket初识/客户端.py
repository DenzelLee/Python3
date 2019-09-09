# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/8/30


import socket

ip_port = ("127.0.0.1", 13000)

# 创建一个 socket 对象
sk = socket.socket()

# 连接服务器
sk.connect(("127.0.0.1", 13000))



send_data = input("请输入>>>")
# 发送数据，要编码encode（"utf8"）
sk.sendall(send_data.encode("utf8"))

# 接受数据,要解码decode（"utf8"）
client_data = sk.recv(1024)
print(client_data.decode("utf8"))


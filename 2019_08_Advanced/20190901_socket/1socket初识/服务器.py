# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/8/30


import socket

# ip地址和端口号
ip_port = ("127.0.0.1", 13000)

# 创建 socket 对象
sk = socket.socket()

# 绑定 ip 地址和端口号
sk.bind(ip_port)

# 监听， 看有没有请求过来
sk.listen(5) # 最多同时接受 5 个
print("服务端启动了")

# 等待传入连接
# 连接成功之后，返回一个新的 socket 对象，并且会返回客户端的 IP 地址和端口号
conn, adrr = sk.accept()
print("客户端的地址", adrr)
print("conn =", conn)


# 接受数据,要解码decode（"utf8"）
client_data = conn.recv(1024)
print(client_data.decode("utf8"))


send_data = input("请输入>>>")
# 发送数据,要编码encode（"utf8"）
conn.sendall(send_data.encode("utf8"))

# 释放资源
conn.close()
sk.close()

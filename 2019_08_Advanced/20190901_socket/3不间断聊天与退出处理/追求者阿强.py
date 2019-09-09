# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/8/30

import socket

sk = socket.socket()

sk.connect(("127.0.0.1", 13005))
print("追求者已上线")

while True:
    # 向女神发消息
    inp = input("请输入>>>")
    sk.sendall(inp.encode("utf8"))

    # 判断是不是想要退出
    if inp == "exit":break

    # 接受消息
    server_data = sk.recv(1024)
    print(server_data.decode("utf8"))


sk.close()


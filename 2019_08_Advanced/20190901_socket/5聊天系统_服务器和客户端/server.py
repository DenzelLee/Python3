# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/9/1


import socket

sk = socket.socket()

sk.bind(("127.0.0.1", 12000))

sk.listen(1)



def handle_data(data):
    # 先处理消息的第二部分
    if data == "natnaniel":
        data_type = "1"
    else:
        data_type = "2"


    # 处理消息的第一部分
    # 前面字段是4个字节的字符串，比如
    # '0008'，其内容是数字，表示消息的长度， 不足4个字节前面补零
    str_len = len(data) + 7
    if len(str(str_len)) < 4:
        str_len = "0"*(4 - len(str(str_len))) + str(str_len)
        data_len = str_len
    else:
        data_len = str(str_len)


    return "|".join([str(data_len), data_type, data])



while True:
    # 等待客户端连接
    conn, addr = sk.accept()

    # 客户端首先会表明身份
    client_name = conn.recv(1024).decode("utf8")
    print(client_name)
    # 告诉客户端，我已经知道你是谁了
    conn.sendall(handle_data("ok").encode("utf8"))


    while True:
        # 收消息
        client_data = conn.recv(1024).decode("utf8")
        print(client_data)

        # 发消息
        server_data = input(">>>")
        conn.sendall(handle_data(server_data).encode("utf8"))
    conn.close()


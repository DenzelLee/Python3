# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/9/1

# 实现
# 一个
# 简单的
# 客服聊天系统。
#
# 客服中心是tcp服务端程序
# 客户使用tcp客户端程序。
#
# 服务端程序
# 先运行， 绑定本机一个ip地址， 等待客户端系统连接上来 。
#
# 客户端程序有一个命令行参数， 表示客户的名字
#
# 连接成功后，  客户端发送给服务端第一个消息
# 必须告诉客服中心，用户的名字
#
# 一个客户连接后，别的客户不能连接， 等到前面的客户断开连接后，才能连上。
#
# 客户端和服务端都是手动在终端输入信息，发送消息后，必须等待接受到对方的消息才能发送下一个消息。
#
# 我们定义消息的格式如下：
# 000
# 8 | 1 | nickname
# 用竖线隔开3部分的字段，分别表示
# 消息长度、 消息类型 、消息内容
#
# 前面字段是4个字节的字符串，比如
# '0008'，其内容是数字，表示消息的长度， 不足4个字节前面补零。
# 注意长度是整个消息内容的长度，包括
# 消息头部和消息体
#
# 后面用竖线隔开的字段，是1个字节的字符串，是消息类型，其内容是数字，1
# 表示客户昵称， 2
# 表示
# 普通消息
#
# 前面两个字段合起来
# 000
# 8 | 1 |  ， 可以看成是一个消息的头部， nickname
# 是消息体
#
# 再后面用竖线隔开的字段是
# 消息内容，其长度等于
# 前面消息长度字段指明的长度
# 减去
# 消息头部长度 （也就是7个字节）

import socket

sk = socket.socket()

sk.connect(("127.0.0.1", 12000))

client_name = "natnaniel"

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

# 先自报家门
sk.sendall(handle_data(client_name).encode("utf8"))
sk.recv(1024)

while True:
    # 发消息
    server_data = input(">>>")
    sk.sendall(handle_data(server_data).encode("utf8"))

    # 收消息
    client_data = sk.recv(1024).decode("utf8")
    print(client_data)

sk.close()


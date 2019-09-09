# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/8/30

import socket, os

# 创建 socket 对象
sk = socket.socket()
# 绑定 ip 地址和端口号
sk.bind(("127.0.0.1", 13001))
# 监听(监听里面放代码块）
sk.listen(5)


def get_file(sk_obj):
    """
    接受文件
    :param sk_obj: socket 对象,有对象才可以发送和接受信息
    :return:
    """
    # 接受文件大小
    file_size = int(sk_obj.recv(1024).decode("utf8"))
    # 告诉对方，我已经收到文件大小了
    sk_obj.sendall("ok, 文件大小接受完毕".encode("utf8"))

    # 接受文件名字
    file_name = sk_obj.recv(1024).decode("utf8")
    # 告诉对方，我已经收到文件名字了
    sk_obj.sendall("ok, 文件名字受完毕".encode("utf8"))


    # 接受文件
    with open("./%s" %file_name, "wb") as f:
        while file_size > 0:
            f.write(sk_obj.recv(1024))
            file_size -= 1024


conn, addr = sk.accept()

get_file(conn)

# 释放资源
conn.close()
sk.close()

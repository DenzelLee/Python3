# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/8/30

# 建立连接
import os, socket
sk = socket.socket()
sk.connect(("127.0.0.1", 13001))

# 定义文件格式
def post_file(sk_obj, file_path):
    """
    上传文件
    :param sk_obj:  socket 对象，有对象才可以发送和接受信息
    :param file_path:  文件的路径
    :return:
    """
    # 发送文件大小
    file_size = os.stat(file_path).st_size
    sk_obj.sendall(str(file_size).encode("utf8"))
    sk_obj.recv(1024)

    # 发送文件的名称
    sk_obj.sendall(os.path.split(file_path)[1].encode("utf8"))

    sk_obj.recv(1024)

    # 发送文件内容
    with open(file_path, "rb") as f:
        while file_size > 0:
            sk_obj.sendall(f.read(1024))
            file_size -= 1024

path = r"D:\MyTest\Python3\Tmp\2019_08_Advanced\20190901_socket\2文件上传\客户端\\picture.png"
post_file(sk, path)


sk.close()

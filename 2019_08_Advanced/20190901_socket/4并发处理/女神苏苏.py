# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/8/30

import socketserver

class MyClass(socketserver.BaseRequestHandler):
    def handle(self):
        print("有人和女神搭讪了:", self.client_address) # 客户端的 ip 地址和端口号
        while True:
            # 接受数据
            client_data = self.request.recv(1024)  # conn.recv(1024)
            print(client_data.decode("utf8"))

            # 发送数据
            self.request.sendall(input("请输入").encode("utf8"))

        self.request.close()



server = socketserver.ThreadingTCPServer(("127.0.0.1", 18100), MyClass)
server = socketserver.ThreadingUDPServer(("127.0.0.1", 18100), MyClass)

print("女神上线了......")
# 调用服务
server.serve_forever()

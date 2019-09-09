#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-30 and 18:32
FileName:20190830_多线程读取网页内容.py
Description：...
'''
import time,threading,requests
from pprint import pprint

# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

text_str = ""
# 2019豆瓣热门电视剧
url1 = "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0"
# 2019豆瓣热门新片
url2 = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0"
# 创建锁对象
lock = threading.Lock()

# 定义线程函数
def addshread(num,url):
    global text_str
    print("\n----开始启动线程%s号----\n" %(num))

    # 涉及到重要数据操作，上锁，资源只允许1号线程使用
    lock.acquire()
    print("\n--%s号线程，已上锁" %(num))

    # 通过接口抓取电影名称/平凡/地址
    re_text = requests.get(url=url)
    re_text = re_text.json()
    count = 1
    for i in re_text["subjects"]:
        print(f"{count:0>2}.Title：--{i['title']:<5}\nRate：{i['rate']:<5}\nUrl：{i['url']}")
        count += 1

    # ---释放资源：解锁，资源转给2号线程使用
    lock.release()
    print("\n--%s号线程，已解锁" %(num))

if __name__ == '__main__':
    t1 = threading.Thread(target=addshread, args=("1", url1))
    t2 = threading.Thread(target=addshread, args=("2", url2))

    t1.start(), t1.join(), t2.start(), t2.join()







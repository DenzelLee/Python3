# usr/bin/python3
# -*- coding:utf-8 -*-
'''
Auther:leo
Date:${DATE} and ${TIME}
File:${FILENAME}
Other:...
'''
'''
要求：
打开百度新歌榜， http://music.baidu.com/top/new
在排名前50的歌曲中，找出其中排名上升的歌曲和演唱者
注意： 有的歌曲名里面有 "影视原声" 这样的标签， 要去掉
最终结果显示的结果如下：
我不能忘记你       :  林忆莲
等                :  严艺丹
'''
from selenium import webdriver
driver = webdriver.Chrome(r"F:\MyTest\WebDriver\chromedriver.exe")
driver.get("http://music.baidu.com/top/new")
alert = driver.find_elements_by_id("__qianqian_pop_closebtn")
if alert:
    alert[0].click()
ele = driver.find_element_by_id("songListWrapper").\
    find_elements_by_class_name("song-item")
for i in ele:
    # print(i.text)
    dir = i.find_element_by_class_name("status").\
    find_element_by_tag_name("i").get_attribute("class")
    if dir == "up":
        name = i.find_element_by_css_selector(".song-title").text
        auther = i.find_element_by_css_selector(".singer").text
        print(f"songName:{name},Auther{auther}")








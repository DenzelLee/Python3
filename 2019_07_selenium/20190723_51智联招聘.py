# usr/bin/python3
# -*- coding:utf-8 -*-
'''
Auther:leo
Date:2019-07-23 and 21:47
File:
Other:...
'''
'''
登录 51job ，http://www.51job.com
输入搜索关键词 "python"， 地区选择 "杭州"（注意，如果所在地已经选中其他地区，要去掉）， 
搜索最新发布的职位， 抓取页面信息。 得到如下的格式化信息
Python开发工程师 | 杭州纳帕科技有限公司 | 杭州 | 0.8-1.6万/月 | 04-27
Python高级开发工程师 | 中浙信科技咨询有限公司 | 杭州 | 1-1.5万/月 | 04-27
高级Python开发工程师 | 杭州新思维计算机有限公司 | 杭州-西湖区 | 1-1.5万/月 | 04-27
'''
from selenium import webdriver
driver = webdriver.Chrome(r"F:\MyTest\WebDriver\chromedriver.exe")
driver.implicitly_wait(1)
driver.get('http://www.51job.com')
driver.find_element_by_id("kwdselectid").send_keys("python")
driver.find_element_by_id("work_position_input").click()
eles = driver.find_element_by_id("work_position_click_center_right_list_000000").find_elements_by_tag_name("em")
for i in eles:
    city = i.text
    status = i.get_attribute("class")
    if status == r"on" and city != r"杭州":
        i.click()
    elif status != r"on" and city == r"杭州" :
        i.click()
driver.find_element_by_id("work_position_click_bottom_save").click()
driver.find_element_by_xpath('''//button[@onclick="kwdGoSearch($('#kwdselectid').val());"]''').click()
eless = driver.find_elements_by_css_selector('#resultList div.el')
# print(eless)
for j in eless:
    job = j.find_element_by_class_name("t1").text
    addr = j.find_element_by_class_name("t2").text
    money = j.find_element_by_class_name("t3").text
    cdate = j.find_element_by_class_name("t4").text
    print(f"{job}|{addr}|{money}|{cdate}")


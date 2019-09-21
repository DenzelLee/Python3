#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-20 and 13:38
FileName:20190920_08_爬取测试开发信息.py
Description：...
第八题
请写一个程序，访问https://www.51job.com/
抓取关键字：测试开发，地点南京的工作中，前3页的职位中，月薪在15000元以上的工作
'''
from selenium import webdriver
from pprint import pprint
from time import sleep
import datetime, time
import re

# 获取当前格式化-年月日：时分秒
nowTimee = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.51job.com/")

# 输入搜索关键字
driver.find_element_by_id("kwdselectid").send_keys("测试开发")
driver.find_element_by_id("work_position_input").click()
sleep(1)

# 循环删除已选地区
while True:
    eles = driver.find_elements_by_css_selector("*[id='work_position_click_multiple_selected']>span")
    if eles == []:
        break
    else:
        for i in eles:
            i.click()
# 点击南京
driver.find_element_by_id("work_position_click_center_right_list_category_000000_070200").click()
sleep(0.5)

# 点击确定
driver.find_element_by_id("work_position_click_bottom_save").click()
sleep(1)

# 点击搜索按钮
driver.find_element_by_css_selector("""[onclick="kwdGoSearch($('#kwdselectid').val());"]""").click()

# 获取页码
pages = driver.find_elements_by_css_selector('.p_in>ul>li')
count = 1
sum = 1
# 循环获取4页信息
while count<=(len(pages)-2):
    # 获取招聘列表信息
    reslists = driver.find_elements_by_css_selector('#resultList>div.el')

    # 循环检查薪资待遇
    for i in reslists[3:]:
        money = i.find_element_by_css_selector("span.t4").text
        name = i.find_element_by_css_selector("a").text
        if money:
            # 字符串获取中文
            mmoney = re.findall("[\u4e00-\u9fa5]+", money)
            # 字符串获取数字
            nmoney = re.findall(r"\d+\.?\d*", money)
            # print(mmoney, nmoney)
            if '万' in mmoney and '月' in mmoney:
                if float(nmoney[0]) >= 1.5 or float(nmoney[1]) >= 1.5:
                    print(f"\n{sum}.高薪工作（15000）：{i.text}\n")
                    sum += 1
    count += 1
    # 点击下一步翻页按钮
    driver.find_element_by_xpath('//li[@class="bk"]/following-sibling::li[last()]').click()


# --结果：
'''
1-34...
35.高薪工作（15000）：芯片平台测试Leader
南京地平线机器人技术有限公司
异地招聘
1.5-3万/月
09-20

36.高薪工作（15000）：算法测试工程师
南京烽火星空通信发展有限公司
南京-建邺区
1-2万/月
09-20

37.高薪工作（15000）：测试工程师（功能测试） (MJ000591)
SHEIN
南京-雨花台区
1.2-1.8万/月
09-19

38.高薪工作（15000）：软件测试（外派中国移动）
南京绛门信息科技股份有限公司
南京-建邺区
0.9-1.5万/月
09-17

Process finished with exit code 0
'''
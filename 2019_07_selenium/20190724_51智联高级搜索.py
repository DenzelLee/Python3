#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-07-26 and 22:20
FileName:20190726_51job高级搜索
Description：Webdriver.自学练习题
'''
'''
题目：
1.登录 http://www.51job.com
2.点击高级搜索
3.输入搜索关键词 软件测试
4.地区选择 成都
5.职能类别 选 计算机软件 -> 软件测试工程师
6.公司性质选 民营公司
7.工作年限选 5-10年

结果：
搜索最新发布的职位，爬取页面信息，打印如下的格式化信息：
Python开发工程师 | 杭州纳帕科技有限公司 | 杭州 | 0.8-1.6万/月 | 04-27
Python高级开发工程师 | 中浙信科技咨询有限公司 | 杭州 | 1-1.5万/月 | 04-27
'''
# 第一步：导入需要用到的库和包（置灰表示没有用到，变色表示成功调用）
from selenium import webdriver
from time import sleep

# 第二步：实例化web驱动器
driver = webdriver.Chrome()
driver.implicitly_wait(1)

# 第三步：打开URL目标链接地址
driver.get("http://www.51job.com")

# 第四步：开始定位元素
driver.find_element_by_css_selector(".more").click()

driver.find_element_by_id("work_position_input").click()

alreadyCitys = driver.find_elements_by_css_selector("#work_position_click_multiple span")

# 第五步：删除已经选中的热门城市
for aCity in alreadyCitys:
    aCity.click()
chengDu = driver.find_element_by_id("work_position_click_center_right_list_category_000000_090200")

# 第六步：新增所在地-成都市
if chengDu.text == r"成都":
    chengDu.click()
sleep(1)
driver.find_element_by_id("work_position_click_bottom_save").click()

# 第七步：输入工作关键字-软件测试
driver.find_element_by_xpath("//input[@id='kwdselectid']").send_keys("软件测试")
sleep(1)
driver.find_element_by_css_selector("div.c_h label").click()
sleep(1)

# 职能搜索
driver.find_element_by_id("funtype_click").click()
sleep(1)
driver.find_element_by_id("funtype_click_center_right_list_category_0100_2700").click()
sleep(1)
driver.find_element_by_id("funtype_click_center_right_list_sub_category_each_0100_2705").click()
driver.find_element_by_id("funtype_click_center_right_list_sub_category_each_0100_2706").click()
driver.find_element_by_id("funtype_click_center_right_list_sub_category_each_0100_2707").click()
driver.find_element_by_id("funtype_click_center_right_list_sub_category_each_0100_2708").click()
driver.find_element_by_id("funtype_click_center_right_list_sub_category_each_0100_2709").click()
driver.find_element_by_id("funtype_click_bottom_save").click()
sleep(1)

# 行业类别
driver.find_element_by_id("indtype_click").click()
driver.find_element_by_id("indtype_click_center_right_list_category_01_01").click()
driver.find_element_by_id("indtype_click_bottom_save").click()
sleep(1)

# 公司性质
driver.find_element_by_id("cottype_list").click()
driver.find_element_by_css_selector("[title='民营公司']").click()
sleep(1)

# # 工作年限
# driver.find_element_by_id("workyear_list").click()
# driver.find_element_by_css_selector("#workyear_list span.li[title='5-10年']").click()
# sleep(1)

# 月薪范围
driver.find_element_by_id("providesalary_list").click()
driver.find_element_by_css_selector("span.li[title='1-1.5万']").click()
sleep(1)

# # 公司规模
# driver.find_element_by_id("companysize_list").click()
# driver.find_element_by_css_selector("span.li[title='50-150人']").click()
# sleep(1)
#
# # 学历要求
# driver.find_element_by_id("degreefrom_list").click()
# driver.find_element_by_css_selector("span.li[title='本科']").click()
# sleep(1)
#
# # 工作类型
# driver.find_element_by_id("jobterm_list").click()
# driver.find_element_by_css_selector("span.li[title='全职']").click()
# sleep(1)
#
# 点击搜索
sleep(3)
driver.find_element_by_css_selector("div.p_sou span.p_but").click()


# 爬取招聘信息打印
sleep(3)
jobLists = driver.find_elements_by_css_selector("#resultList div[class='el']")
count = 0
for i in jobLists:
    jobStr = i.find_elements_by_css_selector("span")
    count +=1
    print(f"{count}."+"|".join(job.text for job in jobStr))


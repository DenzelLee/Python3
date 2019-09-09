#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-07-27 and 12:22
FileName:12306_成都到重庆
Description：...
'''
'''
场景：
1.打开12306官方订票网站：https://kyfw.12306.cn/otn/leftTicket/init
2.出发城市填写 ‘成都东’，到达城市填写 ‘重庆北’ 
（陷阱1：注意输入城市名前，一定要先点击一下输入框，否则查不到） 
（陷阱2：输入城市名最后要包含一个回车符，否则输入框里面会自动清除）
3.发车时间选 06:00--12:00。（可以用Select类通过下标选取，也可以用Xpathposition()方法选取）
4.发车日期选 当前时间的下一天，也就是日期标签栏的，第二个标签。（可以用CSS-#date_range li:nth-child(2)直接选取，也可以用xpath遍历选取）

我们要查找的是所有 二等座还有票的车次，打印出这些有票的车次的信息（这里可以用xpath），结果如下：
1:D2244|成都东|重庆北|06:43|08:52|02:09|当日到达
2:G2371|成都东|重庆西|07:03|08:27|01:24|当日到达


'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# 实例化浏览器驱动
driver = webdriver.Chrome()
driver.get("https://kyfw.12306.cn/otn/leftTicket/init")
driver.implicitly_wait(3)
sleep(3)

# 出发站
driver.find_element_by_id("fromStationText").click()
driver.find_element_by_id("fromStationText").send_keys("成都东")
# 模拟键盘操作：回车键
driver.find_element_by_id("fromStationText").send_keys(Keys.ENTER)

# 终点站
driver.find_element_by_id("toStationText").click()
driver.find_element_by_id("toStationText").send_keys("重启北")
driver.find_element_by_id("toStationText").send_keys(Keys.ENTER)

# 出发日期-逻辑运算符and多元素定位
driver.find_element_by_xpath("//input[@id='train_date' and @class='inp_selected']").click()
calLeft = driver.find_elements_by_css_selector("div.cal-wrap>div.cal div.cal-cm>div")
count, now = 0, 0
for date in calLeft:
    count += 1
    if date.text == r"今天":
        now = count
        print(f"{date.text}是当月第{count}天，我将买明天的车票。")
    if count == now+1:
        date.click()

# 日期选择用法2：通过切换日期列表，选择第二个日期tomorrow，自动搜索车票
# tomorrow = driver.find_element_by_css_selector('#date_range li:nth-child(2)')


# 出发时间：06：00-12：00
driver.find_element_by_id("cc_start_time").click()
sleep(1)
driver.find_element_by_xpath("//select[@id='cc_start_time']/option[position()=3]").click()
sleep(1)

# 出发时间用法2：导入Select，通过下拉框选择出发时间的用法
# timeSelect =  Select(driver.find_element_by_id('cc_start_time'))
# timeSelect.select_by_visible_text('06:00--12:00')


# 点击查询
driver.find_element_by_id("query_ticket").click()
sleep(3)

# 打印结果
# trainNums = driver.find_elements_by_xpath("//div[@id='t-list']/table/tbody[@id='queryLeftTable']/tr")
# 高级判断：二等座td[4]加上[@class]，判断如果有票，就有class属性，没有票就没有class属性，子路径选中第一个td，牛逼！
trainNums = driver.find_elements_by_xpath("//*[@id='queryLeftTable']//td[4][@class]/../td[position()<2]")
num = 0
for train in trainNums:
    new = str(train.text).replace("\n"," | ")
    num +=1
    print(f"{num:<2}:{new}")


# 关闭浏览器（上次忘掉这个，导致电脑卡到飞起）
sleep(5)
driver.close()

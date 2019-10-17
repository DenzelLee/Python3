#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-25 and 12:32
FileName:
Description：...
'''
from selenium import webdriver
from time import sleep
from pprint import pprint
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(r"D:\TestFiles\Python3\chromedriver.exe")
driver.implicitly_wait(30)
driver.get(r"http://s.dianping.com/event/chengdu")
sleep(1)
driver.find_element_by_css_selector(".J-bonus-close").click()
more = driver.find_element_by_xpath("//a[@class='load-more show']")
mores = more.get_attribute("class")
addList = ['春熙路', '牛市口', '万达广场', '九眼桥']
addStr = "双人"
successList = []
failList = []

# 主窗口柄和标题
mainWindows = driver.current_window_handle
mainTitle = driver.title
print(f"\n---- 1.Welcome，欢迎进入霸王餐首页：{mainTitle} ----\n")
sleep(5)

# 加载更多
more = driver.find_element_by_css_selector(".load-more.show")
# print(more)
try:
    while True:
        if more.get_attribute("class") == r"load-more show":
            print(f"-- 点击加载更多成功，请稍等片刻！--")
            more.click()
            sleep(1)
        elif more.get_attribute("class") == r"load-more":
            print("\n---- 2.Success！霸王餐信息已全部加载完毕！开始循环获取商铺信息----\n")
            break
except:
    print("-- 点击加载更多失败，请检查！--")
count = 0
menus = driver.find_elements_by_css_selector(".activity-lists-wraper li")
for i in menus[:]:
    url = i.find_element_by_css_selector("a")
    storeUrl = i.find_element_by_css_selector("a").get_attribute("href")
    storeName = i.find_element_by_css_selector("h4").text
    storeAddr = i.find_element_by_css_selector("div.addi>span.addr").text
    count +=1
    # if storeAddr in addList:
    #     print(f"{count:<3}.附近商家姓名：{storeName} || 地址：{storeAddr} || 链接：{storeUrl}")
    if r"券" not in storeName and (addStr in storeName or r"双人" in storeName):
        print(f"{count:<3}.商家姓名：{storeName} || 地址：{storeAddr} || 链接：{storeUrl}")
        url.click()

        # 跳转新窗口
        for window in driver.window_handles:
            driver.switch_to.window(window)
            if window != mainWindows:
                break
                #--
        sleep(1.5)
        button = driver.find_element_by_css_selector(".btn-txt.J_self_apply")
        # print(f"新标签页面按钮为：{button.text}")
        sleep(1.5)
        button.click()
        sleep(5)# 手动登录时间!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        try:
            # abert = driver.find_element_by_css_selector(".pop-main")
            # print(f"新标签页面弹框为：{abert.text}")
            # abert.click()
            driver.find_element_by_css_selector("#J_pop_ok").click()
            sleep(1)
            abert1 = driver.find_element_by_css_selector(".pop-main .col.tit")
            print(f"\n报名成功页面弹框为：{abert1.text}\n")
            sleep(1)
            # 关闭弹窗
            driver.find_element_by_css_selector(".hd a.close").click()
            sleep(1.5)
            successList.append(f"{count}.{storeName}|{storeUrl}")
        except Exception as e:
            print(e)
            print(f"报名异常，请人工检查连接地址：{count}.{storeName}:{storeUrl}\n")
            failList.append(f"{count}.{storeName}|{storeUrl}")
        finally:
            # 关闭新标签
            driver.close()


        # 切回主窗口
        driver.switch_to.window(mainWindows)
        # print(f"{count}.{storeName}店铺报名成功，成功回到主窗口：{driver.title}")
print(f"报名成功店铺总数：{len(successList)}")
for sucess in  successList:
    print(f"\n---- 3.店铺详情：{sucess} ----\n")

print(f"报名失败店铺总数：{len(failList)}")
for fail in  failList:
    print(f"\n---- 4.店铺详情：{fail} ----\n")

driver.close()

# print(f"报名成功的店铺：{len(successLsit)}{successLsit}")
# print(f'报名失败的店铺：{len(failList)}{failList}')



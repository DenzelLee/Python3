#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-07-28 and 10:02
FileName:20190728_华为官网二级菜单悬停和窗口切换.py
Description：...
'''
'''
-- 情景CSS定位、悬停、校验
1.登录华为官网 https://www.vmall.com/， 
2.点击 "华为官网" 链接
3.检查 "华为官网" 页面上是否 有如下主菜单：智能手机/笔记本/平板/穿戴设备/智能家居/更多产品/软件应用/服务与支持
4.最后再回到主窗口， 检查鼠标停留在 "笔记本&平板" 处的时候， 是否显示的菜单有："平板电脑  笔记本电脑 笔记本配件"
5.模拟悬停操作，打印二级菜单信息
'''
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.vmall.com/")

# 获取当前窗口句柄
mainHandle = driver.current_window_handle
driver.implicitly_wait(5)

# 点击华为官网链接跳转
driver.find_element_by_xpath("//div[@class='s-sub']//li[2]/a").click()
sleep(3)
driver.maximize_window()

# 获取所有窗口句柄
allHandles = driver.window_handles
print("主窗口为："+driver.title)

# 切换浏览器窗口
for handle in allHandles:
    driver.switch_to.window(handle)
    if "华为消费者业务官网" in driver.title: # --这里要用driver.title，不用带括号（）
        # driver.switch_to_window(i) # --这个新版本已经废弃，需要用driver.switch_to.window(i)
        print("新窗口为: "+driver.title)
        break
# menuTops = driver.find_elements_by_css_selector(".left-box .clearfix.nav-cnt li")  # --css用法
menuTops = driver.find_elements_by_xpath("//div[@class='left-box']//ul[@class='clearfix nav-cnt']/li")
menuList = []
for j in menuTops:
    menuName = j.find_element_by_tag_name("a").text
    menuList.append(menuName)

# 检查点
chckin = "智能手机/笔记本/平板/穿戴设备/智能家居/更多产品/软件应用/服务与支持"
menuList = "/".join(menuList)
print(f"\n当前菜单为：\n{menuList}")
if chckin ==menuList:
    print("\nPass the testCase!----------:\n{chckin}\n{menuList}")
else:
    print(f"\nFail the testCase!----------:\n{chckin}\n{menuList}")

# 切回主窗口
for handle2 in allHandles:
    driver.switch_to.window(handle2)
    if handle2 == mainHandle:
        print(f"\n欢迎回到主窗口：{driver.title}")
        break


# 导入鼠标悬停类
from selenium.webdriver import ActionChains

# 定位鼠标悬停位置
sleep(3)
mouseAddr = driver.find_element_by_css_selector("#zxnav_1")

# 悬停到目标区域
ActionChains(driver).move_to_element(mouseAddr).perform()

# 定位目标子区域并打印信息
mouseMenus = driver.find_elements_by_css_selector("#zxnav_1 div.category-panels.category-panels-1 li span")
print("\n悬停打印开始:")
mainMenu = "/".join([m.text for m in mouseMenus])
print(mainMenu+"\n")

# 检查点
check2 = "平板电脑/笔记本电脑/笔记本配件"
if mainMenu == check2:
    print(f"Pass the testCase!----------\n{check2}\n{mainMenu}")
else:
    print(f"Fail the testCase!---------- Please check your daima:\n{check2}\n{mainMenu}")

driver.quit()
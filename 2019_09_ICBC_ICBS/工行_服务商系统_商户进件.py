#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-07 and 14:34
FileName:工行_服务商系统_商户进件.py
Description：...
'''
from selenium import webdriver
from time import sleep
import win32com.client

# 服务商系统-商户进件
def Merchant():
    # 打开浏览器
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    # 开始登陆
    driver.get("http://icbc-isv.wangtest.cn/pp/user/login")
    driver.find_element_by_id("login_name").clear()
    driver.find_element_by_id("login_name").send_keys("18583993001")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("123456")

    # 手动登录（延时10秒）
    sleep(10)
    y, m, d, i, a = "2019","08","06","3","2"
    b = u"二"
    c = u"昆明市"
    print("----开始新建服务商----")
    driver.get("http://icbc-isv.wangtest.cn/pp/merchant/inquiry")
    sleep(5)

    # 点击新建商户按钮
    driver.find_element_by_xpath("//button[@type='button']").click()
    sleep(3)
    # file_path = os.path.abspath('./files/')
    # upload_page = 'file:///'+file_path+'http://icbc-isv.wangtest.cn/pp/merchant/create'
    # driver.get(upload_page)
    #
    # # 定位上传按钮，添加本地文件
    # driver.find_element_by_id("file").send_keys(file_path+'1营业执照.jpg')
    driver.maximize_window()


    # 上传图片
    driver.find_element_by_xpath("//*[@id='business_license_photo']/..").click()
    sleep(3)
    shell = win32com.client.Dispatch("WScript.Shell")
    sleep(1)
    shell.Sendkeys(r"D:\picture\1yyzz.jpg" + "\r\n")

    driver.find_element_by_xpath("//*[@id='lawyer_cert_photo_front']/..").click()
    sleep(3)
    shell = win32com.client.Dispatch("WScript.Shell")
    sleep(1)
    shell.Sendkeys(r"D:\picture\2sfz1.jpg" + "\r\n")

    driver.find_element_by_xpath("//*[@id='lawyer_cert_photo_back']/..").click()
    sleep(3)
    shell = win32com.client.Dispatch("WScript.Shell")
    sleep(1)
    shell.Sendkeys(r"D:\picture\3sfz2.jpg" + "\r\n")

    # 输入营业执照名称
    driver.find_element_by_id("business_license_name").click()
    driver.find_element_by_id("business_license_name").clear()
    driver.find_element_by_id("business_license_name").send_keys(c, u"个体对公", m, d, i, a, u"号")
    driver.find_element_by_xpath("//*[@type='radio'][@value='1']").click()

    # 行业类型
    driver.find_element_by_id("industry_code").click()
    sleep(0.5)
    driver.find_element_by_xpath("//*[@title='购物']").click()
    sleep(0.5)
    driver.find_element_by_xpath("//*[@title='文化用品、钟表眼镜批发业']").click()
    sleep(0.5)

    # 营业执照号码
    driver.find_element_by_id("business_license_code").click()
    driver.find_element_by_id("business_license_code").clear()
    driver.find_element_by_id("business_license_code").send_keys("2019", m, d, "090", i, "00000", a)

    # 营业执照有效期至
    driver.find_element_by_xpath("//*[@title='营业执照有效期至']/../following-sibling::div[1]").click()
    sleep(0.5)
    driver.find_element_by_css_selector("a[title='下一年 (Control键加右方向键)']").click()
    sleep(0.5)
    driver.find_element_by_css_selector(".ant-calendar-tbody td:nth-child(1)").click()
    sleep(0.5)

    # 注册省/市区
    driver.find_element_by_xpath("//*[@title='注册省/市/区']/../following-sibling::div[1]").click()
    sleep(0.5)
    driver.find_element_by_css_selector(".ant-cascader-menus.ant-cascader-menus-placement-bottomLeft li[title='云南省']").click()
    sleep(0.5)
    driver.find_element_by_css_selector(".ant-cascader-menus.ant-cascader-menus-placement-bottomLeft li[title='昆明市']").click()
    sleep(0.5)
    driver.find_element_by_css_selector(".ant-cascader-menus.ant-cascader-menus-placement-bottomLeft li[title='盘龙区']").click()
    sleep(0.5)

    # 注册详细地址
    driver.find_element_by_css_selector(".ant-form-item-children>#address").send_keys(u"注册详细地址", c)

    # 输入注册资本（万元）
    driver.find_element_by_id("reg_capital").click()
    driver.find_element_by_id("reg_capital").clear()
    driver.find_element_by_id("reg_capital").send_keys("100")

    # 门店名称
    driver.find_element_by_id("st_store_name").send_keys(u"门店名称航空", c)

    # 门店经营地址
    driver.find_element_by_xpath("//*[@title='门店经营地址']/../following-sibling::div[1]").click()
    sleep(0.5)
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='贵州省'])[2]/following::li[1]").click()
    sleep(1)
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='香港'])[2]/following::li[1]").click()
    sleep(1)
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='其他'])[3]/following::li[1]").click()
    sleep(1)

    # 门店经营详细地址
    driver.find_element_by_id("st_address_detail").click()
    driver.find_element_by_id("st_address_detail").clear()
    driver.find_element_by_id("st_address_detail").send_keys(u"门店经营地址", c)
    # 业务受理部门

    # 法定代表人姓名
    driver.find_element_by_id("name").click()
    driver.find_element_by_id("name").clear()
    driver.find_element_by_id("name").send_keys(u"法人代表李", b)

    # 证件类型
    # driver.find_element_by_css_selector(".ant-select-selection-selected-value").click()
    # sleep(0.5)
    # driver.find_element_by_css_selector(".ant-select-dropdown-menu-item ant-select-dropdown-menu-item-selected").click()

    # 证件号码
    driver.find_element_by_id("id_card_no").clear()
    driver.find_element_by_id("id_card_no").send_keys("1101011990010", i, "930", a)

    # 证件有效期
    driver.find_element_by_xpath("//*[@title='证件有效期至']/../following-sibling::div[1]").click()
    sleep(0.5)
    driver.find_element_by_css_selector("[title='下一年 (Control键加右方向键)']").click()
    sleep(0.5)
    driver.find_element_by_css_selector(".ant-calendar-active-week>td:nth-child(1)").click()

    # 联系人姓名/电话/邮箱
    driver.find_element_by_id("lawyer_phone").click()
    driver.find_element_by_id("lawyer_phone").clear()
    driver.find_element_by_id("lawyer_phone").send_keys("18583998081")

    driver.find_element_by_id("contact_person").click()
    driver.find_element_by_id("contact_person").clear()
    driver.find_element_by_id("contact_person").send_keys(c, u"个体联系人", a, u"号")

    driver.find_element_by_id("contact_phone").clear()
    driver.find_element_by_id("contact_phone").send_keys("1858399", i, "00", a)
    driver.find_element_by_id("contact_email").clear()
    driver.find_element_by_id("contact_email").send_keys("270981551@qq.com")

    # 点击提交
    driver.find_element_by_css_selector(".ant-btn.ant-btn-primary").click()
    sleep(3)
    print(f"----1.第一页信息提交成功！----")

    # 结算账户类型：企业对公账户1，法人对私账户2
    driver.find_element_by_css_selector(".ant-radio-input[value='1']")

    # 开户许可证图片
    driver.find_element_by_xpath("//*[@id='account_opening_license']/..").click()
    sleep(3)
    shell = win32com.client.Dispatch("WScript.Shell")
    sleep(1)
    shell.Sendkeys(r"D:\picture\4khxkz1.jpg" + "\r\n")


    # 开户银行
    driver.find_element_by_xpath("//*[@title='开户银行']/../following-sibling::div[1]").click()
    sleep(1)
    driver.find_element_by_xpath(u"//li[contains(text(),'中国工商银行')]").click()
    sleep(1)

    # 支行
    driver.find_element_by_xpath("//*[@class='antd-pro-pages-merchant-create-style-titleLayout']/../../following-sibling::div[1]").click()
    sleep(1)
    # driver.find_element_by_xpath("//input[contains(@id,'open_sub_bank')]").clear()
    # sleep(0.5)
    # driver.find_element_by_xpath("//input[contains(@id,'open_sub_bank')]").send_keys(u"春熙路")
    # sleep(0.5)
    driver.find_element_by_xpath(u"//li[contains(text(),'中国工商银行朝阳建平支行')]").click()
    sleep(1)

    # 账户号
    driver.find_element_by_id("account_no").click()
    driver.find_element_by_xpath("//input[@id='account_no']").clear()
    driver.find_element_by_xpath("//input[@id='account_no']").send_keys("6212260521", m, d, i, i, "00", a)

    # 手机号
    driver.find_element_by_id("reserve_phone").click()
    driver.find_element_by_id("reserve_phone").clear()
    driver.find_element_by_id("reserve_phone").send_keys("18583998081")

    # 提交按钮
    driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
    print(f"----2.第二页信息提交成功! ----")

    # 支付宝费率
    driver.find_element_by_id(u"Alipay-支付宝").click()
    driver.find_element_by_id(u"Alipay-支付宝").clear()
    driver.find_element_by_id(u"Alipay-支付宝").send_keys("0.11")

    # 微信费率
    driver.find_element_by_id(u"WechatPay-微信支付").click()
    driver.find_element_by_id(u"WechatPay-微信支付").clear()
    driver.find_element_by_id(u"WechatPay-微信支付").send_keys("0.21")

    # 银联二维码费率
    driver.find_element_by_id(u"UnionPay_QR-银联二维码-2").click()
    driver.find_element_by_id(u"UnionPay_QR-银联二维码-2").clear()
    driver.find_element_by_id(u"UnionPay_QR-银联二维码-2").send_keys("0.31")
    driver.find_element_by_id(u"UnionPay_QR-银联二维码-1").click()
    driver.find_element_by_id(u"UnionPay_QR-银联二维码-1").clear()
    driver.find_element_by_id(u"UnionPay_QR-银联二维码-1").send_keys("0.41")

    # 银联封顶额度金额
    driver.find_element_by_id(u"UnionPay_QR-银联二维码-1-rag_fee_max").click()
    driver.find_element_by_id(u"UnionPay_QR-银联二维码-1-rag_fee_max").clear()
    driver.find_element_by_id(u"UnionPay_QR-银联二维码-1-rag_fee_max").send_keys("1100")

    # 第三页信息提交按钮
    driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
    print(f"----3.第三页信息提交成功！----")
    input("Please input anykes continue doing testCase...")
    sleep(3)
    driver.close()

    # 打印成功页面信息
    stores = driver.find_elements_by_css_selector(".antd-pro-components-testFile-index-testFile>div")
    count1 = 0
    for i in  stores:
        count1 +=1
        print(f"{count1}.提交状态：",i.text)
        print(f"{count1}.营业执照名称：",i.text)
        print(f"{count1}.营业执照号码	：",i.text)
        print(f"{count1}.业务受理部门：",i.text)
        print(f"{count1}.申请单号：",i.text)

Merchant()









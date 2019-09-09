#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-07 and 13:56
FileName:工行_服务商系统_商户进件框架.py
Description：...
'''
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class CreateStore(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_(self):
        driver = self.driver
        y = "2019"
        m = "08"
        d = "06"
        i = "3"
        a = "2"
        b = u"二"
        c = u"昆明市"
        # ERROR: Caught exception [ERROR: Unsupported command [while | ${i}<50 | ]]
        print(i)
        driver.get("http://icbc-isv.wangtest.cn/pp/merchant/inquiry")
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_id("business_license_name").click()
        driver.find_element_by_id("business_license_name").clear()
        driver.find_element_by_id("business_license_name").send_keys(c, u"个体对公", m, d, i, a, u"号")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='经营类型'])[1]/following::input[1]").click()
        driver.find_element_by_id("industry_code").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='版本'])[1]/following::li[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='教育培训'])[1]/following::li[1]").click()
        driver.find_element_by_id("business_license_code").click()
        driver.find_element_by_id("business_license_code").clear()
        driver.find_element_by_id("business_license_code").send_keys("2019", m, d, "090", i, "00000", a)
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='营业执照有效期至'])[1]/following::input[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='版本'])[1]/following::a[7]").click()
        driver.find_element_by_xpath("(//div[@class='ant-calendar-date'][contains(.,'1')])[1]").click()
        driver.find_element_by_id("reg_capital").click()
        driver.find_element_by_id("reg_capital").clear()
        driver.find_element_by_id("reg_capital").send_keys("100")
        driver.find_element_by_css_selector("i.anticon.anticon-down.ant-cascader-picker-arrow > svg").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='版本'])[1]/following::li[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='教育培训'])[1]/following::li[1]").click()
        driver.find_element_by_css_selector("i.anticon.anticon-down.ant-cascader-picker-arrow > svg").click()
        driver.find_element_by_id("province_city").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='贵州省'])[1]/following::li[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='香港'])[1]/following::li[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='其他'])[1]/following::li[1]").click()
        driver.find_element_by_id("address").click()
        driver.find_element_by_id("address").clear()
        driver.find_element_by_id("address").send_keys(u"注册详细地址", c)
        driver.find_element_by_id("st_store_name").click()
        driver.find_element_by_id("st_store_name").clear()
        driver.find_element_by_id("st_store_name").send_keys(u"门店名称航空", c)
        driver.find_element_by_id("store_city").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='贵州省'])[2]/following::li[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='香港'])[2]/following::li[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='其他'])[3]/following::li[1]").click()
        driver.find_element_by_id("st_address_detail").click()
        driver.find_element_by_id("st_address_detail").clear()
        driver.find_element_by_id("st_address_detail").send_keys(u"门店经营地址", c)
        driver.find_element_by_id("name").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(u"法人代表李", b)
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='证件类型'])[1]/following::div[5]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='身份证'])[1]/following::div[1]").click()
        driver.find_element_by_id("id_card_no").clear()
        driver.find_element_by_id("id_card_no").send_keys("1101011990010", i, "930", a)
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='证件有效期至'])[1]/following::input[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='证件有效期至'])[1]/following::input[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='日'])[1]/following::div[33]").click()
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
        # ERROR: Caught exception [unknown command [Click]]
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='开户银行'])[1]/following::div[6]").click()
        driver.find_element_by_xpath(u"//li[@style='-moz-user-select: none;'][contains(.,'中国工商银行')]").click()
        driver.find_element_by_xpath(
            u"//div[@style='display: block; -moz-user-select: none;'][contains(.,'请选择支行')]").click()
        driver.find_element_by_xpath("//input[contains(@id,'open_sub_bank')]").clear()
        driver.find_element_by_xpath("//input[contains(@id,'open_sub_bank')]").send_keys(u"春熙路")
        driver.find_element_by_xpath(u"//li[contains(.,'中国工商银行股份有限公司成都春熙路步行街支行')]").click()
        driver.find_element_by_id("account_no").click()
        driver.find_element_by_xpath("//input[@id='account_no']").clear()
        driver.find_element_by_xpath("//input[@id='account_no']").send_keys("6212260521", m, d, i, i, "00", a)
        driver.find_element_by_id("reserve_phone").click()
        driver.find_element_by_id("reserve_phone").clear()
        driver.find_element_by_id("reserve_phone").send_keys("18583998081")
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_id(u"Alipay-支付宝").click()
        driver.find_element_by_id(u"Alipay-支付宝").clear()
        driver.find_element_by_id(u"Alipay-支付宝").send_keys("0.11")
        driver.find_element_by_id(u"WechatPay-微信支付").click()
        driver.find_element_by_id(u"WechatPay-微信支付").clear()
        driver.find_element_by_id(u"WechatPay-微信支付").send_keys("0.21")
        driver.find_element_by_id(u"UnionPay_QR-银联二维码-2").click()
        driver.find_element_by_id(u"UnionPay_QR-银联二维码-2").clear()
        driver.find_element_by_id(u"UnionPay_QR-银联二维码-2").send_keys("0.31")
        driver.find_element_by_id(u"UnionPay_QR-银联二维码-1").click()
        driver.find_element_by_id(u"UnionPay_QR-银联二维码-1").clear()
        driver.find_element_by_id(u"UnionPay_QR-银联二维码-1").send_keys("0.41")
        driver.find_element_by_id(u"UnionPay_QR-银联二维码-1-rag_fee_max").click()
        driver.find_element_by_id(u"UnionPay_QR-银联二维码-1-rag_fee_max").clear()
        driver.find_element_by_id(u"UnionPay_QR-银联二维码-1-rag_fee_max").send_keys("1100")
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'hspcadmin'
__mtime__ = '2019/11/14'
"""
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.quit()
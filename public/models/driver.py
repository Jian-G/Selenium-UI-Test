#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Key'


import webbrowser
from selenium import webdriver

def browser():
    """
    启动浏览器驱动
    :return: 返回浏览器驱动URL
    """
    try:
        driver = webdriver.Firefox()
        return driver
    except Exception as msg:
        print("驱动异常-> {0}".format(msg))

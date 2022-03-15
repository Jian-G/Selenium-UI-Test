#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'YinJia'


import webbrowser
from selenium import webdriver

def browser():
    """
    启动浏览器驱动
    :return: 返回浏览器驱动URL
    """
    try:
        host = '127.0.0.1:8000'
        # driver = Remote(command_executor='https://' + host + '/wd/hub',
        #                 desired_capabilities={ 'platform': 'ANY',
        #                                        'browserName': 'chrome',
        #                                        'version': "",
        #                                        'javascriptEnabled': True
        #                                     }
        #                 )
        driver = webdriver.Firefox()
        return driver
    except Exception as msg:
        print("驱动异常-> {0}".format(msg))

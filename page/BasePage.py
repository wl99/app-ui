#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 17:01
# @Author  : wenlong.wu@tenbent.com
# @说明     ：根页面，主要用于存放公共方法，供其他 页面调用
# @File    : BasePage.py
# @Software: PyCharm
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver

from driver.Driver import AndroidClient


class BasePage(object):

    def __init__(self):
        self.driver: WebDriver = self.getDriver()

    @classmethod
    def getDriver(cls):
        cls.driver = AndroidClient.driver
        return cls.driver

    @classmethod
    def getClient(cls):
        return AndroidClient

    def find(self, by, value) -> WebElement:
        element: WebElement = self.driver.find_element(by, value)
        return element

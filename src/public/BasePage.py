#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 17:01
# @Author  : wenlong.wu@tenbent.com
# @说明    : 根页面，主要用于存放公共方法，供其他 页面调用
# @File    : BasePage.py
# @Software: PyCharm

from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.driver.Driver import AppClient


class BasePage(object):

    def __init__(self):
        self.driver: WebDriver = self.getDriver()
        self.platform = self.getPlatform()

    @classmethod
    def getDriver(cls):
        cls.driver = AppClient().driver
        return cls.driver

    @classmethod
    def getClient(cls):
        return AppClient

    @classmethod
    def getPlatform(cls):
        cls.platform = AppClient().platform
        return cls.platform

    def find(self, by, value) -> WebElement:
        print("\nby:{0},value:{1}".format(by, value))
        try:
            element: WebElement = self.driver.find_element(by, value)
            return element
        except Exception as e:
            return False

    def finds(self, by, value) -> WebElement:
        elements: WebElement = self.driver.find_elements(by, value)
        return elements

    def find_element(self, timeout, locator):
        return WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(*locator))

    def click(self, by, value, timeout=10):
        element = self.find_element(timeout, (by, value))
        element.click()
        return self

    def typing(self, byType, locate, value, timeout=10):
        element = self.find_element(timeout, (byType, locate))
        element.click()  # Let the element in focus.
        element.clear()
        element.send_keys(value)
        return self

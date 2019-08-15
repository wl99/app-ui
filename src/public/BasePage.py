#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 17:01
# @Author  : wenlong.wu@tenbent.com
# @说明    : 根页面，主要用于存放公共方法，供其他 页面调用
# @File    : BasePage.py
# @Software: PyCharm
import time

import allure
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.driver.Driver import AppClient
from src.utils.Logs import log


class BasePage(object):

    def __init__(self):
        self.driver: WebDriver = self.getDriver()
        self.platform = self.getPlatform()
        self.width = self.driver.get_window_size()['width']
        self.height = self.driver.get_window_size()['height']

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

    @allure.step("查找参数")
    def find(self, by, value, timeout=10) -> WebElement:
        self._find(by, value, timeout)

    @allure.step("查找文本")
    def text(self, text, timeout=10) -> WebElement:
        return self._find(By.XPATH, "//*[@text='" + text + "']", timeout)

    def _find(self, by, value, timeout=10) -> WebElement:
        log.i("查找方式:{0}，查找值:{1}".format(by, value))
        try:
            element: WebElement = WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(by, value))
            return element
        except Exception as e:
            print(e)
            log.e("通过方式{0}未查找到元素{1}".format(by, value))
            log.e(e)
            # 截图
            self.screen_shot("未找到元素")
            # 检查是否是因为权限弹窗导致无法查找元素
            if self.click_shoot_windows():
                log.i("出现权限弹窗，允许后重新查找元素")
                return self._find(by, value)
            return False

    def screen_shot(self, name: str):
        log.i("截图：{}".format(name))
        self.sleep(2)
        png_byte = self.driver.get_screenshot_as_png()
        allure.attach(png_byte, name, allure.attachment_type.PNG)

    def get_logcat(self, name: str):
        logcat = self.driver.get_log('logcat')
        c = '\n'.join([i['message'] for i in logcat])
        log.i("获取日志：{}".format(name))
        allure.attach(c, name, allure.attachment_type.TEXT)

    def finds(self, by, value) -> WebElement:
        return self.driver.find_elements(by, value)

    def click(self, by, value, timeout=10):
        self.find(by, value, timeout).click()
        return self

    @allure.step("输入数据：{sendStr}")
    def typing(self, by, value, sendStr, timeout=10):
        element = self.find(by, value, timeout)
        element.click()  # Let the element in focus.
        # element.clear()
        element.send_keys(sendStr)
        log.i("输入数据：{}".format(sendStr))
        return self

    @staticmethod
    def sleep(num):
        return time.sleep(num)

    def swip_down(self, count=1, method=None, speed=1000):
        """ 向下滑动,常用于下拉刷新
        :param count: 滑动次数
        :param method: 传入的方法 method(action) ,如果返回为True,则终止刷新
        :param speed: 滑动速度 ms
        """
        if count == 1:
            self.driver.swipe(self.width / 2, self.height * 2 / 5, self.width / 2, self.height * 4 / 5, speed)
            self.sleep(1)
        else:
            for x in range(count):
                self.driver.swipe(self.width / 2, self.height * 2 / 5, self.width / 2, self.height * 4 / 5, speed)
                self.sleep(1)
                try:
                    if method(self):
                        break
                except:
                    pass
        log.i("[滑动]向下刷新 ")

    def swip_up(self, count=1, method=None, speed=1000):
        """ 向上刷新
        :param count: 滑动次数
        :param method: 传入的方法 method(action) ,如果返回为True,则终止刷新
        :param speed: 滑动速度 ms
        :return:

        """
        if count == 1:
            self.sleep(1)
            self.driver.swipe(self.width / 2, self.height * 3 / 4, self.width / 2, self.height / 4, speed)
            self.sleep(2)
        else:
            for x in range(count):
                self.driver.swipe(self.width / 2, self.height * 3 / 4, self.width / 2, self.height / 4, speed)
                self.sleep(2)
                try:
                    if method(self):
                        break
                except:
                    pass
        log.i("[滑动]向上刷新 ")

    def swip_left(self, height=0.5, count=1, speed=1000):
        """ 向左滑动
        :param height: 高度满屏幕为1
        :param count: 滑动次数
        :param speed: 滑动速度 ms
        :return:
        """
        for x in range(count):
            self.sleep(1)
            self.driver.swipe(self.width * 7 / 8, self.height * height, self.width / 8, self.height * height, speed)
            self.sleep(2)
            log.i("[滑动]向左滑动")

    def swip_right(self, height=0.5, count=1, speed=1000):
        """向右滑动
        :param height: 高度满屏幕为1
        :param count: 滑动次数
        :param speed: 滑动速度 ms
        :return:
        """
        for x in range(count):
            self.sleep(1)
            self.driver.swipe(self.width / 8, self.height * height, self.width * 7 / 8, self.height * height, speed)
            self.sleep(2)
            log.i("[滑动]向右滑动 ")

    def click_shoot_windows(self):
        """
        :return:检测权限窗口
        """
        try:
            els = self.driver.find_elements(By.CLASS_NAME, 'android.widget.Button')
            for el in els:
                text1 = el.text
                if text1 == '允许':
                    el.click()
                    return True
                elif text1 == '始终允许':
                    el.click()
                    return True
                elif text1 == '确定':
                    el.click()
                    return True
            return False
        except:
            return False

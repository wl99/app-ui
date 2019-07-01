#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 16:42
# @Author  : wenlong.wu@tenbent.com
# @说明     ：Android驱动类
# @File    : Driver.py
# @Software: PyCharm

from appium import webdriver
from appium.webdriver.webdriver import WebDriver
import yaml


class AndroidClient(object):
    driver: WebDriver
    platform = "android"

    @classmethod
    def install_app(cls) -> WebDriver:
        cls.initDriver("install_app")

    @classmethod
    def restart_app(cls) -> WebDriver:
        return cls.initDriver("restart_app")

    @classmethod
    def initDriver(cls, key):
        # 加载配置文件并赋值
        driver_data = yaml.load(open("../data/driver.yaml"), Loader=yaml.FullLoader)
        platform = str(driver_data['platform'])
        cls.platform = platform
        server = driver_data[key]['server']
        implicitly_wait = driver_data[key]['implicitly_wait']
        caps = driver_data[key]['caps'][platform]
        # 启动服务，并设置隐性等待时间
        cls.driver = webdriver.Remote(server, caps)
        cls.driver.implicitly_wait(implicitly_wait)
        return cls.driver
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 16:45
# @Author  : wenlong.wu@tenbent.com
# @说明     ：
# @File    : __init__.py.py
# @Software: PyCharm
import os

# 定义数据根目录
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# 驱动配置路径
DRIVER_FILE = os.path.join(ROOT_DIR, 'driver.yaml')
ELEMENTS_PATH = os.path.join(ROOT_DIR, 'elements')

# 页面元素文件路径
LOGIN_PAGE_FILE = os.path.join(ELEMENTS_PATH, 'LoginPage.yaml')
MAIN_PAGE_FILE = os.path.join(ELEMENTS_PATH, 'MainPage.yaml')
PROFILE_PAGE_FILE = os.path.join(ELEMENTS_PATH, 'ProfilePage.yaml')
SETTING_PAGE_FILE = os.path.join(ELEMENTS_PATH, 'SettingPage.yaml')


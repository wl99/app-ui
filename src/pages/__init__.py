#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 16:50
# @Author  : wenlong.wu@tenbent.com
# @说明     ：
# @File    : __init__.py
# @Software: PyCharm
import os


routes = os.path.abspath(__file__).split('/')
print(routes)
ROOT = '/'.join(routes[:routes.index('app-ui') + 1])


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 16:41
# @Author  : wenlong.wu@tenbent.com
# @说明     ：
# @File    : __init__.py.py
# @Software: PyCharm
import os

routes = os.path.abspath(__file__).split('/')
ROOT = '/'.join(routes[:routes.index('app-ui') + 1])

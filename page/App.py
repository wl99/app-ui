#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 17:13
# @Author  : wenlong.wu@tenbent.com
# @说明     ：打开APP程序
# @File    : App.py
# @Software: PyCharm

from page.BasePage import BasePage
from page.MainPage import MainPage


class App(BasePage):
    @classmethod
    def main(cls):
        cls.getClient().restart_app()
        return MainPage()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 17:13
# @Author  : wenlong.wu@tenbent.com
# @说明     ：打开APP程序
# @File    : App.py
# @Software: PyCharm

from src.public.BasePage import BasePage
from src.pages.MainPage import MainPage


class App(BasePage):
    @classmethod
    def main(cls, platform):
        cls.getClient().restart_app(platform)
        return MainPage()

    @classmethod
    def quit(cls):
        cls.getClient().quit()

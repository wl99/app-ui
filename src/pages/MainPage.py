#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 17:15
# @Author  : wenlong.wu@tenbent.com
# @说明     ：app主页
# @File    : MainPage.py
# @Software: PyCharm
import allure
import yaml

from data import MAIN_PAGE_FILE
from src.pages.ProfilePage import ProfilePage
from src.public.BasePage import BasePage

# 加载页面元素配置
page_data = yaml.load(open(MAIN_PAGE_FILE), Loader=yaml.FullLoader)


class MainPage(BasePage):

    @allure.step("点击【我的】")
    def go_to_profile(self):
        els = page_data[self.platform]
        self.find(**els["我的"]).click()
        return ProfilePage()

    @allure.step("向上滑动")
    def swip_up_test(self):
        self.swip_up(2)

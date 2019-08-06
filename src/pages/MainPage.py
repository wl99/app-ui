#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 17:15
# @Author  : wenlong.wu@tenbent.com
# @说明     ：app主页
# @File    : MainPage.py
# @Software: PyCharm
import allure
import yaml

from src.pages.ProfilePage import ProfilePage
from . import ROOT
from src.public.BasePage import BasePage


class MainPage(BasePage):
    # 加载页面元素配置
    page_data = yaml.load(open(ROOT + "/data/elements/MainPage.yaml"), Loader=yaml.FullLoader)
    els = page_data[BasePage.getPlatform()]

    @allure.step("点击【我的】")
    def go_to_profile(self):
        self.find(**self.els["我的"]).click()
        return ProfilePage()

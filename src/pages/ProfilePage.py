#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 17:20
# @Author  : wenlong.wu@tenbent.com
# @说明     ：我的页面
# @File    : ProfilePage.py
# @Software: PyCharm
import allure
import yaml

from src.pages.LoginPage import LoginPage
from src.pages.SettingPage import SettingPage
from . import ROOT
from src.public.BasePage import BasePage


class ProfilePage(BasePage):
    # 加载页面元素配置
    page_data = yaml.load(open(ROOT + "/data/elements/ProfilePage.yaml"), Loader=yaml.FullLoader)
    els = page_data[BasePage.getPlatform()]

    @allure.step("点击【手机登录】")
    def go_to_login_by_phone(self):
        self.find(**self.els["手机登录"]).click()
        return LoginPage()

    @allure.step("点击【设置】")
    def go_to_set_page(self):
        self.click(**self.els["设置"])
        return SettingPage()

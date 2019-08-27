#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 17:20
# @Author  : wenlong.wu@tenbent.com
# @说明     ：我的页面
# @File    : ProfilePage.py
# @Software: PyCharm
import allure
import yaml

from data import PROFILE_PAGE_FILE
from src.pages.LoginPage import LoginPage
from src.pages.SettingPage import SettingPage
from src.public.BasePage import BasePage

# 加载页面元素配置
page_data = yaml.load(open(PROFILE_PAGE_FILE), Loader=yaml.FullLoader)


class ProfilePage(BasePage):

    @allure.step("点击【手机登录】")
    def go_to_login_by_phone(self):
        els = page_data[self.platform]
        self.find(**els["手机登录"]).click()
        return LoginPage()

    @allure.step("点击【设置】")
    def go_to_set_page(self):
        els = page_data[self.platform]
        self.click(**els["设置"])
        return SettingPage()

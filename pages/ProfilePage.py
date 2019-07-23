#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 17:20
# @Author  : wenlong.wu@tenbent.com
# @说明     ：我的页面
# @File    : ProfilePage.py
# @Software: PyCharm
import yaml

from pages.BasePage import BasePage
from pages.LoginPage import LoginPage


class ProfilePage(BasePage):
    # 加载页面元素配置
    page_data = yaml.load(open("../data/elements/ProfilePage.yaml"), Loader=yaml.FullLoader)


    def go_to_login(self):
        _login_phone = ProfilePage.page_data[BasePage.getPlatform()]["_login_phone"]
        self.find(**_login_phone).click()
        return LoginPage()



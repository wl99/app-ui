#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 17:20
# @Author  : wenlong.wu@tenbent.com
# @说明     ：我的页面
# @File    : ProfilePage.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from page.BasePage import BasePage


class ProfilePage(BasePage):

    def go_to_login(self):
        self.getDriver().find_element_by_id("login_phone_iv").click()



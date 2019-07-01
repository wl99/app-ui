#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 17:15
# @Author  : wenlong.wu@tenbent.com
# @说明     ：app主页
# @File    : MainPage.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from page.BasePage import BasePage
from page.ProfilePage import ProfilePage


class MainPage(BasePage):
    _profile_button = (By.ID, "user_profile_icon")

    def go_to_profile(self):
        # self.find(MainPage._profile_button).click()
        print("$$$$$$$$$$$$$$$")
        self.driver.find_elements_by_id("iv_tab_icon").__getitem__(4).click()
        return ProfilePage()


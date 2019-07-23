#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 17:15
# @Author  : wenlong.wu@tenbent.com
# @说明     ：app主页
# @File    : MainPage.py
# @Software: PyCharm
import yaml

from pages.BasePage import BasePage
from pages.ProfilePage import ProfilePage


class MainPage(BasePage):
    # 加载页面元素配置
    page_data = yaml.load(open("../data/elements/MainPage.yaml"), Loader=yaml.FullLoader)

    def go_to_profile(self):
        _profile_button = MainPage.page_data[BasePage.getPlatform()]["_profile_button"]
        # self.driver.find_elements_by_id("iv_tab_icon").__getitem__(4).click()
        print("----------{}".format(BasePage.getPlatform()))
        el = self.find(**_profile_button)
        el.click()
        return ProfilePage()

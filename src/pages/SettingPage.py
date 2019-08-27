#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time         : 2019-07-24 11:38
# @Author       : wenlong.wu@tenbent.com
# @description  : 设置页面
# @File         : SettingPage
# @Software     : PyCharm
import allure
import yaml

from data import SETTING_PAGE_FILE
from src.public.BasePage import BasePage

# 加载页面元素配置
page_data = yaml.load(open(SETTING_PAGE_FILE), Loader=yaml.FullLoader)


class SettingPage(BasePage):

    @allure.step("点击【退去登录】，并【确定】")
    def exit_app(self):
        els = page_data[self.platform]
        self.click(**els["退出登录"])
        self.click(**els["确定"])

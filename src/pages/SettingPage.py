#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time         : 2019-07-24 11:38
# @Author       : wenlong.wu@tenbent.com
# @description  : 设置页面
# @File         : SettingPage
# @Software     : PyCharm
import allure
import yaml

from . import ROOT
from src.public.BasePage import BasePage


class SettingPage(BasePage):
    # 加载页面元素配置
    page_data = yaml.load(open(ROOT + "/data/elements/SettingPage.yaml"), Loader=yaml.FullLoader)
    els = page_data[BasePage.getPlatform()]

    @allure.step("点击【退去登录】，并【确定】")
    def exit_app(self):
        self.click(**self.els["退出登录"])
        self.click(**self.els["确定"])


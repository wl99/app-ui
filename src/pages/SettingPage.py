#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time         : 2019-07-24 11:38
# @Author       : wenlong.wu@tenbent.com
# @description  : 设置页面
# @File         : SettingPage
# @Software     : PyCharm

import yaml

from . import ROOT
from src.public.BasePage import BasePage


class SettingPage(BasePage):
    # 加载页面元素配置
    page_data = yaml.load(open(ROOT + "/data/elements/ProfilePage.yaml"), Loader=yaml.FullLoader)
    els = page_data[BasePage.getPlatform()]

    def exit_app(self):
        self.find(**self.els["退出登陆"]).click()


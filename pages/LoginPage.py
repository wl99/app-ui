#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time         : 2019-07-23 23:10
# @Author       : wenlong.wu@tenbent.com
# @description  : 登陆页面
# @File         : LoginPage.py
# @Software     : PyCharm

import yaml

from pages.BasePage import BasePage


class LoginPage(BasePage):
    # 加载页面元素配置
    page_data = yaml.load(open("../data/elements/LoginPage.yaml"), Loader=yaml.FullLoader)

    def login_by_phone(self, phoneNum: str):
        els = LoginPage.page_data[BasePage.getPlatform()]

        # 如果存在数据，清除
        if self.find(**els["_clear_btn"]):
            self.find(**els["_clear_btn"]).click()

        # 输入手机号
        phone_input = self.find(**els["_phone_input"])
        phone_input.click()
        phone_input.send_keys(phoneNum)

        # 点击下一步
        self.click(**els["_next_btn"])

        # 输入验证码
        yzm_input = self.find(**els["_yzm_input"])
        yzm_input.click()
        yzm_input.send_keys("1234")

        # 点击登陆
        self.click(**els["_ok_btn"])




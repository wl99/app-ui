#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time         : 2019-07-23 23:10
# @Author       : wenlong.wu@tenbent.com
# @description  : 登陆页面
# @File         : LoginPage.py
# @Software     : PyCharm
import allure
import yaml


from . import ROOT
from src.public.BasePage import BasePage


class LoginPage(BasePage):
    # 加载页面元素配置
    page_data = yaml.load(open(ROOT + "/data/elements/LoginPage.yaml"), Loader=yaml.FullLoader)
    els = page_data[BasePage.getPlatform()]

    @allure.step("输入手机号码:{phoneNum}")
    def input_phone_number(self, phoneNum: str):
        # 如果存在数据，清除
        if self.find(**self.els["X"]):
            self.clear_input()
        # 输入手机号
        phone_input=self.find(**self.els["手机号码输入"])
        phone_input.click()
        phone_input.send_keys(phoneNum)

    @allure.step("清除输入框内容")
    def clear_input(self):
        self.find(**self.els["X"]).click()

    @allure.step("点击【下一步】")
    def click_next(self):
        # 点击下一步
        self.click(**self.els["下一步"])

    @allure.step("输入验证码")
    def input_yzm(self, nums):
        # 输入验证码
        yzm_input=self.find(**self.els["验证码输入"])
        yzm_input.click()
        yzm_input.send_keys(nums)

    @allure.step("点击OK，登陆")
    def click_ok(self):
        # 点击登陆
        self.click(**self.els["登陆"])
        from src.pages.ProfilePage import ProfilePage
        return ProfilePage()


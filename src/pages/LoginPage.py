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

# 加载页面元素配置
page_data = yaml.load(open(ROOT + "/data/elements/LoginPage.yaml"), Loader=yaml.FullLoader)


class LoginPage(BasePage):

    @allure.step("输入手机号码:{phoneNum}")
    def input_phone_number(self, phoneNum: str):
        els = page_data[self.platform]
        # 如果存在数据，清除
        if self.find(**els["X"]):
            self.clear_input()
        # 输入手机号，iOS输入方式不一致
        if self.platform == 'android':
            elements = list(self.finds(**els["手机号码输入"]))
            for i in range(len(phoneNum)):
                elements[i].send_keys(phoneNum[i])
        else:
            self.typing(**els["手机号码输入"], sendStr=phoneNum)

    @allure.step("清除输入框内容")
    def clear_input(self):
        els = page_data[self.platform]
        self.find(**els["X"]).click()

    @allure.step("点击【下一步】")
    def click_next(self):
        els = page_data[self.platform]
        # 点击下一步
        self.click(**els["下一步"])

    @allure.step("输入验证码")
    def input_yzm(self, nums):
        els = page_data[self.platform]
        # 输入验证码
        if self.platform == 'android':
            elements = list(self.finds(**els["验证码输入"]))
            for i in range(len(nums)):
                elements[i].send_keys(nums[i])
        else:
            self.typing(**els["验证码输入"], sendStr=nums)

    @allure.step("点击OK，登陆")
    def click_ok(self):
        els = page_data[self.platform]
        # 点击登陆
        self.click(**els["登陆"])
        from src.pages.ProfilePage import ProfilePage
        return ProfilePage()

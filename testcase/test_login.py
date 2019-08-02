#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 17:36
# @Author  : wenlong.wu@tenbent.com
# @说明     ：登录用例
# @File    : test_login.py
# @Software: PyCharm
import pytest

from src.pages.App import App


class TestLogin(object):
    def test_login(self, app_driver):
        print(app_driver)
        login_page = app_driver.go_to_profile().go_to_login_by_phone()
        login_page.input_phone_number("13000000000")
        login_page.click_next()
        login_page.input_yzm("1234")
        profile_page = login_page.click_ok()
        profile_page.go_to_set_page()

    # self.loginPage.back()

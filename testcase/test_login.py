#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 17:36
# @Author  : wenlong.wu@tenbent.com
# @说明     ：登录用例
# @File    : test_login.py
# @Software: PyCharm
import allure
import pytest



@allure.story("登陆测试用例")
class TestLogin(object):

    @allure.title("登录手机号：{phone}")
    @pytest.mark.parametrize("phone,yzm", [("13000000000", "2234")])
    def test_login(self, app, phone, yzm):
        app.swip_up_test()
        login_page = app.go_to_profile().go_to_login_by_phone()
        login_page.screen_shot("手机号输入页面截图")
        login_page.input_phone_number(phone)
        login_page.click_next()
        login_page.input_yzm(yzm)
        profile_page = login_page.click_ok()
        profile_page.screen_shot("我的页面截图")
        profile_page.go_to_set_page().exit_app()


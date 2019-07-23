#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 17:36
# @Author  : wenlong.wu@tenbent.com
# @说明     ：登录用例
# @File    : test_login.py
# @Software: PyCharm
import pytest
from appium.webdriver.webdriver import WebDriver

from pages.App import App


class TestLogin(object):
    driver: WebDriver


    def test_login(self, platform):
        print(platform)
        App.main(platform).go_to_profile().go_to_login().login_by_phone("13000000000")

        # self.loginPage.back()


if __name__ == "__main__":
    pytest.main("pytest --platform=ios test_login.py")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 17:36
# @Author  : wenlong.wu@tenbent.com
# @说明     ：登录用例
# @File    : test_login.py
# @Software: PyCharm
import pytest

from page.App import App


class TestLogin(object):





    def test_login(self):
        App.main().go_to_profile().go_to_login()


        # self.loginPage.back()

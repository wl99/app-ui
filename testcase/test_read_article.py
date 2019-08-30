#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time         : 2019-08-14 17:04
# @Author       : wenlong.wu@tenbent.com
# @description  : 阅读文章
# @Software     : PyCharm
import allure
from appium.webdriver.mobilecommand import MobileCommand
from selenium.webdriver.common.by import By


@allure.story("阅读文章")
class TestReadArticle:

    @allure.title("阅读文章")
    def test_read_article(self, app):
        """
        :param app:
        :return:
        """
        app.go_to_article().share_article()

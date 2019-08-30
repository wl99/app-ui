#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time         : 2019-08-27 16:34
# @Author       : wenlong.wu@tenbent.com
# @description  : 文章详情页面，原生混合H5的页面
# @Software     : PyCharm

# 加载页面元素配置
import allure
import yaml

from data import ARTICLE_PAGE_FILE
from src.public.BasePage import BasePage

page_data = yaml.load(open(ARTICLE_PAGE_FILE), Loader=yaml.FullLoader)


class ArticlePage(BasePage):

    @allure.step("分享文章")
    def share_article(self):
        els = page_data[self.platform]
        self.switch_to_webview()
        self.swip_up(2)
        self.switch_to_native()
        print(self.get_current_context())
        self.driver.find_element(**els["分享"]).click()
        self.click(**els["分享"])
        # el = self.find(**els["分享"])
        el2 = self.driver.find_element(**els["分享"])
        # print(el.text)
        self.element_shot(el2, "分享")

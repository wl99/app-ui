#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time         : 2019-07-22 17:05
# @Author       : wenlong.wu@tenbent.com
# @description  : 配置文件
# @File         : conftest.py
# @Software     : PyCharm
import datetime

import allure
import pytest

from src.pages.App import App


def pytest_addoption(parser):
    parser.addoption("--platform", action="store", dest="platform", choices=['ios', 'android', 'xcx'],
                     default="android", help="终端默认为Android")


@pytest.fixture(scope="session", autouse=True)
def platform(request):
    return request.config.getoption("platform")


@pytest.fixture(scope="class", autouse=True)
def app(platform):
    yield App.main(platform)
    # App.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # 用例报错捕捉
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        App().screen_shot("错误截图")
        App().get_logcat("手机错误日志")


def pytest_runtest_call(item):
    # 每条用例代码执行之前，非用例执行之前
    allure.dynamic.description("""
    用例开始时间：{0}
    执行终端：{1}""".format(datetime.datetime.now(), App().platform))

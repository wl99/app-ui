#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time         : 2019-07-22 17:05
# @Author       : wenlong.wu@tenbent.com
# @description  : 配置文件
# @File         : conftest.py
# @Software     : PyCharm

import pytest

from src.pages.App import App


def pytest_addoption(parser):
    parser.addoption("--platform", action="store", dest="platform", choices=['ios', 'android', 'xcx'],
                     default="android", help="终端默认为Android")


@pytest.fixture(scope="session", autouse=True)
def platform(request):
    return request.config.getoption("platform")


@pytest.fixture(scope="class", autouse=True)
def app_driver(platform):
    yield App.main(platform)
    App.quit()


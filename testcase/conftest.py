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
def app_driver(platform):
    yield App.main(platform)
    App.quit()

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # 用例报错捕捉
#
#
#     Action = App.main("ios")
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == "call" and rep.failed:
#         f = Action.driver.get_screenshot_as_png()
#         allure.attach(f, '失败截图', allure.attachment_type.PNG)
        # logcat = Action.driver.get_log('logcat')
        # c = '\n'.join([i['message'] for i in logcat])
        # allure.attach(c, 'APPlog', allure.attachment_type.TEXT)
        # if Action.get_app_pid() != Action.apppid:
        #     raise Exception('设备进程 ID 变化，可能发生崩溃')

#
# def pytest_runtest_call(item):
#     # 每条用例代码执行之前，非用例执行之前
#     allure.dynamic.description('用例开始时间:{}'.format(datetime.datetime.now()))
#     Action = App.main(platform)
#     if Action.get_app_pid() != Action.apppid:
#         raise Exception('设备进程 ID 变化，可能发生崩溃')

#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time         : 2019-07-24 10:18
# @Author       : wenlong.wu@tenbent.com
# @description  : 统一运行脚本
# @File         : runcase.py
# @Software     : PyCharm
import os
import subprocess
import sys

import pytest
import logging

logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)s %(asctime)s %(filename)s %(funcName)s line:%(lineno)d]: %(message)s',
                    datefmt='%y%m%d %H:%M:%S')

# 定义数据根目录
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    testcase = sys.argv[1]
    platform = sys.argv[2]
    logging.info(testcase)
    # todo 根据现有的android设备，开启appium服务时加载对应版本的ChromeDriver
    # 1、获取要使用的设备，使用语句查询设备中的ChromeDriver版本
    # adb shell dumpsys package com.google.android.webview | grep versionName
    # 2、使用命令启动appium，并传入对应版本参数
    # appium --chromedriver-executable /path/to/my/chromedriver

    xml_report_path = os.path.join(ROOT_DIR, 'report', 'xml')
    html_report_path = os.path.join(ROOT_DIR, 'report', 'html')
    # , '--reruns', '1'
    pytest.main(['-s', '--platform', platform, '--alluredir', xml_report_path, testcase])
    cmd = 'allure generate --clean {xml} -o {html}'.format(xml=xml_report_path, html=html_report_path)
    logging.info(cmd)
    subprocess.call(cmd, shell=True)

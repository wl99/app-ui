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

routes = os.path.abspath(__file__).split('/')
ROOT = '/'.join(routes[:routes.index('app-ui') + 1])

if __name__ == '__main__':
    testcase = sys.argv[1]
    platform = sys.argv[2]
    logging.info(testcase)

    xml_report_path = os.path.join(ROOT, 'report', 'xml')
    html_report_path = os.path.join(ROOT, 'report', 'html')
    pytest.main(['-s', '--platform', platform, '--alluredir', xml_report_path, testcase])
    cmd = 'allure generate --clean {xml} -o {html}'.format(xml=xml_report_path, html=html_report_path)
    logging.info(cmd)
    subprocess.call(cmd, shell=True)

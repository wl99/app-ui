#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time         : 2019-08-13 16:01
# @Author       : wenlong.wu@tenbent.com
# @description  : 日志打印
# @Software     : PyCharm

import time


class log:
    @staticmethod
    def e(msg, list_msg=None):
        if list_msg is None:
            list_msg = []
        if list_msg:
            log.show_list(msg, list_msg, log.e)
        else:
            ColorLog.show_error(get_now_time() + " [Error]:" + "".join(str(msg)))

    @staticmethod
    def w(msg, list_msg=None):
        if list_msg is None:
            list_msg = []
        if list_msg:
            log.show_list(msg, list_msg, log.w)
        else:
            ColorLog.show_warn(get_now_time() + " [Warn]:" + "".join(str(msg)))

    @staticmethod
    def i(msg, list_msg=None):
        if list_msg is None:
            list_msg = []
        if list_msg:
            log.show_list(msg, list_msg, log.i)
        else:
            ColorLog.show_info(get_now_time() + " [Info]:" + "".join(str(msg)))

    @staticmethod
    def d(msg, list_msg=None):
        if list_msg is None:
            list_msg = []
        if list_msg:
            log.show_list(msg, list_msg, log.d)
        else:
            ColorLog.show_debug(get_now_time() + " [Debug]:" + "".join(str(msg)))

    @staticmethod
    def show_list(msg, list_msg, f):
        temp = msg + "[ " + "\t".join(list_msg) + " ]"
        f(temp)


class ColorLog:
    @staticmethod
    def c(msg, colour):
        try:
            from termcolor import colored, cprint
            p = lambda x: cprint(x, '%s' % colour)
            return p(msg)
        except:
            print(msg)

    @staticmethod
    def show_verbose(msg):
        ColorLog.c(msg, 'white')

    @staticmethod
    def show_debug(msg):
        ColorLog.c(msg, 'blue')

    @staticmethod
    def show_info(msg):
        ColorLog.c(msg, 'green')

    @staticmethod
    def show_warn(msg):
        ColorLog.c(msg, 'yellow')

    @staticmethod
    def show_error(msg):
        ColorLog.c(msg, 'red')


def get_now_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

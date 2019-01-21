# coding: utf-8

import os
import os.path
from wxpy import *


def send_wechat_report():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    reportFilePath = os.path.join(base_dir, 'reports')
    report_list = os.listdir(reportFilePath)
    report_list.sort(key=lambda fn: os.path.getatime(reportFilePath + '\\' + fn))
    new_report = os.path.join(reportFilePath, report_list[-2])
    bot = Bot(cache_path=True, console_qr=1)
    group_test = bot.groups().search('测试')[0]
    group_test.send('自动化测试报告：')
    group_test.send_file(new_report)


if __name__ == '__main__':
    send_wechat_report()

# -*- coding: utf-8 -*-

import unittest
import sys

from HTMLTestRunner import HTMLTestRunner
from case.TestSearchPage import TestSearchPage

reload(sys)
sys.setdefaultencoding("utf-8")

if __name__ == '__main__':
    # TestSearchPage('testSearch')
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestSearchPage('testSearch'))
    # 定义报告存放路径
    fp = open('./report/result.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='百度搜索测试报告', description='用例执行情况：')
    runner.run(suite)
    fp.close()
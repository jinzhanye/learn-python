# -*- coding: utf-8 -*-
import sys
import unittest
from selenium import webdriver
from pages.SearchPage import SearchPage

reload(sys)
sys.setdefaultencoding("utf-8")


class TestSearchPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testSearch(self):
        driver = self.driver
        # 百度网址
        url = u"http://www.baidu.com"
        # 搜索文本
        text = u"开源优测"
        # 期望验证的标题
        assert_title = u"开源优测_百度搜索"
        print(assert_title)

        searchPage = SearchPage(driver, url)

        # 启动浏览器，访问百度首页
        searchPage.goto_baidu_homepage()

        # 输入 搜索词
        searchPage.input_search_text(text)

        # 单击 百度一下 按钮进行搜索
        searchPage.click_search_btn()

        # 验证标题
        self.assertEqual(assert_title, u"开源优测_百度搜索")

    def tearDown(self):
        self.driver.quit()

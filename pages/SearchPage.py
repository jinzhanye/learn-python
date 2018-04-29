# -*- coding: utf-8 -*-
import sys
from selenium.webdriver.common.by import By
from BasePage import BasePage

reload(sys)
sys.setdefaultencoding("utf-8")

class SearchPage(BasePage):
    # 元素集
    # 搜索输入框
    search_input = (By.ID, 'kw')
    # 百度一下 按钮
    search_button = (By.ID, 'su')

    def __init__(self, driver, base_url=u"http://www.baidu.com"):
        BasePage.__init__(self, driver, base_url)

    def goto_baidu_homepage(self):
        print (u"打开浏览器:"+self.base_url)
        self.driver.get(self.base_url)

    def input_search_text(self, text=u"开源优测"):
        print (u"输入搜索关键字： 开源优测 ")
        self.input_text(self.search_input, text)

    def click_search_btn(self):
        print (u"点击 百度一下  按钮")
        self.click(self.search_button)

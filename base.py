# coding=utf-8
from selenium import webdriver
import time
from util.get_by_local import GetByLocal


class ActionMethod:
    def get_url(self, url):
        self.driver.get(url)

    def get_element(self, id):
        # 实例化对象
        get_by_element = GetByLocal(self.driver)
        element = get_by_element.get_local_element(id)
        return element

    def element_send_keys(self, id, value):
        # 对元素输入
        element = self.get_element(id)
        element.send_keys(value)

    def click_element(self,id):
        element = self.get_element(id)
        element.click()

    def sleep_time(self):
        # 等待
        time.sleep(3)

    def close_browser(self):
        # 关闭浏览器
        self.driver.close()


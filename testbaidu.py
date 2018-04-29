# coding=utf-8
import time
import unittest
from selenium import webdriver


class BaiduSearch(unittest.TestCase):
    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.driver.get("https://www.baidu.com")

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        self.driver.quit()

    def test_baidu_search(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        self.driver.find_element_by_id('kw').send_keys('selenium-demo')
        time.sleep(2)
        try:
            assert 'selenium-demo' in self.driver.title
            print ('Test Pass.')
        except Exception as e:
            print (self.driver.title)
            print ('Test Fail.', format(e))


# __name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。
# 这句话的意思就是，当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
if __name__ == '__main__':
    # unittest.main(), 添加这个是支持在cmd，里面，cd到这个脚本文件所在的目录，然后Python
    # 脚本名.py执行，如果不添加这一段，是无法执行cmd里面运行脚本的
    unittest.main()

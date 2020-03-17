# -*- coding:utf-8 -*-
# @Time   : 2019-10-17
# @Author : Dingjs

import time
import unittest
from UISelenium_python_autoFramewrok.utils.Browser_engine import BrowserEngine

class BaiduSearch(unittest.TestCase):

    def UnsupportBrowser(cls):
        pass


    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)


    def tearDown(self):
        self.driver.quit()

    def test_baidu_search(self):

        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(1)
        try:
            assert 'selenium' in self.driver.title
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))

if __name__ == "__main__":
    unittest.main()









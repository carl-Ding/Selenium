# -*- coding:utf-8 -*-
# @Time   : 2019-10-18
# @Author : Dingjs

from UISelenium_python_autoFramewrok.utils.Basepage import BasePage
from selenium.webdriver.common.by import By

class NewHomePage(BasePage):
    #点击进入体育新闻入口
    sport_news_link =(By.XPATH,"//*[@class = 'lavalamp-item']/a[text()= '体育']")
    def click_sport(self):
        self.click(self.sport_news_link)
        self.sleep(2)
# -*- coding:utf-8 -*-
# @Time   : 2019-10-17
# @Author : Dingjs

import  os.path
from configparser import ConfigParser
from selenium import webdriver
from UISelenium_python_autoFramewrok.utils.log import Logger

logger = Logger(logger='BrowserEngine').getlog()

class BrowserEngine(object):
    dir  = os.path.dirname(os.path.abspath('.')) #相对路径获取方法
    chrome_dir_path = dir + '/drivers/chromedriver.exe'    #如果把chromedriver放到python根目录下，则可省了
    ie_driver_path = dir + '/drivers/IEDriverServer.exe'

    def __init__(self,driver):
        self.driver = driver
        #加载启动项
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('headless')

    #从配置文件config.ini读取浏览器等信息
    def open_browser(self, driver):

        config =ConfigParser()
        # file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        # config.read(file_path,encoding='UTF-8'), 如果代码有中文注释，用这个，不然报解码错误

        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")
        logger.info("The test server url is: %s" % url)

        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            # driver = webdriver.Chrome(self.chrome_driver_path)
            driver = webdriver.Chrome(chrome_options=self.option) #调用option，不打开浏览器运行testcase
            # driver =webdriver.Chrome()
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser.")

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    #退出浏览器
    def quit_browser(self):
        self.driver.quit()
        logger.info("Now, Close and quit the browser.")



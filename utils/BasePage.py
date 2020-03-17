# -*- coding:utf-8 -*-
# @Time   : 2019-10-25
# @Author : Dingjs

from public.common.log import Logger
from config import globalparam
from selenium.common.exceptions import NoSuchElementException
import os
import time

logger = Logger(logger='BasePage').getlog()
class BasePage:
    """测试基类"""

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def isdisplayed(element):
        """元素是否存在"""
        value = element.is_displayed()
        return value

    @staticmethod
    def sleep(secondes):
        """强制等待"""
        time.sleep(secondes)
        logger.info('Sleep for %d seconds' % secondes)

    def open_url(self,url):
        self.driver.get(url)

    def forward(self):
        """浏览器前进"""
        self.driver.forward()
        logger.info("Click forward on current page.")

    def back(self):
        """浏览器后退"""
        self.driver.back()
        logger.info("Click back on current page.")

    def wait(self,seconds):
        """隐式等待"""
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    def close(self):
        """关闭当前窗口"""
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.info("Faile to quit the browser with %s" %e)

    def get_img(self):
        """截图"""
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = os.path.join(globalparam.test_img_path,'%s.png' % rq)
        # noinspection PyBroadException

        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")

        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_img()

    def find_element(self, selector):
        """定位元素"""
        by = selector[0]
        value = selector[1]
        element = None
        if by in ['id', 'name', 'class', 'tag', 'link', 'plink', 'css', 'xpath']:
            # noinspection PyBroadException
            try:
                if by == 'id':
                    element = self.driver.find_element_by_id(value)
                elif by == 'name':
                    element = self.driver.find_element_by_name(value)
                elif by == 'class':
                    element = self.driver.find_element_by_class_name(value)
                elif by == 'tag':
                    element = self.driver.find_element_by_tag_name(value)
                elif by == 'link':
                    element = self.driver.find_element_by_link_text(value)
                elif by == 'plink':
                    element = self.driver.find_element_by_partial_link_text(value)
                elif by == 'css':
                    element = self.driver.find_element_by_css_selector(value)
                elif by == 'xpath':
                    element = self.driver.find_element_by_xpath(value)
                else:
                    logger.error('Not find the element')
                logger.info("Had  find the element! ,by %s via value :%s " %(by,value))
                # logger.info('元素定位成功。定位方式：%s，使用的值%s：' % (by, value))

                return element
            except NoSuchElementException as e:
                logger.error("NoSuchElementException %s " %e)
                self.get_img()  # 调用截图
        else:
            logger.error('Please enter a valid type of targeting elements')

    def type(self, selector, value):
        """输入内容"""
        element = self.find_element(selector)
        # element.clear()
        logger.info('clear input_box')
        # noinspection PyBroadException
        try:
            element.send_keys(value)
            logger.info('input is：%s' % value)
        except BaseException:
            logger.error('Failed to type in input box', exc_info=1)
            self.get_img()

    #输入并确认
    def type_enter(self,selector,value):
        try:
            element = self.find_element(selector)
            element.send_keys(value)
            time.sleep(1)
            element.send_keys(Keys.ENTER)
        except Exception as e:
            logger.info("Failed to type_and_enter with %s" % e)
            self.get_img()
            raise

    def click(self, selector):
        """点击元素"""
        element = self.find_element(selector)
        # noinspection PyBroadException
        try:
            element.click()
            logger.info('"The element \' %s \' was clicked." % element.text')
        except BaseException:
            display = self.isdisplayed(element)
            if display is True:
                self.sleep(3)
                element.click()
                logger.info('The element was clicked')
            else:
                self.get_img()
                logger.error('Failed to click the element', exc_info=1)

    def right_click(self,selector):
        """右击元素"""
        element = self.find_element(selector)
        try:
            ActionChains(self.driver).context_click(element).perform()
            logger.info("The element \' %s \' was clicked." % element.text)
        except NameError as e:
            logger.error("Failed to right_click the element with %s" % e)
            self.get_img()

    def double_click(self,selector):
        """双击"""
        element = self.find_element(selector)
        try:
            ActionChains(self.driver).double_click(element).perform()
        except Exception as e:
            logger.info("Failed to double_click the element with %s" % e)
            self.get_img()
            raise

    def move_to_element(self,selector):
        """鼠标移到元素上"""
        try:
            element = self.find_element(selector)
            ActionChains(self.driver).move_to_element(element).perform()
        except Exception as e:
            logger.info("Failed to move_to_element the element with %s" % e)
            self.get_img()
            raise

    def drag_and_drop(self, element_selector,ta_selector):
        """拖拽"""
        try:
            element_drag = self.find_element(element_selector)
            taget_drop = self.find_element(ta_selector)
            ActionChains(self.driver).drag_and_drop(element_drag,taget_drop).perform()
        except Exception as e:
            logger.info("Failed to drag_and_drop the element with %s" % e)
            self.get_img()
            raise

    def refresh(self):
        """刷新"""
        self.driver.refresh()

    def submit(self,selector):
        """submit"""
        try:
            element = self.find_element(selector)
            element.submit()
        except Exception as e:
            logger.info("Failed to submit the element with %s" % e)
            self.get_img()

    def get_attribute(self,selector,attribute):
        """获取元素属性"""
        try:
            element = self.find_element(selector)
            return element.get_attribute(attribute)
        except Exception as e:
            logger.info("Failed to get_attribute  with %s" % e)
            self.get_img()
            raise

    def get_text(self,selector):
        """获取元素的文本信息"""
        try:
            return self.find_element(selector).text
        except Exception as e:
            logger.info("Failed to get_text  with %s" % e)
            self.get_img()

    def dismiss_alert(self):
        """弹窗 alert——取消"""
        self.driver.switch_to.alert.dismiss()


    def clear(self,selector):
        """清除文本框"""
        element = self.find_element(selector)
        try:
            element.clear()
            logger.info("Clear text in input box before typing.")

        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_img()

    def use_js(self, js):
        """调用js"""
        # noinspection PyBroadException
        try:
            self.driver.execute_script(js)
            logger.info('successful，js contents is：%s' % js)
        except BaseException:
            logger.error('js error', exc_info=1)

    def switch_menue(self, parentelement, secelement, targetelement):
        """三级菜单切换"""
        self.sleep(3)
        # noinspection PyBroadException
        try:
            self.driver.switch_to_default_content()
            self.click(parentelement)
            logger.info('成功点击一级菜单：%s' % parentelement)
            self.click(secelement)
            logger.info('成功点击二级菜单：%s' % secelement)
            self.click(targetelement)
            logger.info('成功点击三级菜单：%s' % targetelement)
        except BaseException:
            logger.error('切换菜单报错', exc_info=1)


    def switch_ifarme(self, selector):
        """切换ifarme"""
        element = self.find_element(selector)
        # noinspection PyBroadException
        try:
            self.driver.switch_to.frame(element)
            logger.info('Successful to switch_to_frame! ')
        except BaseException:
            logger.error('Failed to  switch_to_frame', exc_info=1)

    def quit_iframe(self):
        """退出当前iframe"""
        self.driver.switch_to_default_content()

    def get_title(self):
        """获取title"""
        title = self.driver.title
        logger.info('Current page title is:%s' % title)
        return title

    def quit(self):
        """关闭浏览器"""
        self.driver.quit()
        logger.info('quit the browser')


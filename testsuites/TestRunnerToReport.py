# -*- coding:utf-8 -*-
# @Time   : 2019-10-18
# @Author : Dingjs


import unittest
import HTMLTestRunner
import os
import time
'''
这个文件，只执行以下两个步骤：
1.执行用例
2.保存报告
'''

# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/report/testreports/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# HtmlFile= os.path.join(report_path,'%s.html' %now)
HtmlFile = os.path.join(report_path, now + 'xx项目web自动化测试报告.html')
fp = open(HtmlFile,'wb')

if __name__ == "__main__":
    #使用discover方法执行测试用例
    # suit = os.getcwd()
    suite=os.path.dirname(os.path.abspath('.'))
    suit = os.path.join(suite,'testsuites')

    discov = unittest.defaultTestLoader.discover(
        suit,pattern='test*.py')

    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u"xx项目测试报告",
        description=u'执行情况'
        )
    runner.run(discov)



UItestframework项目目前具有以下功能：<br>
1、对webdriver进行了第二次的简单封装，使用更加方便
</br>
2、具有打印日志的功能，打印在控制台和文件中
<br>
3、读取配置文件(.ini文件):
<br>
4、具有发邮件的功能:
<br>
5、生成测试报告：html测试报告的路径：
<br>
6、使用了PageObject模式来编写测试脚本
<br>
7、针对使用chrome浏览器，不打开浏览器，直接运行测试用例：
   =>用chrome-headless
<br>
<br>
<br>
Selenium UI 自动化测试框架（基于 python 3+selenium）
框架目录构造：<br>
|-------config： 用来存储配置文件，如 config.ini 文件，配种了所需浏览器方式及被测地址
<br>
|-------utils：框架底层封装层，可以根据自己的想法封装底层方法
<br>
|  |-------→base_page：封装了selenium库中常用的方法，包括对象查找，截图输出，浏览器的前进后退，清除和输入
<br>
|  |-------→browser_engine：通过读取配置文件去选择浏览器和url，并返回浏览器对象实例
<br>
|  |-------→log.py：封装了日志输入，包括文件输出和控制台的输出 
<br>
|-------report:测试报告和截图
<br>
|  |-------→screenshots：用于接收测试过程中错误截图文件
<br>
|  |-------→testreports：用于接收测试报告文件的输出
<br>
|-------Logs：用于接收日志文件的输出
<br>
|-------pageobjects：用于封装页面对象，
<br>
|-------testsuite：用于测试用例的存放和用例集合套件 ，示例：TestRunner.py
<br>
|-------dirvers：用于存放浏览器的 selenium 驱动

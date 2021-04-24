#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: test_grid
@time: 2021/4/22 9:51 下午
@desc:
"""
import time
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote


class TestGrid:
    """
    selenium_grid ： server上注册两个节点
    pytest-xdist插件进行并行测试, pytest test_grid.py -n 2
    分发2个请求到2个节点上进行并行测试
    """
    def setup(self):
        hub_url = "http://localhost:4444/wd/hub"
        capability = DesiredCapabilities.CHROME.copy()
        self.driver = Remote(command_executor=hub_url, desired_capabilities=capability)

    def teardown(self):
        self.driver.quit()

    def test_node1(self):
        self.driver.get("https://www.baidu.com")
        print(self.driver.page_source)
        time.sleep(5)


    def test_node2(self):
        self.driver.get("https://www.baidu.com")
        print(self.driver.page_source)
        time.sleep(5)







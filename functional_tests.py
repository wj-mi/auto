# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest


class VisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)     # 等待页面加载完成

    def tearDown(self):
        self.browser.quit()

    def test_things_list(self):
        # 小明打开浏览器，输入地址：http://localhost/，打开了一个页面
        self.browser.get("http://localhost:5001/")
        # 小明看见页面的标题和头部都包含“待办事项”这个词
        self.assertIn(u'待办事项', self.browser.title)

        # 页面包含一句欢迎语，邀请小明输入一个待办事项并点击提交按钮
        self.assertIn('welcome', self.browser.context())

        # 小明在输入框中输入了“购买《Python核心编程》”，并点击提交按钮

        # 页面中显示了“1. 购买《Python核心编程》”

        # 小明在输入框中输入了“购买《测试驱动开发》”，并点击提交按钮

        # 页面中显示了两个待办事项


if __name__ == '__main__':
    unittest.main()

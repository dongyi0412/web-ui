# -*- coding: utf-8 -*-
# @File: test_demo.py
# @Author: HanWenLu
# @E-mail: wenlupay@163.com
# @Time: 2020/10/26  11:08

import os

import pytest
import allure

from pageobj.baidu import BaiDu
from public.yaml_data import caseda

yamlfile = os.path.basename(__file__).replace('py', 'yaml')  # 获取当前目运行文件


class TestBaiDu:

    @allure.feature("百度搜索")  # 测试用例特性（主要功能模块）
    @allure.story("所搜验证")  # 模块说明
    @allure.title("输入内容并搜索")  # 用例标题
    @allure.description('输入多参数搜索')  # 用例描述
    @pytest.mark.testbaidu    # 用列标记
    @pytest.mark.parametrize('content', caseda(yamlfile, 'test_baidu_search'))   # 测试数据
    def test_baidu_search(self, webDriver,content):

        with allure.step('输入搜索内容'):

            BaiDu(webDriver).input_search_content(content)

        with allure.step('点击搜索'):

            BaiDu(webDriver).click_search_button()




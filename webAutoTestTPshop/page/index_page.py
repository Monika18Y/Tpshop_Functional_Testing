"""
首页页面
"""
import page
from base.base_page import BaseHandle, BasePage


class IndexPage(BasePage):
    """首页-对象库层"""

    def __init__(self):
        super().__init__()
        self.login_link = page.login_link  # 登录按钮
        self.search_bar = page.search_bar  # 商品搜索框
        self.search_button = page.search_button  # 搜索按钮
        self.my_order_link = page.my_order_link  # 我的订单
        self.my_cart = page.my_cart  # 我的购物车

    def find_login_link(self):
        """定位登录链接"""
        return self.find_element_func(self.login_link)

    def find_search_bar(self):
        """定位商品搜索框"""
        return self.find_element_func(self.search_bar)

    def find_search_button(self):
        """定位搜索按钮"""
        return self.find_element_func(self.search_button)

    def find_my_order_link(self):
        """定位我的订单链接"""
        return self.find_element_func(self.my_order_link)

    def find_my_cart(self):
        """定位我的购物车"""
        return self.find_element_func(self.my_cart)


class IndexHandle(BaseHandle):
    """首页-操作层"""

    def __init__(self):
        self.index_page = IndexPage()

    def click_login_link(self):
        """点击登录链接"""
        self.click_func(self.index_page.find_login_link())

    def input_search_bar(self, kw):
        """输入商品"""
        self.input_text_func(self.index_page.find_search_bar(), kw)

    def click_search_button(self):
        """点击搜索按钮"""
        self.click_func(self.index_page.find_search_button())

    def click_my_order_link(self):
        """点击我的订单"""
        self.click_func(self.index_page.find_my_order_link())

    def click_my_cart(self):
        """点击我的购物车"""
        self.click_func(self.index_page.find_my_cart())


class IndexProxy(object):
    """首页-业务层"""

    def __init__(self):
        self.index_handle = IndexHandle()

    def go_to_login(self):
        """跳转登录页面"""
        self.index_handle.click_login_link()

    def search_good(self, kw):
        """
        输入商品并点击搜索
        :param kw: 输入的商品名称
        :return: 无
        """
        self.index_handle.input_search_bar(kw)  # 输入商品
        self.index_handle.click_search_button()  # 点击搜索

    def go_to_my_order_page(self):
        """去我的订单页面"""
        self.index_handle.click_my_order_link()

    def go_to_my_cart(self):
        """去我的购物车页面"""
        self.index_handle.click_my_cart()

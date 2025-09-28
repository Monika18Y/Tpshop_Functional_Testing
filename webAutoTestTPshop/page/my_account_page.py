"""
我的账户页面
"""

from base.base_page import BasePage, BaseHandle


class MyAccountPage(BasePage):
    """我的账户-对象库层"""

    def __init__(self):
        super().__init__()
        self.my_cart_link = 'class name', 'share-shopcar-index'  # 我的购物车
        self.index_link = 'link text', '首页'  # 首页
        self.my_order_link = 'link text', '我的订单'  # 我的订单

    def find_my_cart_link(self):
        """定位我的购物车链接"""
        return self.find_element_func(self.my_cart_link)

    def find_index_link(self):
        """定位首页链接"""
        return self.find_element_func(self.index_link)

    def find_my_order_link(self):
        """定位我的订单链接"""


class MyAccountHandle(BaseHandle):
    """我的账户-操作层"""

    def __init__(self):
        self.my_account_page = MyAccountPage()

    def click_my_cart_link(self):
        """点击我的购物车"""
        self.click_func(self.my_account_page.find_my_cart_link())

    def click_index_link(self):
        """点击去首页链接"""
        self.click_func(self.my_account_page.find_index_link())

    def click_my_order_link(self):
        """点击我的订单"""
        self.click_func(self.my_account_page.find_my_order_link())


class MyAccountProxy(object):
    """我的账户-业务层"""

    def __init__(self):
        self.my_account_handle = MyAccountHandle()

    def go_to_my_cart(self):
        """去我的购物车"""
        self.my_account_handle.click_my_cart_link()

    def my_account_to_index(self):
        """从我的账户页面去首页页面"""
        self.my_account_handle.click_index_link()

    def my_account_to_order(self):
        """从我的账户去我的订单页面"""
        self.my_account_handle.click_my_order_link()

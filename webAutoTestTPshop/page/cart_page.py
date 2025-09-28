"""
购物车页面
"""
from base.base_page import BasePage, BaseHandle


class CartPage(BasePage):
    """购物车-对象库层"""

    def __init__(self):
        super().__init__()
        self.choose_all = 'class name', 'checkFull'  # 全选
        self.go_to_pay = 'css selector', 'body > div.shoplist_deta.floatflex > div > div > div > div.row_foot_last > div.column.widallr > div.butpayin > a'  # 去结算

    def find_choose_all(self):
        """定位全选按钮"""
        return self.find_element_func(self.choose_all)

    def find_go_to_pay(self):
        """定位去结算按钮"""
        return self.find_element_func(self.go_to_pay)


class CartHandle(BaseHandle):
    """购物车-操作层"""

    def __init__(self):
        self.cart_page = CartPage()

    def select_choose_all(self):
        """点击全选"""
        self.select_func(self.cart_page.find_choose_all())

    def click_go_to_pay(self):
        """点击去结算"""
        self.click_func(self.cart_page.find_go_to_pay())


class CartProxy(object):
    """购物车---操作层"""

    def __init__(self):
        self.cart_handle = CartHandle()  # 操作对象

    def go_check_order_page(self):
        """去核对订单页面"""
        self.cart_handle.select_choose_all()  # 确认全选
        self.cart_handle.click_go_to_pay()  # 去结算

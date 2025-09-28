"""
核对订单页面
"""
from base.base_page import BaseHandle, BasePage


class CheckOrderPage(BasePage):
    """核对订单-对象库层"""

    def __init__(self):
        super().__init__()
        self.submit_order = 'id', 'submit_order'

    def find_submit_order(self):
        """定位提交订单按钮"""
        return self.find_element_func(self.submit_order)


class CheckOrderHandle(BaseHandle):
    """核对订单-操作层"""

    def __init__(self):
        self.check_order_page = CheckOrderPage()

    def click_submit_order(self):
        """点击提交订单按钮"""
        self.click_func(self.check_order_page.find_submit_order())


class CheckOrderProxy(object):
    """核对订单-业务层"""

    def __init__(self):
        self.check_order_handle = CheckOrderHandle()

    def go_to_payment_page(self):
        """去支付页面"""
        self.check_order_handle.click_submit_order()

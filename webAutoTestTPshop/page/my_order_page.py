"""
我的订单页面
"""

from base.base_page import BasePage, BaseHandle
from utlis import DriverUtil


class MyOrderPage(BasePage):
    """我的订单-对象库层"""

    def __init__(self):
        super().__init__()
        self.obligation = 'link text', '立即支付'  # 提交订单
        self.immediate_payment = 'class name', 'button-confirm-payment'  # 确认支付方式
        self.driver = DriverUtil.get_driver()

    def find_obligation(self):
        """定位待付款"""
        return self.find_element_func(self.obligation)

    def find_immediate_payment(self):
        """定位立即支付"""

        # return self.find_element_func(self.immediate_payment)
        # self.driver.current_window_handle
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # return var.find_element(self.immediate_payment)
        return self.find_element_func(self.immediate_payment)


class MyOrderPageHandle(BaseHandle):
    """我的订单-操作层"""

    def __init__(self):
        self.my_order_page = MyOrderPage()

    def click_obligation(self):
        """点击待付款"""
        self.click_func(self.my_order_page.find_obligation())

    def click_immediate_payment(self):
        """点击立即支付"""
        self.click_func(self.my_order_page.find_immediate_payment())


class MyOrderProxy(object):
    """我的订单-业务层"""

    def __init__(self):
        self.my_order_handle = MyOrderPageHandle()

    def go_to_payment_page(self):
        """去支付页面"""

        self.my_order_handle.click_obligation()
        self.my_order_handle.click_immediate_payment()

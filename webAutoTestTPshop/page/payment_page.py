"""
订单支付页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class PaymentPage(BasePage):
    """支付页面-对象库层"""

    def __init__(self):
        super().__init__()
        self.order_payment_mes = By.CSS_SELECTOR, '.erhuh>h3'  # 订单提交成功信息
        self.payment_method = 'id', 'input-ALIPAY-1'  # 支付方式按钮
        self.confirm_payment = 'link text', '确认支付方式'  # 确认支付方式

    def find_order_payment_mes(self):
        """定位订单提交成功的信息"""
        return self.find_element_func(self.order_payment_mes)

    def find_payment_method(self):
        """定位支付方式"""
        return self.find_elements_func(self.payment_method, 0)

    def find_confirm_payment(self):
        """定位确认支付方式按钮"""
        return self.find_element_func(self.confirm_payment)


class PaymentHandle(BaseHandle):
    """支付页面-操作层"""

    def __init__(self):
        self.payment_page = PaymentPage()

    def get_order_payment_mes(self):
        """获取支付成功的信息"""
        return self.get_text_func(self.payment_page.find_order_payment_mes())

    def click_payment_method(self):
        """选择支付方式"""
        self.click_func(self.payment_page.find_payment_method())

    def click_confirm_payment(self):
        """点击确认支付方式"""
        self.click_func(self.payment_page.find_confirm_payment())


class PaymentProxy(object):
    """支付页面-业务层"""

    def __init__(self):
        super().__init__()
        self.payment_handle = PaymentHandle()

    def get_order_payment_mes_text(self):
        """查看支付成功信息"""
        return self.payment_handle.get_order_payment_mes()

    def choose_pay_on_delivery(self):
        """选择并确认货到付款"""
        self.payment_handle.click_payment_method()
        self.payment_handle.click_confirm_payment()

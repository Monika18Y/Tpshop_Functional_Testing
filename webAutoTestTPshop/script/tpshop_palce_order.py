"""
测试下订单&测试订单支付
"""
import unittest

from page.cart_page import CartProxy
from page.check_order_page import CheckOrderProxy
from page.index_page import IndexProxy
from page.login_page import LoginProxy
from page.my_account_page import MyAccountProxy
from page.my_order_page import MyOrderProxy
from page.payment_page import PaymentProxy
from utlis import DriverUtil, get_tip_text, switch_new_window
from time import sleep


class TestTPShopPlaceOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()
        cls.index_proxy = IndexProxy()  # 首页
        cls.login_proxy = LoginProxy()  # 登录页面
        cls.my_account_proxy = MyAccountProxy()  # 我的账户
        cls.cart_proxy = CartProxy()  # 购物车
        cls.check_order_proxy = CheckOrderProxy()  # 核对订单
        cls.payment_proxy = PaymentProxy()  # 订单支付页面
        cls.my_order_proxy = MyOrderProxy()  # 我的订单
        cls.payment_proxy = PaymentProxy()  # 订单支付

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()

    def setUp(self) -> None:
        self.driver.get('https://hmshop-test.itheima.net/')

    def tearDown(self) -> None:
        ...

    def test_01place_order(self):
        """测试下订单功能"""
        self.index_proxy.go_to_my_cart()  # 首页点击去我的购物车
        self.cart_proxy.go_check_order_page()  # 购物车页面点击去结算
        sleep(3)
        self.check_order_proxy.go_to_payment_page()  # 核对订单页面点击提交订单
        mes = get_tip_text('订单提交成功')
        # mes = self.payment_proxy.get_order_payment_mes_text() # 获取信息
        self.assertTrue(mes)

    def test_02payment(self):
        """测试支付功能"""
        self.index_proxy.go_to_my_order_page()  # 首页点击我的订单
        self.driver.refresh()
        switch_new_window()
        self.my_order_proxy.go_to_payment_page()  # 去支付页面
        self.driver.refresh()
        switch_new_window()
        self.payment_proxy.choose_pay_on_delivery()  # 选择支付方式
        mes = get_tip_text('订单提交成功')
        self.assertTrue(mes)


if __name__ == '__main__':
    unittest.main()

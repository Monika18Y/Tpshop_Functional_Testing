"""
购物车测试用例
"""
import unittest
import logging

from parameterized import parameterized
from page.good_detail_page import GoodDetailProxy
from page.index_page import IndexProxy
from page.search_list_page import SearchListProxy
from utlis import DriverUtil


class TestTPShopCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()
        cls.index_proxy = IndexProxy()  # 首页业务层
        cls.search_list_proxy = SearchListProxy()  # 搜索列表业务层
        cls.good_detail_proxy = GoodDetailProxy()  # 商品详情页面业务层

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()

    def setUp(self) -> None:
        self.driver.get('https://hmshop-test.itheima.net/')

    add_cart_data = [('小米', '小米8', '添加成功')]

    @parameterized.expand(add_cart_data)
    def test_cart(self, searh_kw, text_kw, expect):
        """加入购物车测试"""
        self.index_proxy.search_good(searh_kw)
        self.search_list_proxy.go_good_detail(text_kw)
        self.good_detail_proxy.add_cart_btn_proxy()
        mes = self.good_detail_proxy.get_add_cart_text()
        self.assertIn(expect, mes)
        logging.info(mes)


if __name__ == '__main__':
    unittest.main()

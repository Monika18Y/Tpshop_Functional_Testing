"""
商品详情页面
"""
from base.base_page import BasePage, BaseHandle
from utlis import DriverUtil


class GoodDetailPage(BasePage):
    """商品详情页-对象库层"""

    def __init__(self):
        super().__init__()
        self.add_cart_btn = 'id', 'join_cart'
        self.add_cart_btn_result = 'css selector', '#addCartBox > div.colect-top > div > span'

    def find_cart_btn(self):
        """定位加入购物车"""
        return self.find_element_func(self.add_cart_btn)

    def find_cart_btn_result(self):
        """定位加入购物车结果"""
        return self.find_element_func(self.add_cart_btn_result)


class GoodDetailHandle(BaseHandle):
    """商品详情页-操作层"""

    def __init__(self):
        self.driver = None
        self.good_detail_page = GoodDetailPage()

    def click_add_cart_btn(self):
        """点击加入购物车"""
        self.click_func(self.good_detail_page.find_cart_btn())

    def get_add_cart_btn_result(self):
        """获取加入购物车信息"""
        self.driver = DriverUtil.get_driver()
        iframe_tag = self.driver.find_elements('tag name', 'iframe')[0]
        self.driver.switch_to.frame(iframe_tag)
        return self.get_text_func(self.good_detail_page.find_cart_btn_result())


class GoodDetailProxy(object):
    """商品详情页-业务层"""

    def __init__(self):
        self.good_detail_handle = GoodDetailHandle()

    def add_cart_btn_proxy(self):
        """将商品加入购物车"""
        self.good_detail_handle.click_add_cart_btn()

    def get_add_cart_text(self):
        """获取加入购物车文本"""
        return self.good_detail_handle.get_add_cart_btn_result()

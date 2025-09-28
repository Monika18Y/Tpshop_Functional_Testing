"""
搜索列表页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class SearchListPage(BasePage):
    """搜索列表页面-对象库层"""

    def __init__(self):
        super().__init__()
        self.good_link = 'xpath', "//*[@class='shop_name2']/*[contains(text(),'{}')]"

    def find_good_link(self, kw):
        """定位搜索的商品"""
        location = self.good_link[0], self.good_link[1].format(kw)
        return self.find_element_func(location)


class SearchListHandle(BaseHandle):
    """搜索列表页面-操作层"""

    def __init__(self):
        self.search_list_page = SearchListPage()

    def click_good_link(self, kw):
        """点击商品"""
        self.click_func(self.search_list_page.find_good_link(kw))


class SearchListProxy(object):
    """搜索列表页面-业务层"""

    def __init__(self):
        self.search_list_proxy = SearchListHandle()

    def go_good_detail(self, kw):
        """
        去商品详情页
        :param kw: 定位商品文本部分内容
        :return: 无
        """
        self.search_list_proxy.click_good_link(kw)

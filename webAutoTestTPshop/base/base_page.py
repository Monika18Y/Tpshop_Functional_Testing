"""
PO 文件基类
"""
from utlis import DriverUtil


class BasePage(object):
    """对象库层基类"""

    def __init__(self):
        self.driver = DriverUtil.get_driver()  # 获取浏览器对象

    def find_element_func(self, location):
        """
        element页面元素定位方法
        :param location: 定位方法和定位数据
        :return: 页面元素
        """
        return self.driver.find_element(location[0], location[1])

    def find_elements_func(self, location, num):
        """
        elements页面元素定位方法
        :param location: 定位方法和定位数据
        :param num: 索引
        :return: 页面元素
        """
        # elements = self.driver.find_elements(location[0], location[1])
        # return elements[num]
        return self.driver.find_elements(location[0], location[1])[num]

class BaseHandle(object):
    """操作层基类"""

    def input_text_func(self, element, text):
        """
        元素输入方法
        :param element: 页面元素
        :param text: 输入内容
        :return: 无
        """
        element.clear()  # 清空
        element.send_keys(text)  # 输入

    def click_func(self, element):
        """
        元素点击方法
        :param element: 页面元素
        :return: 无
        """
        element.click()

    def get_text_func(self, element):
        """
        获取文本信息
        :param element: 页面元素
        :return: 返回文本信息
        """
        return element.text

    def select_func(self, element):
        """
        单选或复选框未选中，则点击选中，选中不操作
        :param element: 页面元素
        :return: 无
        """
        choose = element.is_selected()
        if not choose:
            element.click()

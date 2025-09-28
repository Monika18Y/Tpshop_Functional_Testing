"""
登录页面
"""
import page
from base.base_page import BasePage, BaseHandle


class LoginPage(BasePage):
    """登录-对象库层"""

    def __init__(self):
        super().__init__()
        # self.user_mobile = By.ID, 'username'  # 手机号
        # self.psw = By.ID, 'password'  # 密码
        # self.code = By.ID, 'verify_code'  # 验证码
        # self.login = By.CLASS_NAME, 'J-login-submit'  # 登录按钮

    def find_user_mobile(self):
        """定位用户名"""
        return self.find_element_func(page.user_mobile)

    def find_psw(self):
        """定位密码"""
        return self.find_element_func(page.psw)

    def find_code(self):
        """定位验证码"""
        return self.find_element_func(page.code)

    def find_login(self):
        """定位登录按钮"""
        return self.find_element_func(page.login)


class LoginHandle(BaseHandle):
    """登录-操作层"""

    def __init__(self):
        self.login_page = LoginPage()

    def input_user_mobile(self, user_mobile):
        """输入用户名"""
        self.input_text_func(self.login_page.find_user_mobile(), user_mobile)

    def input_psw(self, psw):
        """输入密码"""
        self.input_text_func(self.login_page.find_psw(), psw)

    def input_code(self, code):
        """输入验证码"""
        self.input_text_func(self.login_page.find_code(), code)

    def click_login(self):
        """点击登录按钮"""
        self.click_func(self.login_page.find_login())


class LoginProxy(object):
    """登录-业务层"""

    def __init__(self):
        self.login_handle = LoginHandle()

    def user_login(self, user_mobile, psw, code):
        """用户登录操作"""
        self.login_handle.input_user_mobile(user_mobile)  # 用户名
        self.login_handle.input_psw(psw)  # 密码
        self.login_handle.input_code(code)  # 验证码
        self.login_handle.click_login()  # 点击登录

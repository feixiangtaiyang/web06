import pytest
from pages.users_login_page import UsersLoginPage


class TestUserLoginPage():

    @pytest.fixture(autouse=True)
    def open_register(self, usersLoginPage:UsersLoginPage):
        usersLoginPage.open("/users/login/")

    def test_users_login_1(self, usersLoginPage:UsersLoginPage):
        '''登录-输入用户名为空，任意密码123456,点登陆按钮，提示：这个字段是必须的'''
        usersLoginPage.input_login_username("")
        usersLoginPage.input_login_password("123456")
        usersLoginPage.click_login_btn()
        # 断言
        assert usersLoginPage.get_error_tips() == "这个字段是必须的"


    def test_users_login_2(self, usersLoginPage:UsersLoginPage):
        '''登录-输入邮箱格式不正确“123abc” ,密码123456,点登陆按钮，提示:用户名或密码错误'''
        usersLoginPage.input_login_username("123abc")
        usersLoginPage.input_login_password("123456")
        usersLoginPage.click_login_btn()
        # 断言
        assert usersLoginPage.get_error_tips() == "用户名或密码错误"

    def test_users_login_3(self, usersLoginPage:UsersLoginPage):
        '''登录-邮箱格式正确123@qq.com，密码不对:111111，提示：用户名或密码错误 '''
        usersLoginPage.input_login_username("123@qq.com")
        usersLoginPage.input_login_password("111111")
        usersLoginPage.click_login_btn()
        # 断言
        assert usersLoginPage.get_error_tips() == "用户名或密码错误"

    def test_users_login_4(self, usersLoginPage:UsersLoginPage, base_url):
        '''登录-输入正确的邮箱1234@qq.com，正确的密码:123456，登录成功'''
        usersLoginPage.input_login_username("1234@qq.com")
        usersLoginPage.input_login_password("123456")
        usersLoginPage.click_login_btn()
        # 断言
        assert usersLoginPage.get_error_tips() == ""
        # 判断跳转的url
        url = usersLoginPage.driver.current_url
        print("获取跳转后的url", url)
        assert url == base_url + "/"





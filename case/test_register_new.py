from pages.register_page import RegisterPage
import pytest

class TestRegisterPageNew():

    @pytest.fixture(autouse=True)
    def open_register(self, registerPage:RegisterPage):
        registerPage.open("/users/register/")


    def test_email_1(self, registerPage:RegisterPage):
        ''' 注册-输入邮箱为空，密码为空，
        点提交按钮，邮箱输入框红色提示 (class属性包含errorput)'''
        # registerPage.open("/users/register/")
        registerPage.input_email("")
        registerPage.input_password("")
        registerPage.click_register_btn()
        # 实际结果
        actual_result = registerPage.get_email_class()
        print("实际结果", actual_result)
        # 断言
        assert "errorput" in actual_result


    def test_email_2(self, registerPage:RegisterPage):
        ''' 注册-邮箱格式不正确，密码为空，
        点提交按钮，邮箱输入框红色提示(class 属性包含errorput)'''
        # registerPage.open("/users/register/")
        registerPage.input_email("1234")
        registerPage.input_password("")
        registerPage.click_register_btn()
        # 实际结果
        actual_result = registerPage.get_email_class()
        print("实际结果", actual_result)
        # 断言
        assert "errorput" in actual_result

    def test_password_3(self, registerPage:RegisterPage):
        '''
        注册-邮箱格式正确(111@qq.com),密码为空，
        点提交按钮，密码框提示红色（class属性errorput）
        :return:
        '''
        # registerPage.open("/users/register/")
        registerPage.input_email("1234@qq.com")
        registerPage.input_password("")
        registerPage.click_register_btn()
        # 实际结果
        actual_result = registerPage.get_password_class()
        print("实际结果", actual_result)
        # 断言
        assert "errorput" in actual_result

    def test_password_4(self, registerPage:RegisterPage):
        '''
        注册-邮箱格式正确(111@qq.com), 密码小于6位，
        点提交按钮，密码框提示红色（class属性errorput）
        :return:
        '''
        # registerPage.open("/users/register/")
        registerPage.input_email("1234@qq.com")
        registerPage.input_password("12345")
        registerPage.click_register_btn()
        # 实际结果
        actual_result = registerPage.get_password_class()
        print("实际结果", actual_result)
        # 断言
        assert "errorput" in actual_result

    def test_password_5(self, registerPage:RegisterPage):
        '''
        注册-邮箱格式正确(111@qq.com), 密码大于20位，
        点提交按钮，密码框提示红色（class属性errorput）
        :return:
        '''
        # registerPage.open("/users/register/")
        registerPage.input_email("1234@qq.com")
        registerPage.input_password("1234567890123456789012")
        registerPage.click_register_btn()
        # 实际结果
        actual_result = registerPage.get_password_class()
        print("实际结果", actual_result)
        # 断言
        assert "errorput" in actual_result

    def test_email_input_6(self, registerPage:RegisterPage):
        '''注册-邮箱输入框，输入文本：111@qq.com，再清空文本，输入框为空'''
        registerPage.input_email("123@qq.com")
        assert registerPage.get_email_attr(attr="value") == "123@qq.com"

        # 清空输入框
        registerPage.clear_email()
        assert registerPage.get_email_attr(attr="value") == ""

    def test_password_input_7(self, registerPage:RegisterPage):
        '''注册-密码框输入文本：123456，显示******'''
        registerPage.input_password("123456")
        assert registerPage.get_password_attr(attr="value") == "123456"

        # 判断输入框显示*****
        assert registerPage.get_password_attr(attr="type") == "password"

    def test_register_link_8(self, registerPage:RegisterPage, base_url):
        '''注册-点页面“回到首页”按钮，点击跳转到首页/'''
        link = registerPage.get_link_href('//*[@class="index-font"]')
        print("实际结果：%s" % link)  # http://49.235.92.12:8200/
        assert link == base_url+"/"

    def test_register_link_9(self, registerPage:RegisterPage, base_url):
        '''注册-点页面“logo图片”按钮，点击跳转到首页/'''
        link = registerPage.get_link_href('//*[@class="index-logo"]')
        print("实际结果：%s" % link)  # http://49.235.92.12:8200/
        assert link == base_url+"/"

    def test_register_link_10(self, registerPage:RegisterPage, base_url):
        '''注册-点页面“登陆”按钮，点击跳转到登陆页/users/login/'''
        link = registerPage.get_link_href('//*[text()="[登录]"]')
        print("实际结果：%s" % link)
        assert link == base_url+"/users/login/"

    def test_register_link_11(self, registerPage:RegisterPage, base_url):
        '''注册-点页面“注册”按钮，点击跳转到登陆页/users/register/'''
        link = registerPage.get_link_href('//*[text()="[注册]"]')
        print("实际结果：%s" % link)
        assert link == base_url+"/users/register/"

    def test_register_link_12(self, registerPage:RegisterPage, base_url):
        '''注册-点页面“立即登陆”按钮，点击跳转到登陆页/users/login/'''
        link = registerPage.get_link_href('//*[text()="[立即登录]"]')
        print("实际结果：%s" % link)
        assert link == base_url+"/users/login/"


        














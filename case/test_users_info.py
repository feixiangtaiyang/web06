from pages.users_userinfo_page import UsersUserInfoPage
import pytest


class TestUsersUserInfoPage():

    @pytest.fixture(autouse=True)
    def open(self, userInfoPage:UsersUserInfoPage):
        '''直接进入到个人资料页面'''
        userInfoPage.open("/users/userinfo/")

    def test_userinfo_1(self, userInfoPage:UsersUserInfoPage):
        '''个人信息-修改昵称为空，点保存，提示：请输入昵称！'''
        userInfoPage.clear_nick_name()
        userInfoPage.input_nick_name("")
        userInfoPage.click_save_btn()
        tips = userInfoPage.get_error_tips()
        assert tips == "请输入昵称！"

    @pytest.mark.parametrize("test_input", ["上海-悠悠", "yoyo"])
    def test_userinfo_2(self, userInfoPage:UsersUserInfoPage, test_input):
        '''个人信息-修改昵称：上海-悠悠，点保存，提示：个人信息修改成功'''
        userInfoPage.clear_nick_name()
        userInfoPage.input_nick_name(test_input)
        userInfoPage.click_save_btn()
        dialog = userInfoPage.get_dialog_text()
        assert dialog == "个人信息修改成功！"
        # 再查看昵称显示
        assert userInfoPage.get_nick_value() == test_input

    def test_userinfo_3(self, userInfoPage:UsersUserInfoPage):
        '''个人信息-修改昵称：yoyoabcdefa，大于10个字符 ，输入框只多显示10个字符'''
        userInfoPage.clear_nick_name()
        userInfoPage.input_nick_name("yoyoabcdefa")
        assert userInfoPage.get_nick_value() == "yoyoabcdef"

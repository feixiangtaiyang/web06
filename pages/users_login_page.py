from common.base import Base


class UsersLoginPage(Base):
    '''用户登录页'''

    login_username_loc = ("id", "username")
    login_password_loc = ("id", "password_l")
    login_btn_loc = ("id", "jsLoginBtn")

    error_tips_loc = ("class name", "errorlist")
    tips_loc = ("id", "jsLoginTips")


    def input_login_username(self, user=""):
        '''登录用户名'''
        self.send(self.login_username_loc, user)

    def input_login_password(self, password=""):
        '''登录密码'''
        self.send(self.login_password_loc, password)

    def click_login_btn(self):
        '''点立即登录按钮'''
        self.click(self.login_btn_loc)

    def get_error_tips(self):
        '''获取页面提示语'''
        tips = self.get_text(self.error_tips_loc)
        if not tips:
            tips = self.get_text(self.tips_loc)
        return tips




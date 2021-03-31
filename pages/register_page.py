from common.base import Base


class RegisterPage(Base):
    '''注册页'''

    email_loc = ("id", "id_email")
    # /..定位父元素
    email_div_loc = ("xpath", "//*[@id='id_email']/..")
    password_loc = ("id", "id_password")
    password_div_loc = ("xpath", "//*[@id='id_password']/..")
    btn_loc = ("id", "jsEmailRegBtn")

    back_index_loc = ("class name", "index-font")
    login_link_loc = ("css selector", ".form-p>a")

    # 注册成功
    success_loc = ("css selector", "body>h1")


    def input_email(self, text):
        '''输入邮箱'''
        self.send(self.email_loc, text)

    def input_password(self, text):
        '''输入密码'''
        self.send(self.password_loc, text)

    def click_register_btn(self):
        '''点注册按钮'''
        self.click(self.btn_loc)

    def register_success_text(self):
        '''获取注册成功的文本'''
        return self.get_text(self.success_loc)

    def get_email_class(self):
        '''获取邮箱输入框class属性'''
        return self.get_attribute(self.email_div_loc, "class")

    def get_password_class(self):
        '''获取密码输入框class属性'''
        return self.get_attribute(self.password_div_loc, "class")

    def clear_email(self):
        '''清空邮箱输入框'''
        self.clear(self.email_loc)

    def get_email_attr(self, attr="value"):
        '''获取邮箱的属性'''
        return self.get_attribute(self.email_loc, attr)

    def get_password_attr(self, attr="type"):
        '''获取密码输入框的属性'''
        return self.get_attribute(self.password_loc, attr)

    def get_link_href(self, xpath_loc):
        '''获取a标签的href属性, xpath定位'''
        loc = ("xpath", xpath_loc)
        return self.get_attribute(loc, "href")








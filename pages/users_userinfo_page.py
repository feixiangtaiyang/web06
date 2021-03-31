from common.base import Base
import time


class UsersUserInfoPage(Base):

    nick_name_loc = ("id", "nick_name")
    save_btn_loc = ("id", "jsEditUserBtn")
    error_tips_loc = ("class name", "error-tips")
    dialog_loc = ("css selector", "#jsSuccessTips>.cont")

    def clear_nick_name(self):
        '''清空昵称'''
        self.clear(self.nick_name_loc)

    def input_nick_name(self, name=""):
        '''输入昵称'''
        self.send(self.nick_name_loc, name)

    def get_nick_value(self):
        '''获取输入内容'''
        return self.get_attribute(self.nick_name_loc, "value")

    def click_save_btn(self):
        '''点击保存按钮'''
        self.click(self.save_btn_loc)

    def get_error_tips(self):
        '''获取tips提示语'''
        return self.get_text(self.error_tips_loc)

    def get_dialog_text(self):
        '''获取dialog弹窗内容'''
        time.sleep(0.2)
        dialog = self.get_text(self.dialog_loc)
        return dialog


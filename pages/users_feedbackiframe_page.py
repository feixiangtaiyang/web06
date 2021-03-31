from common.base import Base

class UsersFeedbackiframePage(Base):
    '''意见反馈页面'''

    iframe_loc = ("id", "feedback_iframe")
    select_loc = ("name", "subject")
    textarea_loc = ("id", "message")
    email_loc = ("name", "email")
    send_btn_loc = ("class name", "button")

    def to_iframe(self):
        '''切换到iframe页面'''
        self.switch_iframe(self.iframe_loc)

    def select_subject(self, value=""):
        '''选中下拉选项'''
        self.select_by_value(self.select_loc, value)

    def all_subjects(self):
        '''获取所有的选项'''
        all_options = self.select_object(self.select_loc).options  # 返回list of 元素对象
        all_text = [i.text for i in all_options]
        return all_text

    def selected_subject(self):
        '''获取被选中的选项'''
        selected = self.select_object(self.select_loc).first_selected_option
        return selected.text

    def input_feedback_textarea(self, text=""):
        '''输入反馈内容'''
        self.send(self.textarea_loc, text)

    def input_feedback_email(self, text=""):
        '''输入联系方式'''
        self.send(self.email_loc, text)

    def click_send_btn(self):
        '''点send按钮'''
        self.click(self.send_btn_loc)



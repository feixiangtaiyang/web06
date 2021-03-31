import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import platform
import time
from pages.register_page import RegisterPage
from common.connect_msysql import DbConnect, dbinfo
from pages.users_login_page import UsersLoginPage
from pages.users_feedbackiframe_page import UsersFeedbackiframePage
from pages.users_userinfo_page import UsersUserInfoPage




# 下面的方式可以判断当前系统是windows还是linux


@pytest.fixture(scope="session", name="driver")
def browser():
    '''定义全局driver'''
    if platform.system() == 'Windows':
        # windows系统有界面
        # _driver = webdriver.Chrome()
        # _driver.maximize_window


        #window无界面
        chrome_options = Options()
        chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
        chrome_options.add_argument('--headless')  # 无界面
        _driver = webdriver.Chrome(chrome_options=chrome_options)



    else:
        # linux启动
        chrome_options = Options()
        chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
        chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在报错问题
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')   # 禁用GPU硬件加速。如果软件渲染器没有就位，则GPU进程将不会启动。
        chrome_options.add_argument('--headless')  # 无界面

        # _driver = webdriver.Chrome()
        _driver = webdriver.Chrome(chrome_options=chrome_options)

    yield _driver
    # quit是退出浏览器
    _driver.quit()


@pytest.fixture(scope="session")
def base_url():
    url = "http://49.235.92.12:8200"
    return url

@pytest.fixture(scope="session")
def db():
    _db = DbConnect(dbinfo, "online")
    yield _db
    _db.close()


@pytest.fixture(scope="session")
def registerPage(driver, base_url):
    register = RegisterPage(driver, base_url)
    return register

@pytest.fixture(scope="session")
def usersLoginPage(driver, base_url):
    usersLogin = UsersLoginPage(driver, base_url)
    return usersLogin


@pytest.fixture(scope="session")
def usersFeedbackPage(driver, base_url):
    feedback = UsersFeedbackiframePage(driver, base_url)
    return feedback

@pytest.fixture(scope="session")
def login_driver(driver, usersLoginPage:UsersLoginPage):
    '''用户先登陆，返回driver'''
    usersLoginPage.open("/users/login/")
    usersLoginPage.input_login_username("1234@qq.com")
    usersLoginPage.input_login_password("123456")
    usersLoginPage.click_login_btn()
    return driver


@pytest.fixture(scope="session")
def userInfoPage(login_driver, base_url):
    '''需先登陆, 返回已登陆的页面对象'''
    userInfo = UsersUserInfoPage(login_driver, base_url)
    return userInfo
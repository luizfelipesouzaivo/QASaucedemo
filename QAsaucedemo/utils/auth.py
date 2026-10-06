from config.settings import SAUCE_PASSWORD, SAUCE_USERNAME
from pages.login_page import LoginPage


def login_as_standard_user(page):
    login = LoginPage(page)
    login.open()
    login.login(SAUCE_USERNAME, SAUCE_PASSWORD)
    login.assert_logged_in()
    return login

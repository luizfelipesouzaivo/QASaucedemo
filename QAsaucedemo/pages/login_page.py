from playwright.sync_api import expect
from config.settings import BASE_URL


class LoginPage:
    URL = BASE_URL

    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")

    def open(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_logged_in(self):
        expect(self.page).to_have_url("**/inventory.html")

    def assert_error_visible(self):
        expect(self.error_message).to_be_visible()

    def error_text(self) -> str:
        return self.error_message.inner_text()

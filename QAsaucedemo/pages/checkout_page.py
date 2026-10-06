from playwright.sync_api import expect


class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.error_message = page.locator("[data-test='error']")
        self.complete_message = page.locator(".complete-header")
        self.summary_items = page.locator(".cart_item")

    def fill_customer_data(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_to_summary(self):
        self.continue_button.click()
        expect(self.page).to_have_url("**/checkout-step-two.html")

    def finish(self):
        self.finish_button.click()
        expect(self.page).to_have_url("**/checkout-complete.html")

    def assert_error_visible(self):
        expect(self.error_message).to_be_visible()

    def assert_success_message(self):
        expect(self.complete_message).to_have_text("Thank you for your order!")

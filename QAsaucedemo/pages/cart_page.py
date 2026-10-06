from playwright.sync_api import expect


class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator("#checkout")
        self.continue_shopping_button = page.locator("[data-test='continue-shopping']")

    def item_count(self) -> int:
        return self.cart_items.count()

    def remove_product(self, product_id: str):
        self.page.locator(f"#remove-{product_id}").click()

    def checkout(self):
        self.checkout_button.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()
        expect(self.page).to_have_url("**/inventory.html")

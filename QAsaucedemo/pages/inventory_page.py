from playwright.sync_api import expect


class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.products = page.locator(".inventory_item")
        self.product_prices = page.locator(".inventory_item_price")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.sort_dropdown = page.locator(".product_sort_container")
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")
        self.menu = page.locator(".bm-menu")

    def product_count(self) -> int:
        return self.products.count()

    def add_product(self, product_id: str):
        self.page.locator(f"#add-to-cart-{product_id}").click()

    def remove_product(self, product_id: str):
        self.page.locator(f"#remove-{product_id}").click()

    def cart_quantity(self) -> int:
        return int(self.cart_badge.inner_text()) if self.cart_badge.is_visible() else 0

    def open_cart(self):
        self.cart_link.click()

    def sort_by(self, value: str):
        self.sort_dropdown.select_option(value)

    def prices(self) -> list[float]:
        return [float(price.replace("$", "")) for price in self.product_prices.all_inner_texts()]

    def open_menu(self):
        self.menu_button.click()
        expect(self.menu).to_be_visible()

    def logout(self):
        self.open_menu()
        self.logout_link.click()
        expect(self.page).to_have_url("**/")

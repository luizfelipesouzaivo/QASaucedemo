import pytest
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from utils.auth import login_as_standard_user


def prepare_checkout(page):
    login_as_standard_user(page)
    inventory = InventoryPage(page)
    inventory.add_product("sauce-labs-backpack")
    inventory.open_cart()
    cart = CartPage(page)
    cart.checkout()
    return CheckoutPage(page)


@pytest.mark.smoke
@pytest.mark.checkout
def test_checkout_completo(page):
    checkout = prepare_checkout(page)

    checkout.fill_customer_data("Luiz", "Felipe", "21900000")
    checkout.continue_to_summary()
    assert checkout.summary_items.count() == 1

    checkout.finish()
    checkout.assert_success_message()


@pytest.mark.regression
@pytest.mark.checkout
@pytest.mark.parametrize(
    "first_name,last_name,postal_code",
    [
        ("", "Felipe", "21900000"),
        ("Luiz", "", "21900000"),
        ("Luiz", "Felipe", ""),
    ],
)
def test_checkout_deve_validar_campos_obrigatorios(page, first_name, last_name, postal_code):
    checkout = prepare_checkout(page)

    checkout.fill_customer_data(first_name, last_name, postal_code)
    checkout.continue_button.click()

    checkout.assert_error_visible()

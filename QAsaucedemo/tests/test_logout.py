import pytest
from pages.inventory_page import InventoryPage
from utils.auth import login_as_standard_user


@pytest.mark.smoke
@pytest.mark.navigation
def test_logout_deve_retornar_para_login(page):
    login_as_standard_user(page)
    inventory = InventoryPage(page)

    inventory.logout()

    assert page.url.rstrip("/") == "https://www.saucedemo.com"
    assert login_button_visible(page)


def login_button_visible(page):
    return page.locator("#login-button").is_visible()

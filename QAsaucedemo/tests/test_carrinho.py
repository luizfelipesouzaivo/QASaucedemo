import pytest
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from utils.auth import login_as_standard_user


@pytest.mark.smoke
@pytest.mark.cart
def test_acessar_carrinho_com_produto(page):
    login_as_standard_user(page)
    inventory = InventoryPage(page)
    inventory.add_product("sauce-labs-backpack")
    inventory.open_cart()

    cart = CartPage(page)

    assert cart.item_count() == 1


@pytest.mark.regression
@pytest.mark.cart
def test_adicionar_dois_produtos_no_carrinho(page):
    login_as_standard_user(page)
    inventory = InventoryPage(page)
    inventory.add_product("sauce-labs-backpack")
    inventory.add_product("sauce-labs-bike-light")
    inventory.open_cart()

    cart = CartPage(page)

    assert cart.item_count() == 2


@pytest.mark.regression
@pytest.mark.cart
def test_remover_produto_do_carrinho(page):
    login_as_standard_user(page)
    inventory = InventoryPage(page)
    inventory.add_product("sauce-labs-backpack")
    inventory.open_cart()

    cart = CartPage(page)
    cart.remove_product("sauce-labs-backpack")

    assert cart.item_count() == 0


@pytest.mark.regression
@pytest.mark.cart
def test_continuar_comprando_deve_retornar_para_produtos(page):
    login_as_standard_user(page)
    inventory = InventoryPage(page)
    inventory.add_product("sauce-labs-backpack")
    inventory.open_cart()

    cart = CartPage(page)
    cart.continue_shopping()

    assert "inventory.html" in page.url

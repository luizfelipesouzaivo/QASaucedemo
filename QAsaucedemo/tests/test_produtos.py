import pytest
from pages.inventory_page import InventoryPage
from utils.auth import login_as_standard_user


@pytest.mark.smoke
@pytest.mark.productos
def test_lista_produtos_deve_conter_seis_produtos(page):
    login_as_standard_user(page)
    inventory = InventoryPage(page)

    assert inventory.product_count() == 6


@pytest.mark.regression
@pytest.mark.products
def test_adicionar_produto_deve_atualizar_carrinho(page):
    login_as_standard_user(page)
    inventory = InventoryPage(page)

    inventory.add_product("sauce-labs-backpack")

    assert inventory.cart_quantity() == 1


@pytest.mark.regression
@pytest.mark.products
def test_adicionar_dois_produtos_deve_atualizar_carrinho(page):
    login_as_standard_user(page)
    inventory = InventoryPage(page)

    inventory.add_product("sauce-labs-backpack")
    inventory.add_product("sauce-labs-bike-light")

    assert inventory.cart_quantity() == 2


@pytest.mark.regression
@pytest.mark.products
def test_ordenacao_por_menor_preco_deve_ser_crescente(page):
    login_as_standard_user(page)
    inventory = InventoryPage(page)

    inventory.sort_by("lohi")
    prices = inventory.prices()

    assert prices == sorted(prices)


@pytest.mark.regression
@pytest.mark.products
def test_ordenacao_por_maior_preco_deve_ser_decrescente(page):
    login_as_standard_user(page)
    inventory = InventoryPage(page)

    inventory.sort_by("hilo")
    prices = inventory.prices()

    assert prices == sorted(prices, reverse=True)

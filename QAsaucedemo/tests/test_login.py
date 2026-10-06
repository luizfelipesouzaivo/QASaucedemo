import pytest
from pages.login_page import LoginPage


@pytest.mark.smoke
@pytest.mark.login
def test_login_com_sucesso(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    login.assert_logged_in()


@pytest.mark.regression
@pytest.mark.login
@pytest.mark.parametrize(
    "username,password",
    [
        ("usuario_invalido", "secret_sauce"),
        ("standard_user", "senha_errada"),
        ("", "secret_sauce"),
        ("standard_user", ""),
    ],
)
def test_login_com_credenciais_invalidas(page, username, password):
    login = LoginPage(page)
    login.open()
    login.login(username, password)
    login.assert_error_visible()

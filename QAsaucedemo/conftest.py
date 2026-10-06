from pathlib import Path
import pytest
from playwright.sync_api import Page, sync_playwright
from config.settings import DEFAULT_TIMEOUT, HEADLESS, SLOW_MO

ARTIFACTS_DIR = Path(__file__).parent / "test-results"


@pytest.fixture
def page():
    ARTIFACTS_DIR.mkdir(exist_ok=True)
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=HEADLESS, slow_mo=SLOW_MO)
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()
        page.set_default_timeout(DEFAULT_TIMEOUT)
        yield page
        context.close()
        browser.close()


@pytest.fixture
def authenticated_page(page: Page):
    from pages.login_page import LoginPage
    from config.settings import SAUCE_PASSWORD, SAUCE_USERNAME

    login = LoginPage(page)
    login.open()
    login.login(SAUCE_USERNAME, SAUCE_PASSWORD)
    login.assert_logged_in()
    return page


def pytest_runtest_makereport(item, call):
    if call.when != "call":
        return
    report = call.excinfo
    if report is None:
        return
    page = item.funcargs.get("page")
    if page is None:
        return
    try:
        path = ARTIFACTS_DIR / f"{item.nodeid.replace('::', '__').replace('/', '_')}.png"
        page.screenshot(path=str(path), full_page=True)
    except Exception:
        pass

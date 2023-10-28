import pytest


@pytest.fixture
def browser_login(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(url="https://www.saucedemo.com/")
    page.locator("#user-name").type("standard_user", delay=20)
    page.locator("#password").type("secret_sauce", delay=20)
    page.click(selector="#login-button")
    page.wait_for_timeout(2000)
    context.storage_state(path="state.json")
    yield page
    context.close()


@pytest.fixture
def browser_saved_login(browser_login):
    context = browser_login.context.browser.new_context(storage_state="state.json")
    page = context.new_page()
    page.goto(url="https://www.saucedemo.com/inventory-item.html?id=4")
    yield page



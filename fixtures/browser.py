import pytest
from playwright.sync_api import sync_playwright, Playwright, Page

# FIRST METHOD

# @pytest.fixture
# def browser_context():
#     p = sync_playwright().start()
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#     yield context
#     browser.close()
#     p.stop()

# SECOND METHOD
@pytest.fixture(scope="session")
def browser(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    yield browser
    browser.close()
    playwright.stop()

@pytest.fixture
def browser_context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture
def page(page: Page):
    page.goto(url="https://google.com")
    yield page
    page.close()
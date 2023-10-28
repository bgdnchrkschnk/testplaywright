import pytest
# from playwright.sync_api import sync_playwright, Playwright, Page

# FIRST METHOD

# @pytest.fixture
# def browser_context():
#     p = sync_playwright().start()
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#     yield context
#     browser.close()
#     p.stop()

# # SECOND METHOD
# @pytest.fixture(scope="function")
# def browser(playwright):
#     browser = playwright.firefox.launch(headless=False)
#     yield browser
#     browser.close()
#     playwright.stop()
# #
# @pytest.fixture
# def page(browser):
#     context = browser.new_context()
#     yield context
#     context.close()

# @pytest.fixture(scope="function")
# def page(page):
#     page.goto(url="")
#     yield page

@pytest.fixture()
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    # page.set_viewport_size({"width":1600, "height":800})
    page.goto(url="https://ask.fm/login")
    yield page
    context.close()

import os
from playwright.sync_api import expect

import pytest

class Tests:
    @pytest.mark.this
    def test_login(self, browser_context):
        page = browser_context.new_page()
        # page.set_viewport_size({"width": 2560, "height": 1800})
        page.goto(url="https://ask.fm/login")
        assert "https://ask.fm/login" in page.url
        page.locator("#user_name").type("bgdnchrkschnk")
        page.locator("#user_password").type("2445253")
        page.screenshot(timeout=1000, path="./screenshots/login.png")
        page.locator("input[type=submit]").click()
        page.wait_for_timeout(4000)
        page.screenshot(path="./screenshots/private_cabinet.png")
        page.wait_for_timeout(3000)
        test = page.locator(selector="pb-3.p-4")
        if not page.locator(selector=".captcha-container"):
            assert "account/wall" in page.url, "URL WRONG"
            assert expect(page.locator(selector="pb-3.p-4")).to_be_visible(), "Ask block is not recognized on page!"
            assert "Стена" in page.title(), f"Page title is wrong - '{page.title()}'"

    @pytest.mark.parametrize("login, pw", [("dimasik", "ehfwhie"), ("alinchik", "5327632")])
    def test_invalid_login(self, browser_context, login, pw):
        page = browser_context.new_page()
        # page.set_viewport_size({"width": 2560, "height": 1800})
        page.goto(url="https://ask.fm/login")
        assert "https://ask.fm/login" in page.url
        page.locator("#user_name").type(login)
        page.locator("#user_password").type(pw)
        page.screenshot(timeout=1000, path="./screenshots/login.png")
        page.locator("input[type=submit]").click()
        page.wait_for_timeout(4000)
        page.screenshot(path="./screenshots/private_cabinet.png")
        assert page.locator(selector="p.rsp-container"), f"Invalid creds block admonition is not recognized on page!"

    @pytest.mark.test
    def test_page(self, page):
        page.locator(selector="textarea.gLFyf").type(delay=0.03, text="iPhone 13 Green")
        page.keyboard.press(key="Enter")
        page.wait_for_timeout(3000)



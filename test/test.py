import os
from playwright.sync_api import expect

import pytest

class Tests:
    # @pytest.mark.this
    def test_login(self, page):
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

    @pytest.mark.parametrize("login, pw", [("dimasik", "ehfwhie"), ("alinchik", "5327632"), pytest.param("dedjid", "cneui", marks=pytest.mark.xfail)])
    def test_invalid_login(self, page, login, pw):
        assert "https://ask.fm/login" in page.url
        page.locator("#user_name").type(login)
        page.locator("#user_password").type(pw)
        page.screenshot(timeout=1000, path="./screenshots/login.png")
        page.locator("input[type=submit]").click()
        page.wait_for_timeout(5000)
        page.screenshot(path="./screenshots/private_cabinet.png")
        assert page.locator(selector="p.rsp-container"), f"Invalid creds block admonition is not recognized on page!"



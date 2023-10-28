import ast
import os
import string

from playwright.sync_api import expect

import pytest

class Tests:
    @staticmethod
    def clear_input(page, locator):
        return page.locator(locator).fill("")

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
        page.reload()
        test = page.locator(selector="pb-3.p-4")
        if not page.locator(selector=".captcha-container"):
            assert "account/wall" in page.url, "URL WRONG"
            assert expect(page.locator(selector="pb-3.p-4")).to_be_visible(), "Ask block is not recognized on page!"
            assert "Стена" in page.title(), f"Page title is wrong - '{page.title()}'"

    # @pytest.mark.this
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

    @pytest.mark.only
    def test_go_back_forward(self, page):
        page.get_by_role("link", name="Sign up").click()
        page.wait_for_timeout(1000)
        page.go_back()
        page.wait_for_timeout(1000)
        page.go_forward()
        page.wait_for_timeout(1000)
        page.go_back()
        page.type(selector="#user_name", text="something..", delay=20)
        page.wait_for_timeout(7000)
        page.reload()
        # self.clear_input(page=page, locator="#user_name")
        print(page.locator("input#user_name").input_value())
        # page.wait_for_timeout(2000)
        # page.click(selector="//input[@type='submit']")
        # page.wait_for_timeout(2000)
        # admonition = page.locator(selector=".flash-message")
        # assert admonition.is_visible(), "Not visible"
        # print(admonition.inner_text())
        # assert "You forgot to fill" in admonition.inner_text(), "Text is absent!"






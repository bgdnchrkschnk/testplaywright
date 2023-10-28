

def test_user_is_logged_in(browser_login):
    page = browser_login
    assert page.locator("#inventory-container"), "Not visible!"

def test_user_logout(browser_login):
    page = browser_login
    page.click(".bm-burger-button")
    page.click("#logout_sidebar_link")
    assert page.locator("login-button"), "Login button is not visible!"

def test_product_item(browser_saved_login):
    browser_saved_login.wait_for_timeout(4500)
    assert browser_saved_login.locator("#add-to-cart-sauce-labs-backpack", has_text="Add to cart").is_visible()
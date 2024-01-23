
# в корзину
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://oz.by/")
    page.get_by_role("link", name="0,13").click()
    page.get_by_role("button", name=" Положить в корзину").click()

    # ---------------------
    context.close()
    browser.close()



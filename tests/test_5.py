from playwright.sync_api import Playwright, sync_playwright, expect
# footer

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://oz.by/")
    page.get_by_role("link", name="Служба поддержки").nth(1).click()
    page.goto("https://oz.by/")
    page.get_by_role("link", name="Доставка").click()
    page.goto("https://oz.by/")
    page.get_by_role("link", name="Оплата").click()
    page.goto("https://oz.by/")
    page.get_by_role("link", name="Обработка персональных данных").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

from playwright.sync_api import Playwright, sync_playwright, expect
# footer

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://oz.by/")
    page.get_by_role("link", name="Новости OZ").click()
    page.goto("https://oz.by/")
    page.get_by_role("link", name="Магазины OZ").click()
    page.goto("https://oz.by/")
    page.get_by_role("link", name="Вакансии").click()
    page.goto("https://oz.by/")
    page.get_by_role("link", name="Бонусная программа").click()
    page.goto("https://oz.by/")
    page.get_by_role("link", name="Партнерская программа").click()

    # ---------------------
    context.close()
    browser.close()



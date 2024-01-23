# menu
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://oz.by/")
    page.get_by_role("link", name="Акции и скидки").click()
    page.goto("https://oz.by/")
    page.get_by_role("link", name="Топ товаров до −60%").click()
    page.goto("https://oz.by/")
    page.get_by_role("link", name="Книги", exact=True).first.click()
    page.goto("https://oz.by/")
    page.get_by_role("link", name="Развлечения, творчество").first.click()
    page.goto("https://oz.by/")
    page.get_by_role("link", name="Сувениры, подарки").click()
    page.goto("https://oz.by/")
    page.get_by_role("link", name="Канцтовары, учёба").click()
    page.goto("https://oz.by/")
    page.get_by_role("link", name="Косметика, парфюмерия").click()
    page.get_by_role("link", name="Продукты, деликатесы").click()
    page.goto("https://oz.by/")
    page.get_by_role("link", name="Дом, сад, зоотовары").click()
    page.goto("https://oz.by/")
    page.get_by_role("link", name="Детям и мамам").click()
    page.goto("https://oz.by/")
    page.get_by_role("link", name="Техника, электроника").click()
    page.goto("https://oz.by/")
    page.get_by_role("link", name="Туризм, отдых, спорт").click()
    page.goto("https://oz.by/")
    page.locator("#storesTab").get_by_role("link", name="Магазины OZ").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

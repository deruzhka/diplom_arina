from playwright.sync_api import Playwright, sync_playwright, expect
# служба поддержки

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://oz.by/")
    page.locator("#top-page").get_by_role("link", name="Служба поддержки").click()
    page.get_by_role("navigation").get_by_role("link", name="Оформление заказа").click()
    page.get_by_role("link", name="Доставка заказа").click()
    page.get_by_role("link", name="Оплата заказа").click()
    page.locator("#top-page").get_by_role("link", name="Обработка персональных данных").click()
    page.get_by_role("link", name="Замена и возврат товара").click()
    page.locator("#top-page").get_by_role("link", name="Бонусная программа").click()
    page.get_by_role("link", name="Вопросы по сайту и приложению").click()
    page.get_by_role("link", name="Акции, скидки и рекламные игры").click()
    page.get_by_role("link", name="Вопросы по ассортименту").click()
    page.get_by_role("link", name="Документы и соглашения").click()
    page.get_by_role("link", name="Работа с юридическими лицами").click()
    page.get_by_role("link", name="О компании").click()

    # ---------------------
    context.close()
    browser.close()



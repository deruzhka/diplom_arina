from playwright.sync_api import Playwright, sync_playwright, expect
# авторизация

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://oz.by/")
    page.get_by_role("link", name="Войти").click()
    page.get_by_role("button", name="Получить SMS c кодом").click()
    page.get_by_placeholder("Введите код").fill("9097")
    page.get_by_placeholder("Введите код").press("Enter")
    page.get_by_role("button", name="Подтверждаю").click()

    # ---------------------
    context.close()
    browser.close()



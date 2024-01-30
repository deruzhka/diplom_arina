from playwright.sync_api import Playwright, sync_playwright, expect
# footer
import allure
import pytest_check as check
def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://oz.by/")
    with allure.step('Проверка нажатия кнопки "Служба поддержки"'):
        if check.is_true(page.get_by_role("Служба поддержки").is_visible()):
            page.get_by_role("Служба поддержки").click()
    page.goto("https://oz.by/")
    with allure.step('Проверка нажатия кнопки "Доставка"'):
        if check.is_true(page.get_by_role("Доставка").is_visible()):
            page.get_by_role("Доставка").click()
    page.goto("https://oz.by/")
    with allure.step('Проверка нажатия кнопки "Оплата"'):
        if check.is_true(page.get_by_role("Оплата").is_visible()):
            page.get_by_role("Оплата").click()
    page.goto("https://oz.by/")
    with allure.step('Проверка нажатия кнопки "Обработка персональных данны"'):
        if check.is_true(page.get_by_role("Обработка персональных данны").is_visible()):
            page.get_by_role("Обработка персональных данны").click()

    # ---------------------
    context.close()
    browser.close()


# menu
from playwright.sync_api import Playwright, sync_playwright, expect
import allure
import pytest_check as check

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://oz.by/")
    with allure.step('Проверка нажатия кнопки "Акции и скидки"'):
        if check.is_true(page.get_by_role("Акции и скидки").is_visible()):
            page.get_by_role("Акции и скидки").click()


    page.goto("https://oz.by/")
    with allure.step('Проверка нажатия кнопки "Топ товаров до −60%"'):
        if check.is_true(page.get_by_role("Топ товаров до −60%").is_visible()):
            page.get_by_role("Топ товаров до −60%").click()

    page.goto("https://oz.by/")
    with allure.step('Проверка нажатия кнопки "Книги"'):
        if check.is_true(page.get_by_role("Книги").is_visible()):
            page.get_by_role("Книги").click()

    page.goto("https://oz.by/")
    with allure.step('Проверка нажатия кнопки "Развлечения, творчествои"'):
        if check.is_true(page.get_by_role("Развлечения, творчество").is_visible()):
            page.get_by_role("Развлечения, творчество").click()


    # ---------------------
    context.close()
    browser.close()

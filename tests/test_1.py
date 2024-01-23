from playwright.sync_api import Playwright, sync_playwright, expect
import allure
import pytest_check as check


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://oz.by/")

    with allure.step('Проверка нажатия кнопки "Введите название товара"'):
        if check.is_true(page.get_by_placeholder("Введите название товара").is_visible()):
            page.get_by_placeholder("Введите название товара").click()

    with allure.step('Проверка поиска'):
        if check.is_true(page.get_by_placeholder("Введите название товара").is_visible()):
            page.get_by_placeholder("Введите название товара").fill("пушкин")
            page.get_by_placeholder("Введите название товара").press("Enter")

    with allure.step('Проверка отображения результата поиска и нажатия на первый элемент поиска'):

        page.locator("#goods-table div").filter(has_text="Скоро закончится -10% 0,26 25").get_by_role("link").click()
        page.get_by_role("button", name=" Положить в корзину").click()

    # ---------------------
    context.close()
    browser.close()


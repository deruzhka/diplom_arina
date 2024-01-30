from playwright.sync_api import Playwright, sync_playwright, expect
# footer
import allure
import pytest_check as check

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://oz.by/")

    with allure.step('Проверка нажатия кнопки "Новости OZ"'):
        if check.is_true(page.get_by_role("Новости OZ").is_visible()):
            page.get_by_role("Новости OZ").click()
    page.goto("https://oz.by/")
    with allure.step('Проверка нажатия кнопки "Магазины OZ"'):
        if check.is_true(page.get_by_role("Магазины OZ").is_visible()):
            page.get_by_role("Магазины OZ").click()
    page.goto("https://oz.by/")
    with allure.step('Проверка нажатия кнопки "Вакансии"'):
        if check.is_true(page.get_by_role("Вакансии").is_visible()):
            page.get_by_role("Вакансии").click()
    page.goto("https://oz.by/")
    with allure.step('Проверка нажатия кнопки "Бонусная программа"'):
        if check.is_true(page.get_by_role("Бонусная программа").is_visible()):
            page.get_by_role("Бонусная программа").click()
    page.goto("https://oz.by/")
    with allure.step('Проверка нажатия кнопки "Партнерская программа"'):
        if check.is_true(page.get_by_role("Партнерская программа").is_visible()):
            page.get_by_role("Партнерская программа").click()

    # ---------------------
    context.close()
    browser.close()



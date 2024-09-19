import time
from playwright.sync_api import sync_playwright


def test_e2e():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://rozetka.com.ua/ua/")
        page.get_by_role("button", name="Каталог").click()
        page.get_by_role("link", name="Ноутбуки", exact=True).click()
        page.locator("app-goods-tile-default").filter(has_text="391395969").get_by_label("Купити").click()
        page.locator("rz-header-cart > button").click()
        page.get_by_test_id("continue-shopping-link").click()
        page.get_by_role("button", name="Каталог").click()
        page.get_by_role("link", name="Комплектуючi").click()
        page.goto("https://hard.rozetka.com.ua/ua/processors/c80083/")
        page.locator("app-goods-tile-default").filter(has_text="331700554").get_by_label("Купити").click()
        page.get_by_role("button", name="2", exact=True).click()
        page.get_by_role("link", name="Оформити замовлення").click()
        page.get_by_role("button", name="Редагувати товари").click()
        page.locator("#cartProductActions0").click()
        page.get_by_role("button", name="Видалити", exact=True).click()
        page.locator("#cartProductActions0").click()
        page.get_by_role("button", name="Видалити", exact=True).click()
        page.get_by_placeholder("Я шукаю").fill("Asus")
        page.get_by_role("button", name="Знайти").click()
        page.get_by_role("button", name="Скасувати").click()
        page.get_by_role("link", name="Rozetka Logo").click()

        browser.close()

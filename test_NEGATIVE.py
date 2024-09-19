import time
from playwright.sync_api import sync_playwright


def test_negative():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # page.pause()
        page.goto("https://rozetka.com.ua/ua/")
        page.get_by_role("link", name="Побутова техніка").click()
        page.get_by_role("link", name="Кондиціонери Кондиціонери").click()
        page.locator("app-goods-tile-default").filter(has_text="436056035").locator("[aria-label='Перемістити в список бажань']").click()
        page.get_by_text("Вхід Телефон Продовжити або").click()
        page.get_by_test_id("modal-close-btn").get_by_role("button").click()
        page.get_by_role("link", name="Rozetka Logo").click()

        browser.close()

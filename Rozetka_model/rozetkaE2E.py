from playwright.sync_api import Playwright


class Rozetka:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def open_page(self):
        self.page.goto("https://rozetka.com.ua/ua/")
        return self

    def open_catalog(self):
        self.page.get_by_role("button", name="Каталог").click()
        self.page.get_by_role("link", name="Ноутбуки", exact=True).click()
        return self

    def add_laptop(self):
        self.page.locator("app-goods-tile-default").filter(has_text="391395969").get_by_label("Купити").click()
        return self

    def check_cart(self):
        self.page.locator("rz-header-cart > button").click()
        self.page.get_by_test_id("continue-shopping-link").click()
        return self

    def open_completing(self):
        self.page.get_by_role("button", name="Каталог").click()
        self.page.get_by_role("link", name="Комплектуючi").click()
        self.page.goto("https://hard.rozetka.com.ua/ua/processors/c80083/")
        return self

    def add_processor(self):
        self.page.locator("app-goods-tile-default").filter(has_text="331700554").get_by_label("Купити").click()
        return self

    def order(self):
        self.page.get_by_role("button", name="2", exact=True).click()
        self.page.get_by_role("link", name="Оформити замовлення").click()
        return self

    def edit_cart(self):
        self.page.get_by_role("button", name="Редагувати товари").click()
        self.page.locator("#cartProductActions0").click()
        self.page.get_by_role("button", name="Видалити", exact=True).click()
        self.page.locator("#cartProductActions0").click()
        self.page.get_by_role("button", name="Видалити", exact=True).click()
        return self

    def search_product(self):
        self.page.get_by_placeholder("Я шукаю").fill("Asus")
        self.page.get_by_role("button", name="Знайти").click()
        return self

    def cancel_search(self):
        self.page.get_by_role("button", name="Скасувати").click()
        return self

    def go_home(self):
        self.page.get_by_role("link", name="Rozetka Logo").click()
        return self

    def close_browser(self):
        self.page.close()
        self.context.close()
        self.browser.close()
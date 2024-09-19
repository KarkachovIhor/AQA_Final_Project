from playwright.sync_api import Playwright, expect


class Negative:
    def __init__(self, playwright: Playwright):
        self.modal_locator = None
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def open_page(self):
        self.page.goto("https://rozetka.com.ua/ua/")
        return self

    def catalog(self):
        self.page.get_by_role("link", name="Побутова техніка").click()
        self.page.get_by_role("link", name="Кондиціонери Кондиціонери").click()
        return self

    def add_to_favorites(self):
        self.page.locator("app-goods-tile-default").filter(has_text="436056035").locator("[aria-label='Перемістити в список бажань']").click()
        return self

    def window_check(self):
        self.modal_locator = self.page.get_by_text("Вхід Телефон Продовжити або")
        expect(self.modal_locator).to_be_visible()
        return self

    def close_the_window(self):
        self.page.get_by_test_id("modal-close-btn").get_by_role("button").click()
        return self

    def home(self):
        self.page.get_by_role("link", name="Rozetka Logo").click()
        return self

    def close_browser(self):
        self.page.close()
        self.context.close()
        self.browser.close()

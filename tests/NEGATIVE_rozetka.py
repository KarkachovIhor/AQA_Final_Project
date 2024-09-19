from playwright.sync_api import sync_playwright
from Rozetka_model.rozetka_negative import Negative


def test_negative():
    with sync_playwright() as playwright:
        rozetka_negative = Negative(playwright)
        rozetka_negative.open_page()
        rozetka_negative.catalog()
        rozetka_negative.add_to_favorites()
        rozetka_negative.window_check()
        rozetka_negative.close_the_window()
        rozetka_negative.home()
        rozetka_negative.close_browser()
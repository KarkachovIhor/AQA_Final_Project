from playwright.sync_api import sync_playwright
from Rozetka_model.rozetkaE2E import Rozetka


def test_e2e():
    with sync_playwright() as playwright:
        rozetka_e2e = Rozetka(playwright)
        rozetka_e2e.open_page()
        rozetka_e2e.open_catalog()
        rozetka_e2e.add_laptop()
        rozetka_e2e.check_cart()
        rozetka_e2e.open_completing()
        rozetka_e2e.add_processor()
        rozetka_e2e.order()
        rozetka_e2e.edit_cart()
        rozetka_e2e.search_product()
        rozetka_e2e.cancel_search()
        rozetka_e2e.go_home()
        rozetka_e2e.close_browser()

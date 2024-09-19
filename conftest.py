from _pytest.fixtures import fixture
from playwright.sync_api import sync_playwright

from Rozetka_model.rozetkaE2E import Rozetka
from Rozetka_model.rozetka_negative import Negative


@fixture
def get_test():
    with sync_playwright() as playwright:
        yield playwright


@fixture
def rozetka_e2e(get_test):
    rozetka = Rozetka(get_test)
    yield rozetka
    rozetka.close_browser()


@fixture
def rozetka_negative(get_test):
    negative = Negative(get_test)
    yield negative
    negative.close_browser()

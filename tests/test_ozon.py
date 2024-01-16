from pages.main_page import MainPage
from pages.search_page import SearchPage


def test_main_page():
    MainPage.verify_page()


def test_search():
    search_string = "ozon tech"

    MainPage.Header.header_search.click()
    MainPage.search_input.input(search_string)
    MainPage.search_button.click()
    SearchPage.verify_page(search_string)

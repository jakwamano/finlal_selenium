from components.header import ComponentHeader
from locator import Locator


class MainPage:
    Header = ComponentHeader

    search_input = Locator('//div[contains(@class, "tm-search__input")]//input', "Search input")
    search_button = Locator('//div[contains(@class, "tm-search__input")]//span', "Search button")
    news_block = Locator('//section[@id="news_block_1"]', "News block")

    @staticmethod
    def verify_page():
        MainPage.Header.verify_component()
        assert MainPage.news_block.is_on_page()

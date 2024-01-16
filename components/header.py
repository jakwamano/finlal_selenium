from locator import Locator


class ComponentHeader:
    header_logo = Locator('//a[contains(@class, "tm-header__logo")]', "Header logo")
    header_search = Locator('//a[contains(@class, "tm-header-user-menu__search")]', "Header search")

    @staticmethod
    def verify_component():
        assert ComponentHeader.header_logo.is_on_page()
        assert ComponentHeader.header_search.is_on_page()

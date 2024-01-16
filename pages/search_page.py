from components.header import ComponentHeader
from locator import Locator


class SearchPage:
    Header = ComponentHeader

    article = Locator('//div[@class="tm-articles-list"]/article', "Article")
    preview = Locator('//div[contains(@class, "placeholder-wrapper")]', "Article placeholder")

    @staticmethod
    def verify_page(expected_string_in_results: str):
        SearchPage.preview.wait_for_disappear()

        SearchPage.Header.verify_component()

        articles = SearchPage.article.get_all_elements()
        assert articles, "empty articles list"

        errors = []
        for article in articles:
            if expected_string_in_results not in article.text().lower():
                errors.append(f"'{expected_string_in_results}' not found in '{article.text().lower()}'")

        assert not errors, errors

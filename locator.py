from __future__ import annotations

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from driver import Driver


class Locator:
    xpath: str = None
    name: str = None
    webelement: WebElement = None

    def __init__(self, xpath: str, name: str):
        self.xpath = xpath
        self.name = name

    def _webelement_required(self):
        def update_webelement():
            try:
                self.webelement = Driver().find_element_by_xpath(self.xpath)
                return self
            except Exception:
                raise Exception(f'Error: cannot locate {self.name}')

        # magic function to update webelement if there is no webelement or if DOM element changed
        if not self.webelement:
            update_webelement()
            return
        try:
            # if not fails, webelement still has the DOM object link
            self.webelement.location
            return
        except StaleElementReferenceException:
            update_webelement()

    def is_on_page(self) -> bool:
        elements = Driver().find_elements_by_xpath(self.xpath)
        if elements:
            return True
        return False

    def click(self):
        self._webelement_required()
        self.webelement.click()

    def text(self) -> str:
        self._webelement_required()
        return self.webelement.text

    def input(self, value: str):
        self._webelement_required()
        self.webelement.send_keys(value)

    def wait_for_disappear(self):
        WebDriverWait(Driver(), 10).until_not(expected_conditions.presence_of_element_located((By.XPATH, self.xpath)))

    def get_all_elements(self) -> [Locator]:
        response = []
        for element in Driver().find_elements_by_xpath(self.xpath):
            locator = Locator(xpath=self.xpath, name=self.name)
            locator.webelement = element
            response.append(locator)
        return response

from selenium.webdriver import Firefox


class Driver(Firefox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.implicitly_wait(5)  # default time waiting for a locator
import pytest

from finlal_selenium.tests.driver import Driver


@pytest.fixture()
def browser() -> Driver:
    driver = Driver(executable_path="path/to/driver")
    driver.set_window_size(1920, 1080)
    driver.get("https://habr.com/ru/all")

    yield driver

    try:
        driver.quit()
    finally:
        driver.__class__._instances = {}

import os
from typing import Final

import pytest
from pytest_bdd import given
from selenium.webdriver import ChromeOptions, Remote
from selenium.webdriver.remote.webdriver import WebDriver

from custom_types import WebDriverFixture


BASE_URL: Final = 'https://bank.gov.ua/en/'


@pytest.fixture(scope='session')
def driver() -> WebDriverFixture:
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--accept-lang=en-US')
    chrome_options.add_argument("--headless=new")
    chrome_options.page_load_strategy = 'eager'
    host = os.environ.get('WEBDRIVER_HOST', 'localhost')
    driver = Remote(f'http://{host}:4444', options=chrome_options)
    driver.maximize_window()
    yield driver

    driver.quit()


@given('Open website')
def open_website(driver: WebDriver) -> None:
    driver.get(BASE_URL)

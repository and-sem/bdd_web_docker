from typing import Generator, TypeAlias

from selenium.webdriver.remote.webdriver import WebDriver


WebDriverFixture: TypeAlias = Generator[WebDriver, None, None]

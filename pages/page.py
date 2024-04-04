from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Page:
    timeout = 15

    def __init__(self, browser: WebDriver) -> None:
        self.browser = browser

    def get_header(self) -> WebElement:
        return self.find_tag('h1')

    def find_tag(self, html_tag_name: str) -> WebElement:
        return self._wait_for_element(By.TAG_NAME, html_tag_name)

    def find_xpath(self, xpath: str) -> WebElement:
        return self._wait_for_element(By.XPATH, xpath)

    def _wait_for_element(self, strategy: str, selector: str) -> WebElement:
        return WebDriverWait(self.browser, self.timeout).until(
            EC.presence_of_element_located((strategy, selector))
        )

from typing import Final

from selenium.webdriver.remote.webdriver import WebDriver, WebElement

from pages.page import Page


class WelcomePage(Page):
    _MENU_ITEM_XPATH_TEMPLATE: Final = '//*[@id="desktop-menu"]/li[{}]/a'

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def find_menu_item(self, item_number: str | int) -> WebElement:
        return self.find_xpath(self._MENU_ITEM_XPATH_TEMPLATE.format(item_number))

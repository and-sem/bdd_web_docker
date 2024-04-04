from pytest_bdd import scenarios, then, when
from pytest_bdd.parsers import parse
from selenium.webdriver.remote.webdriver import WebDriver

from pages import Page, WelcomePage


scenarios('text.feature')


@when(parse('Click menu item {item_number}'))
def click_menu_item(driver: WebDriver, item_number: str) -> None:
    welcome_page = WelcomePage(driver)
    welcome_page.find_menu_item(item_number).click()


@then(parse('Page with {header_text} opens'))
def check_item_link(driver: WebDriver, header_text: str) -> None:
    page = Page(driver)
    assert header_text == page.get_header().text

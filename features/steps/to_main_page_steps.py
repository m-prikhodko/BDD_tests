from behave import *
from selenium.webdriver.common.by import By


@when(u'open web site listing page')
def open_listing(context):
    context.driver.get('https://markformelle.by/catalog/zhenshchinam/sale-leaders/')


@when(u'click on logo')
def banner_click(context):
    element = context.driver.find_element(By.CSS_SELECTOR, '.logo-desktop')
    element.click()


@then(u'main page is opened')
def main_page_opened(context):
    assert "Mark Formelle" in context.driver.title


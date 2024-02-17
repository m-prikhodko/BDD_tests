from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


@given(u'launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)


@when(u'open web site main page')
def open_main_page(context):
    context.driver.get('https://markformelle.by/')


@then(u'logo is on the main page')
def logo_presence(context):
    status = context.driver.find_element(By.CSS_SELECTOR, '.logo-desktop').is_displayed()
    assert status is True


@then(u'close browser')
def close_browser(context):
    context.driver.close()

import pytest
from selene import browser
from selenium import webdriver
from helpers import attach


@pytest.fixture(scope="function", autouse=True)
def browser_settings():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.timeout = 2
    browser.config.base_url = 'https://demowebshop.tricentis.com'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser.config.driver_options = options

    yield
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()

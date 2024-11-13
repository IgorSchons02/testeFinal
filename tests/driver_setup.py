# driver_setup.py
from selenium import webdriver
import os

def get_driver():
    selenium_url = os.getenv('SELENIUM_REMOTE_URL', 'http://localhost:4444/wd/hub')
    options = webdriver.FirefoxOptions()  # Alterado para FirefoxOptions
    driver = webdriver.Remote(
        command_executor=selenium_url,
        options=options
    )
    return driver

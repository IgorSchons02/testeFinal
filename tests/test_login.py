import time
from driver_setup import get_driver
from selenium.webdriver.common.by import By

def test_login():
    driver = get_driver()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    #login 
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'Username')]").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'Password')]").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[text()=' Login ']").click()



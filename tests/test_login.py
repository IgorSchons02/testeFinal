import time
from driver_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login():
    driver = get_driver()
    driver.get("https://opensource-demo.orangehrmlive.com/")

    #login
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'Username')]").send_keys("Admin")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'Password')]").send_keys("admin123")
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()=' Login ']").click()
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.oxd-main-menu-item[href='/web/index.php/pim/viewPimModule']"))).click()
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.oxd-button.oxd-button--medium.oxd-button--secondary"))).click()

    assert "addEmployee" in driver.current_url
    driver.quit()



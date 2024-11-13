import time
from driver_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_user():
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
    driver.find_element(By.CSS_SELECTOR, "a.oxd-main-menu-item[href='/web/index.php/pim/viewPimModule']").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "//button[text()=' Add ']").click()

    time.sleep(2)
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'First Name')]").send_keys("#$@%#")
    
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'Middle Name')]").send_keys("teste")

    time.sleep(2)
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'Last Name')]").send_keys("teste")

    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()=' Save ']").click()
    time.sleep(5)
    assert "empNumber" in driver.current_url
    driver.quit()

def test_post():
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
    driver.find_element(By.CSS_SELECTOR, "a.oxd-main-menu-item[href='/web/index.php/buzz/viewBuzz']").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'What's on your mind?')]").send_keys("teste de post")
    driver.find_element(By.XPATH, "//button[text()=' Post ']").click()

    time.sleep(5)
    assert "viewBuzz" in driver.current_url
    driver.quit()
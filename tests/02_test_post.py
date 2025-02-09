import time
from driver_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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
    driver.find_element(By.CSS_SELECTOR, ".oxd-buzz-post-input").send_keys("teste de post")
    driver.find_element(By.XPATH, "//button[text()=' Post ']").click()

    time.sleep(5)
    assert "viewBuzz" in driver.current_url
    driver.quit()



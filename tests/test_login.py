from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver_setup import get_driver

def test_login():
    driver = get_driver()
    driver.get("https://opensource-demo.orangehrmlive.com/")

    # login
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder,'Username')]"))).send_keys("Admin")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder,'Password')]"))).send_keys("admin123")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Login ']"))).click()

    # Clica no menu "PIM"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.oxd-main-menu-item[href='/web/index.php/pim/viewPimModule']"))).click()

    # Espera pelo botão "Add" e clica nele
    button_add = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.oxd-button.oxd-button--medium.oxd-button--secondary")))
    driver.execute_script("arguments[0].click();", button_add)

    # Verificação de URL
    assert "addEmployee" in driver.current_url
    driver.quit()

# test_login.py
from driver_setup import get_driver  # Importando a função get_driver
from selenium.webdriver.common.by import By

def test_login():
    driver = get_driver()
    driver.get("https://opensource-demo.orangehrmlive.com/")

    # Simular ações no OrangeHRM
    driver.find_element(By.XPATH, "//a[text()='Username']").send_keys("Admin")
    driver.find_element(By.XPATH, "//a[text()='passowrd']").send_keys("admin123")
    driver.find_element(By.ID, "btnLogin").click()
    
    assert "dashboard" in driver.current_url
    driver.quit()


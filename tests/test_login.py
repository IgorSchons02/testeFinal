import time
from driver_setup import get_driver
from selenium.webdriver.common.by import By

def test_login():
    driver = get_driver()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    # Simular ações no OrangeHRM
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'Username')]").send_keys("Admin")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'Password')]").send_keys("admin123")
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()=' Login ']").click()

try:
    driver = get_driver()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    assert "dashboard" in driver.current_url
    print("TESTE APROVADO")  # Se o assert for true
except AssertionError:
    print("TESTE REPROVADO")  

    driver.quit()

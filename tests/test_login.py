#from selenium import webdriver
import time
from driver_setup import get_driver  # Importando a função get_driver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome() 
# driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login') 
# driver.maximize_window()

driver = get_driver()
driver.get("https://opensource-demo.orangehrmlive.com/")

# Simular ações no OrangeHRM
time.sleep(1)
driver.find_element(By.XPATH, "//input[contains(@placeholder,'Username')]").send_keys("Admin")
time.sleep(1)
driver.find_element(By.XPATH, "//input[contains(@placeholder,'Password')]").send_keys("admin123")
time.sleep(1)
driver.find_element(By.XPATH, "//button[text()=' Login ']").click()

time.sleep(1)

assert "dashboard" in driver.current_url
driver.quit()





import time
from driver_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

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
    driver.find_element(By.CSS_SELECTOR, ".oxd-buzz-post-input").send_keys("teste dee post")
    driver.find_element(By.XPATH, "//button[text()=' Post ']").click()

    time.sleep(5)
    assert "viewBuzz" in driver.current_url
    driver.quit()


def test_curtida():
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
    driver.find_element(By.ID, "heart").click()
    
    time.sleep(5)
    assert "viewBuzz" in driver.current_url
    driver.quit()

def test_repost():
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
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[3]/div[1]/button[2]/i").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()=' Share ']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[3]/div[1]/button[2]/i").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()=' Share ']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[3]/div[1]/button[2]/i").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()=' Share ']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[3]/div[1]/button[2]/i").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()=' Share ']").click()

    driver.find_element(By.ID, 'oxd-toaster_1') #id da confirmação
    driver.quit()
    
def test_driverlicense():
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
    driver.find_element(By.CSS_SELECTOR, "a.oxd-main-menu-item[href='/web/index.php/pim/viewMyDetails']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input").send_keys("#%@$@$$@$")
    driver.find_element(By.XPATH, "//button[text()=' Save ']").click()

    driver.find_element(By.ID, 'oxd-toaster_1') #id da confirmação
    driver.quit()

def test_driverlicense():
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
    driver.find_element(By.CSS_SELECTOR, "a.oxd-main-menu-item[href='/web/index.php/pim/viewMyDetails']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input").send_keys("#%@$@$$@$")
    driver.find_element(By.XPATH, "//button[text()=' Save ']").click()

    driver.find_element(By.ID, 'oxd-toaster_1') #id da confirmação
    driver.quit()

def test_workexperience():
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
    driver.find_element(By.CSS_SELECTOR, "a.oxd-main-menu-item[href='/web/index.php/pim/viewMyDetails']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[9]/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()=' Add ']").click()

    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("teste company")
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("teste QA")
    driver.find_element(By.XPATH, "//button[text()=' Save ']").click()

    driver.find_element(By.ID, 'oxd-toaster_1') #id da confirmação
    driver.quit()

def test_userOk():
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
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'First Name')]").send_keys("teste")
    
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'Middle Name')]").send_keys("teste")

    time.sleep(2)
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'Last Name')]").send_keys("tste")

    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()=' Save ']").click()
    driver.find_element(By.ID, 'oxd-toaster_1') #id da confirmação
    driver.quit()

def test_postarVideo():
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
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/button[2]").click()
    
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'Paste Video URL')]").send_keys("https://www.youtube.com/watch?v=3_upA09AntU")

    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()=' Share ']").click()

    driver.find_element(By.ID, 'oxd-toaster_1') #id da confirmação
    driver.quit()

def test_deletarPost():
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
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/li/button/i").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[2]/li/ul/li[1]/p").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()=' Yes, Delete ']").click()

    driver.find_element(By.ID, 'oxd-toaster_1') #id da confirmação
    driver.quit()



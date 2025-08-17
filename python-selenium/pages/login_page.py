from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver=driver
        self.username=(By.NAME,"username")
        self.password=(By.NAME,"password")
        self.login_button=(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")



    def login(self, user, pwd):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.username)).send_keys(user)
        wait.until(EC.visibility_of_element_located(self.password)).send_keys(pwd)
        wait.until(EC.element_to_be_clickable(self.login_button)).click()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddEmployees:

    def __init__(self,driver):
        self.driver=driver
        self.pim_page = (By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']")
        self.add_page=(By.XPATH,"(//a[@class='oxd-topbar-body-nav-tab-item'])[2]")
        # self.add=(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.first_name=(By.NAME,"firstName")
        self.middle_name=(By.NAME,"middleName")
        self.last_name=(By.NAME,"lastName")
        self.save_button=(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")
        self.loader=(By.CLASS_NAME,"oxd-form-loader")

    def add_emp(self,first_name,middle_name,last_name):
        wait=WebDriverWait(self.driver,10)
        wait.until(EC.element_to_be_clickable(self.pim_page)).click()
        wait.until(EC.element_to_be_clickable(self.add_page)).click()
        # wait.until(EC.visibility_of_element_located(self.add)).click()
        wait.until(EC.presence_of_element_located(self.first_name)).send_keys(first_name)
        wait.until(EC.presence_of_element_located(self.middle_name)).send_keys(middle_name)
        wait.until(EC.presence_of_element_located(self.last_name)).send_keys(last_name)
        wait.until(EC.invisibility_of_element_located(self.loader))
        wait.until(EC.element_to_be_clickable(self.save_button)).click()
        # wait.until(EC.invisibility_of_element_located(By.CLASS_NAME, "oxd-form-loader"))
        wait.until(EC.invisibility_of_element_located(self.loader))



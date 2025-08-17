from os import waitstatus_to_exitcode

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from tests.test_orange import driver


class PimModule:

    def __init__(self,driver):
        self.driver=driver
        self.pim=(By.XPATH,"(//a[@class='oxd-main-menu-item'])[2]")


    def go_to_pim(self):
        wait=WebDriverWait(self.driver,10)
        actions = ActionChains(self.driver)
        mouse_action = wait.until(EC.visibility_of_element_located(self.pim))
        actions.move_to_element(mouse_action).click().perform()
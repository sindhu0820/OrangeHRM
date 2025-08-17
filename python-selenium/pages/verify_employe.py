
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time


class VerifyEmployee:

    def __init__(self, driver):
        self.driver = driver
        self.employee_list_url = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"

        # Locators
        self.search_input = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.search_button = (By.XPATH, "//button[normalize-space()='Search']")
        self.table_rows = (By.XPATH, "//div[contains(@class,'oxd-table-body')]//div[@role='row']")
        self.first_name_cells = (By.XPATH, "//div[contains(@class,'oxd-table-body')]//div[@role='row']//div[@role='cell'][3]")
        self.last_name_cells = (By.XPATH, "//div[contains(@class,'oxd-table-body')]//div[@role='row']//div[@role='cell'][4]")

    def go_to_employee_list(self):
        self.driver.get(self.employee_list_url)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_all_elements_located(self.table_rows))

    def verify_employee(self, *emp_names):
        wait = WebDriverWait(self.driver, 20)
        try:
            self.go_to_employee_list()

            for emp_name in emp_names:
                # Clear search input
                search_input_el = wait.until(EC.element_to_be_clickable(self.search_input))
                search_input_el.send_keys(Keys.CONTROL, "a")
                search_input_el.send_keys(Keys.DELETE)
                time.sleep(0.5)


                search_input_el.send_keys(emp_name)

                wait.until(EC.element_to_be_clickable(self.search_button)).click()

                wait.until(EC.presence_of_all_elements_located(self.table_rows))
                time.sleep(0.5)

                first_names = wait.until(EC.presence_of_all_elements_located(self.first_name_cells))
                last_names = wait.until(EC.presence_of_all_elements_located(self.last_name_cells))

                name_list = [
                    f"{fn.text.strip()} {ln.text.strip()}".lower()
                    for fn, ln in zip(first_names, last_names)
                ]

                # Debug print
                print(f"DEBUG: Table contains → {name_list}")

                # Check if employee is present
                if emp_name.strip().lower() in name_list:
                    print(f"✅ Employee '{emp_name}' found.")
                else:
                    print(f"❌ Employee '{emp_name}' NOT found.")

        except TimeoutException:
            print("❌ Timeout: Could not find employee list or table on page.")



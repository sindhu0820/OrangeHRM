from selenium import webdriver
from pages.login_page import LoginPage
from pages.pim_module import  PimModule
from pages.add_employees import AddEmployees
from pages.verify_employe import VerifyEmployee
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
#driver.implicitly_wait(10)
try:
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login = LoginPage(driver)
    login.login("Admin", "admin123")

    pim =PimModule(driver)
    pim.go_to_pim()

    employees=AddEmployees(driver)
    employees.add_emp("sindhu","n","gowda")
    employees.add_emp("asha", "n", "gowda")
    employees.add_emp("chandini", "n", "gowda")

    verify=VerifyEmployee(driver)
    verify.verify_employee("sindhu n gowda")
    verify.verify_employee("asha n gowda")
    verify.verify_employee("chandini n gowda")




finally:
    sleep(10)
    driver.quit()
from selenium.webdriver.common.by import By

from Features.environment import logger
from testdata.data import Orangehrm
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when(u'I navigate to Leave section')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    logger.info("Assign leave to an employee and verify assignment")
    leave=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Leave']")))
    leave.click()


@when(u'I click on Assign Leave')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    assign_leave=wait.until(EC.presence_of_element_located((By.XPATH,"//a[normalize-space()='Assign Leave']")))
    assign_leave.click()


@when(u'I fill on the required fields')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    employee_name=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Type for hints...']")))
    employee_name.send_keys(Orangehrm.emp_name)
    emp_name_option=wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='Richard akhill Johnson']")))
    emp_name_option.click()
    leave_type_dropdown=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'oxd-select-text--active')]")))
    leave_type_dropdown.click()
    leave_type=wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='CAN - Bereavement']")))
    leave_type.click()
    from_date=wait.until(EC.element_to_be_clickable((By.XPATH,"(//i[contains(@class,'oxd-date-input-icon')])[1]")))
    from_date.click()
    # btn=wait.until(EC.element_to_be_clickable((By.XPATH,"(//button[@class='oxd-icon-button'])[3]")))
    # btn.click()
    date=wait.until(EC.element_to_be_clickable((By.XPATH,"(//div[normalize-space()='3'])[1]")))
    date.click()
    to_date=wait.until(EC.element_to_be_clickable((By.XPATH,"(//i[contains(@class,'oxd-date-input-icon')])[2]")))
    to_date.click()
    # btn = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='oxd-icon-button'])[3]")))
    # btn.click()
    date = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[normalize-space()='3'])[1]")))
    date.click()



@when(u'I click on Assign')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    assign=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Assign']")))
    assign.click()

@then(u'Success message has to be displayed confirming the leave assignment')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    try:
        msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(@class,'toast-title')]")))
        assert "Success" in msg.text
        logger.info("Success message displayed")
    except Exception as e:
        logger.info(f"Success message not displayed due to {e}")


@when(u'I click on My leave')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    my_leave=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='My Leave']")))
    my_leave.click()

@then(u'Assigned leave should appear in the employee’s leave records')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    record=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[text()='Richard akhill Johnson']")))
    record.click()

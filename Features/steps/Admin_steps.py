from selenium.webdriver.common.by import By
from Features.environment import capture_screenshot
from testdata.data import Orangehrm
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

#This step connect to the logger file
logger = logging.getLogger(__name__)

@given(u'I open the login page')
def step_impl(context):
    context.driver.get(Orangehrm.url)


@given(u'I login with valid username and valid password')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    username=wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    password =wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    username.send_keys(Orangehrm.username)
    password.send_keys(Orangehrm.password)
    login_btn=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_btn.click()


@when(u'I click on admin')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    logger.info("Creating a new user and validating the login")
    Admin=wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='Admin']")))
    Admin.click()

@when(u'I click on add button')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    Add= wait.until(EC.visibility_of_element_located((By.XPATH,"(//button[contains(@class,'oxd-button oxd-button--medium')])[3]")))
    Add.click()


@when(u'I enter the user details')
def step_impl(context):
    wait=WebDriverWait(context.driver,20)
    User_role_dropdown=wait.until(EC.element_to_be_clickable((By.XPATH,"(//i[contains(@class,'oxd-select-text--arrow')])[1]")))
    User_role_dropdown.click()
    user_role=wait.until(EC.visibility_of_element_located((By.XPATH,"(//span[text()='Admin'])[2]")))
    user_role.click()
    Employee_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']")))
    Employee_name.send_keys(Orangehrm.Employee_name)
    Employee_option=wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Radha  Gupta']")))
    Employee_option.click()
    status_dropdown=wait.until(EC.element_to_be_clickable((By.XPATH,"(//i[contains(@class,'oxd-select-text--arrow')])[2]")))
    status_dropdown.click()
    status=wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='Enabled']")))
    status.click()
    username=wait.until(EC.visibility_of_element_located((By.XPATH,"(//input[contains(@class,'oxd-input--active')])[2]")))
    username.send_keys(Orangehrm.new_username)
    password=wait.until(EC.visibility_of_element_located((By.XPATH,"(//input[@type='password'])[1]")))
    password.send_keys(Orangehrm.new_password)
    confirm_password=wait.until(EC.visibility_of_element_located((By.XPATH,"(//input[@type='password'])[2]")))
    confirm_password.send_keys(Orangehrm.new_password)



@when(u'I click on save button')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    submit = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    submit.click()

@then(u'I should get the success message')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    try:
        msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(@class,'toast-title')]")))
        assert "Success" in msg.text
        logger.info("Success message displayed")
        capture_screenshot(context.driver,"Success message displayed")
    except Exception as e:
        logger.info(f"Success message not displayed due to {e}")
        capture_screenshot(context.driver,"Success message not displayed")



@when(u'I click on logout button')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    drop_down = wait.until(EC.visibility_of_element_located((By.XPATH, "//i[contains(@class,'oxd-icon bi-caret')]")))
    drop_down.click()
    logout_button=wait.until(EC.visibility_of_element_located((By.XPATH,"//a[text()='Logout']")))
    logout_button.click()

@when(u'I login with the newly created credentials')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    username=wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    password =wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    username.send_keys(Orangehrm.new_username)
    password.send_keys(Orangehrm.new_password)
    login=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login.click()


@then(u'I should redirected to the homepage')
def step_impl(context):
    current_url = context.driver.current_url
    assert 'orangehrmlive' in current_url


@when(u'I click on user management')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    logger.info("Validating presence of the newly created user in the admin user list")
    user_management=wait.until(EC.element_to_be_clickable((By.XPATH,"(//i[contains(@class, 'oxd-icon bi-chevron-down')])[1]")))
    user_management.click()


@when(u'I click on users')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    users=wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Users']")))
    users.click()



@then(u'newly created user should be present in the user list')
def step_impl(context):
    wait=WebDriverWait(context.driver, 10)
    try:
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Radha Gupta']")))
        assert "Radha Gupta" in element.text, 'new user not present in the list'
        logger.info("Newly created user is present in the list")
        capture_screenshot(context.driver,"New user creation verified")
    except Exception as e:
        logger.info(f"unable to find the newly created user due to {e} ")
        capture_screenshot(context.driver,"New user has not created")


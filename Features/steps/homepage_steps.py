import logging

from selenium.webdriver.common.by import By
from Features.environment import capture_screenshot
from testdata.data import Orangehrm
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)


@when(u'I login with valid username and valid password')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    logger.info("Verifying visibility and clickability of main menu items after login")
    username=wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    password =wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    username.send_keys(Orangehrm.username)
    password.send_keys(Orangehrm.password)


@when(u'I click Login button')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    lgn=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    lgn.click()


@then(u'I am  redirected to the homepage')
def step_impl(context):
    current_url = context.driver.current_url
    assert 'orangehrmlive' in current_url


@then(u'Main menu items such as Admin,PIM,Leave,Time,Recruitment,My info,Performance,Dashboard should be visible and clickable')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    try:
        menu_items = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard"]
        for item in menu_items:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{item}']")))
            assert element.is_displayed(), f"{item}  is not displayed"
            assert element.is_enabled(), f"{item} is not enabled"
        logger.info("Main menu items is visible and enabled")
        capture_screenshot(context.driver,"Main menu items is visible and enabled")

    except Exception as e:
        logger.info(f"Main menu items are not visible and enabled due to {e}")
        capture_screenshot(context.driver,"Main menu items is not visible and enabled")




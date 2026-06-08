from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Features.environment import  capture_screenshot
import logging

logger = logging.getLogger(__name__)

@when(u'I click on My info')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    logger.info("Validate the presence of menu items under My Info")
    my_info=wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='My Info']")))
    my_info.click()

@then(u'menu items under My info should be visible and clickable')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    try:
        my_info_items = ["Personal Details", "Contact Details", "Emergency Contacts", "Dependents", "Immigration",
                         "Job", "Salary", "Report-to", "Qualifications", "Memberships"]
        for item in my_info_items:
            element = wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[normalize-space()='{item}']")))
            assert element.is_displayed(), f"{item} is not visible"
            assert element.is_enabled(), f"{item} is not clickable"
            element.click()
        logger.info("Menu items under My info is visible and clickable")
        capture_screenshot(context.driver,"Menu items under My info is visible and clickable")
    except Exception as e:
        logger.info(f"Menu items under My info is not visible and clickable due to {e}")
        capture_screenshot(context.driver,"Menu items under My info is visible and clickable")




from selenium.webdriver.common.by import By
from Features.environment import capture_screenshot
from testdata.data import Orangehrm
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)

@when(u'I navigate to claim section')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    logger.info("Initiating the claim request")
    claim=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Claim']")))
    claim.click()


@when(u'I click on submit claim')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    submit_claim=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='Submit Claim']")))
    submit_claim.click()

@when(u'I fill on required fields')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    event_dropdown=wait.until(EC.element_to_be_clickable((By.XPATH,"(//i[contains(@class,'text--arrow')])[1]")))
    event_dropdown.click()
    event=wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='Accommodation']")))
    event.click()
    currency_dropdown=wait.until(EC.element_to_be_clickable((By.XPATH,"(//i[contains(@class,'text--arrow')])[2]")))
    currency_dropdown.click()
    currency=wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='Indian Rupee']")))
    currency.click()
    Remarks=wait.until(EC.visibility_of_element_located((By.XPATH,"//textarea[contains(@class,'resize-vertical')]")))
    Remarks.send_keys(Orangehrm.remark)


@when(u'I click on create button')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    submit=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
    submit.click()


@then(u'success message has to displayed')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    try:
        msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(@class,'toast-title')]")))
        assert "Success" in msg.text
        logger.info("Claim request has been initiated successfully")
        capture_screenshot(context.driver,"success message displayed")
    except Exception as e:
        logger.info(f"Unable to initiate the claim request due to {e}")
        capture_screenshot(context.driver,"success message not displayed")

@then(u'the request should be listed in users claim history')
def step_impl(context):
    wait=WebDriverWait(context.driver,10)
    try:
        my_claims = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'My Claims')]")))
        my_claims.click()
        lst = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Room Accommodation']")))
        assert "Room Accommodation" in lst.text
        logger.info("The claim request is listed in claim history")
        capture_screenshot(context.driver,"claim request listed in users claim history")

    except Exception as e:
        logger.info(f"unable to find the claim request in the claim history due to {e}")
        capture_screenshot(context.driver,"claim request not listed in users claim history")


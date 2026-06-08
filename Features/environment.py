import logging
import os
from selenium import webdriver
import allure

#creating a function to capture screenshots and attaching it to the allure report
@allure.step("Take screenshot and attach it to the report")
def capture_screenshot(driver,step_name):
    allure.attach(driver.get_screenshot_as_png(),name=step_name,attachment_type=allure.attachment_type.PNG)

logger = logging.getLogger()
# setlevel for what we want
logger.setLevel(logging.INFO)
# format includes the details we want in theo utput
formatter = logging.Formatter(fmt="%(asctime)s : %(levelname)s : %(name)s : %(message)s")
# to display the information in the console
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
# saving the logger in the mentioned file
file_handler = logging.FileHandler("test_logs.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

#setup before execution of every test case
def before_scenario(context,scenario):
    #browser setup to run the tests on chrome and firefox
    browser=os.getenv("BROWSER","chrome").lower()
    if browser=="chrome":
        options = webdriver.ChromeOptions()
        #avoids the pop ups such as change password pop_up
        options.add_argument("--disable-popup-blocking")
        #opens the browser in incognito mode
        options.add_argument("--incognito")
        context.driver = webdriver.Chrome(options=options)
    elif browser=="firefox":
        options = webdriver.FirefoxOptions()
        context.driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"unsupported browser:{browser}")
    context.driver.maximize_window()

#step that executes after evry test case execution
def after_scenario(context,scenario):
    #capturing the screenshots on failed test scenarios
    if str(scenario.status).lower()=="failed":
        allure.attach(context.driver.get_screenshot_as_png(),name=f"Failed:{scenario.name}",attachment_type=allure.attachment_type.PNG)
      #closing the browser
    context.driver.quit()




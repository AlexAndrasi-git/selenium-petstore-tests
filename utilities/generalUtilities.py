import os
import time

from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.loginPage import LoginPageLocators


class GeneralUtilities:

    def __init__(self, driver):
        self.driver = driver
        if os.getenv('GITHUB_ACTIONS') is None:
            load_dotenv()

    def login_to_petstore(self, username, password):
        self.driver.get('https://training.testifi.io/login')
        self.driver.implicitly_wait(2)

        username_input = self.driver.find_element(*LoginPageLocators.usernameInput)
        password_input = self.driver.find_element(*LoginPageLocators.passwordInput)
        login_button = self.driver.find_element(*LoginPageLocators.loginButton)

        username_input.send_keys(username)
        password_input.send_keys(password)

        login_button.click()
        time.sleep(1)

    def wait_for_element_visibility_and_click(self, locator, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        selectedLocator = wait.until(EC.visibility_of_element_located(locator))
        selectedLocator.click()



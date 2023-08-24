import time
import os

import unittest2
from selenium import webdriver
from pages.loginPage import LoginPageLocators
from dotenv import load_dotenv
from selenium.webdriver.common.by import By


class TestLoginToPetstore(unittest2.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    if os.getenv('GITHUB_ACTIONS') is None:
        load_dotenv()

    def login_to_petstore(self, username, password):
        self.driver.get('https://training.testifi.io/login')
        self.driver.implicitly_wait(3)

        username_input = self.driver.find_element(*LoginPageLocators.usernameInput)
        password_input = self.driver.find_element(*LoginPageLocators.passwordInput)
        login_button = self.driver.find_element(*LoginPageLocators.loginButton)

        username_input.send_keys(username)
        password_input.send_keys(password)

        login_button.click()
        time.sleep(1)

    def test_login_with_admin_user(self):
        username = os.environ.get('ADMIN_USERNAME')
        password = os.environ.get('ADMIN_PASSWORD')
        self.login_to_petstore(username, password)
        current_url = self.driver.current_url
        self.assertEqual(current_url, "https://training.testifi.io/home")

    def test_login_with_demo_user(self):
        username = os.environ.get('DEMO_USERNAME')
        password = os.environ.get('DEMO_PASSWORD')
        self.login_to_petstore(username, password)
        current_url = self.driver.current_url
        self.assertEqual(current_url, "https://training.testifi.io/home")

    # Negative tests

    def test_login_with_invalid_credentials(self):
        self.login_to_petstore("invalidUser", "invalidPass")
        
        errorMsgContainer = self.driver.find_element(By.CSS_SELECTOR, ".cdk-live-announcer-element.cdk-visually-hidden")
        error_message_text = errorMsgContainer.text
        print("Error Message:", error_message_text)

        if error_message_text != "Username or password are wrong":
            self.fail("The error message about wrong credentials is missing or changed")

        current_url = self.driver.current_url
        self.assertEqual(current_url, "https://training.testifi.io/login")

    def test_login_with_invalid_username_valid_password(self):
        password = os.environ.get('DEMO_PASSWORD')
        self.login_to_petstore("invalidUser", password)

        errorMsgContainer = self.driver.find_element(By.CSS_SELECTOR, ".cdk-live-announcer-element.cdk-visually-hidden")
        error_message_text = errorMsgContainer.text
        print("Error Message:", error_message_text)

        if error_message_text != "Username or password are wrong":
            self.fail("The error message about wrong credentials is missing or changed")

        current_url = self.driver.current_url
        self.assertEqual(current_url, "https://training.testifi.io/login")

    def test_login_with_valid_username_invalid_password(self):
        username = os.environ.get('DEMO_USERNAME')
        self.login_to_petstore(username, "invalidPass")

        errorMsgContainer = self.driver.find_element(By.CSS_SELECTOR, ".cdk-live-announcer-element.cdk-visually-hidden")
        error_message_text = errorMsgContainer.text
        print("Error Message:", error_message_text)

        if error_message_text != "Username or password are wrong":
            self.fail("The error message about wrong credentials is missing or changed")

        current_url = self.driver.current_url
        self.assertEqual(current_url, "https://training.testifi.io/login")

    def test_login_with_empty_username_empty_password(self):
        self.login_to_petstore("", "")

        errorMsgContainer = self.driver.find_element(By.CSS_SELECTOR, ".cdk-live-announcer-element.cdk-visually-hidden")
        error_message_text = errorMsgContainer.text
        print("Error Message:", error_message_text)

        if error_message_text != "Username or password are wrong":
            self.fail("The error message about wrong credentials is missing or changed")

        current_url = self.driver.current_url
        self.assertEqual(current_url, "https://training.testifi.io/login")

    def test_login_with_valid_username_empty_password(self):
        username = os.environ.get('DEMO_USERNAME')
        self.login_to_petstore(username, "")

        errorMsgContainer = self.driver.find_element(By.CSS_SELECTOR, ".cdk-live-announcer-element.cdk-visually-hidden")
        error_message_text = errorMsgContainer.text
        print("Error Message:", error_message_text)

        if error_message_text != "Username or password are wrong":
            self.fail("The error message about wrong credentials is missing or changed")

        current_url = self.driver.current_url
        self.assertEqual(current_url, "https://training.testifi.io/login")

    def test_login_with_empty_username_valid_password(self):
        password = os.environ.get('DEMO_PASSWORD')
        self.login_to_petstore("", password)

        errorMsgContainer = self.driver.find_element(By.CSS_SELECTOR, ".cdk-live-announcer-element.cdk-visually-hidden")
        error_message_text = errorMsgContainer.text
        print("Error Message:", error_message_text)

        if error_message_text != "Username or password are wrong":
            self.fail("The error message about wrong credentials is missing or changed")

        current_url = self.driver.current_url
        self.assertEqual(current_url, "https://training.testifi.io/login")


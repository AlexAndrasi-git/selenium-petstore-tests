import os
import time

import unittest2
from utilities.generalUtilities import GeneralUtilities
from pages.petsPage import PetsPageLocators
from pages.generalPage import PetsPageHomeLocators
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestVerifyPetFunctions(unittest2.TestCase):

    def set_up(self):
        if os.environ.get('GITHUB_ACTIONS') == 'true':
            options = webdriver.ChromeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('headless')
            options.add_argument("start-maximized");
            options.add_argument('--disable-infobars')
            options.add_argument('--disable-dev-shm-usage')
            self.driver = webdriver.Chrome(options=options)
            self.generalUtilities = GeneralUtilities(self.driver)
            self.driver.implicitly_wait(3)
        else:
            self.driver = webdriver.Chrome()
            self.generalUtilities = GeneralUtilities(self.driver)
            self.driver.implicitly_wait(3)

    def tear_down(self):
        self.generalUtilities.driver.quit()

    def test_search_by_sold_status(self):
        username = os.environ.get('ADMIN_USERNAME')
        password = os.environ.get('ADMIN_PASSWORD')
        self.generalUtilities.login_to_petstore(username, password)

        # Sort the pets by 'sold' status in Table View
        self.generalUtilities.wait_for_element_visibility_and_click(PetsPageHomeLocators.petsHeaderButton)
        self.generalUtilities.wait_for_element_visibility_and_click(PetsPageLocators.petsMainButton)
        self.generalUtilities.wait_for_element_visibility_and_click(PetsPageLocators.petsFindPetButton)
        self.generalUtilities.wait_for_element_visibility_and_click(PetsPageLocators.petsSelectAttributeMatSelect)
        self.generalUtilities.wait_for_element_visibility_and_click(PetsPageLocators.petsStatusAttributeMatOption)
        self.generalUtilities.wait_for_element_visibility_and_click(PetsPageLocators.petsNextButton)
        self.generalUtilities.wait_for_element_visibility_and_click(PetsPageLocators.petsStatusSelectMatOption)
        self.generalUtilities.wait_for_element_visibility_and_click(PetsPageLocators.petsSoldStatusMatOption)
        petsSoldStatusMatOption = self.driver.find_element(*PetsPageLocators.petsSoldStatusMatOption)
        petsSoldStatusMatOption.send_keys(Keys.ESCAPE)
        self.generalUtilities.wait_for_element_visibility_and_click(PetsPageLocators.petsSearchButton)

        # Select 50 items instead of 5 in the Table View
        petsItemsPerPageMatSelect = self.driver.find_element(*PetsPageLocators.petsItemsPerPageMatSelect)
        self.driver.execute_script("arguments[0].scrollIntoView();", petsItemsPerPageMatSelect)
        time.sleep(2)
        petsItemsPerPageMatSelect.click()
        pets50ItemPerPageMatOption = self.driver.find_element(*PetsPageLocators.pets50ItemPerPageMatOption)
        pets50ItemPerPageMatOption.click()

        # Iterate through the list of pets and verify that only 'sold' pets are visible
        statuses = self.driver.find_elements(*PetsPageLocators.petsTableViewStatusTd)
        expectedStatus = "sold"

        for status in statuses:
            actualStatus = status.text
            assert actualStatus == expectedStatus, f"Text assertion failed. Expected: '{expectedStatus}', Actual: '{actualStatus}'"

    def test_card_view_visibility(self):
        username = os.environ.get('ADMIN_USERNAME')
        password = os.environ.get('ADMIN_PASSWORD')
        self.generalUtilities.login_to_petstore(username, password)

        # Verify that the 'Card View' visibility in the frontend
        self.generalUtilities.wait_for_element_visibility_and_click(PetsPageHomeLocators.petsHeaderButton)
        self.generalUtilities.wait_for_element_visibility_and_click(PetsPageLocators.petsMainButton)
        self.generalUtilities.wait_for_element_visibility_and_click(PetsPageLocators.petsAddANewViewButton)
        self.generalUtilities.wait_for_element_visibility_and_click(PetsPageLocators.petsCardViewButton)

        petsItemsPerPageMatSelect = self.driver.find_element(*PetsPageLocators.petsItemsPerPageMatSelect)
        petsItemsPerPageMatSelect.click()
        pets50ItemPerPageMatOption = self.driver.find_element(*PetsPageLocators.pets50ItemPerPageMatOption)
        pets50ItemPerPageMatOption.click()
        time.sleep(2)

        # Iterate through the list of pets and get their names
        pet_names_in_table_view = self.driver.find_elements(*PetsPageLocators.petsTableViewNameTd)
        table_view_counter = 0

        list_of_table_view_pet_names = list()
        for name in pet_names_in_table_view:
            name = name.text
            list_of_table_view_pet_names.append(name)
            table_view_counter = table_view_counter + 1

        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)", PetsPageLocators.petsAppCardView)
        pet_names_in_card_view = self.driver.find_elements(*PetsPageLocators.petsNameMatCardTitle)
        card_view_counter = 0

        for name in pet_names_in_card_view:
            name = name.text
            assert name == list_of_table_view_pet_names[card_view_counter]
            card_view_counter = card_view_counter + 1






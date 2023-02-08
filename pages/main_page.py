import keyboard
from .locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_registration_page(self):
        register_link = self.browser.find_element(*MainPageLocators.REGISTER_LINK)
        register_link.click()

    def filter_by_pet_type(self):
        open_pet_type_dropdown = self.browser.find_element(*MainPageLocators.PET_TYPE_DROPDOWN)
        open_pet_type_dropdown.click()
        pet_type_dog = self.browser.find_element(*MainPageLocators.PET_TYPE_DOG)
        pet_type_dog.click()

    def filter_by_pet_name_positive(self):
        input_pet_name = self.browser.find_element(*MainPageLocators.PET_NAME_INPUT)
        input_pet_name.click()
        input_pet_name.send_keys('Hari')
        keyboard.send('enter')

    def filter_by_pet_name_negative(self):
        input_pet_name = self.browser.find_element(*MainPageLocators.PET_NAME_INPUT)
        input_pet_name.click()
        input_pet_name.send_keys('Hariii')
        keyboard.send('enter')

    def open_pet_details(self):
        details_button = self.browser.find_element(*MainPageLocators.DETAILS_BUTTON)
        details_button.click()

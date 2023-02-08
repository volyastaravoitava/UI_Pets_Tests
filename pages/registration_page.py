from .base_page import BasePage
from .locators import RegistrationPageLocators
from .testing_data import EmailOptions, PasswordOptions


class RegistrationPage(BasePage):

    def input_new_email(self):
        register_email = self.browser.find_element(*RegistrationPageLocators.REGISTER_EMAIL)
        register_email.send_keys(*EmailOptions.NEW_EMAIL)

    def input_invalid_email(self):
        register_email = self.browser.find_element(*RegistrationPageLocators.REGISTER_EMAIL)
        register_email.send_keys(*EmailOptions.INVALID_EMAIL)

    def input_existing_email(self):
        register_email = self.browser.find_element(*RegistrationPageLocators.REGISTER_EMAIL)
        register_email.send_keys(*EmailOptions.VALID_EMAIL)

    def input_valid_password(self):
        register_pass = self.browser.find_element(*RegistrationPageLocators.REGISTER_PASS)
        register_pass.send_keys(*PasswordOptions.VALID_PASSWORD)

    def click_on_blank_space(self):
        blank_space = self.browser.find_element(*RegistrationPageLocators.BLANK_SPACE)
        blank_space.click()

    def confirm_valid_password(self):
        register_pass = self.browser.find_element(*RegistrationPageLocators.REGISTER_CONFIRM_PASS)
        register_pass.send_keys(*PasswordOptions.VALID_PASSWORD)

    def input_invalid_password(self):
        register_pass = self.browser.find_element(*RegistrationPageLocators.REGISTER_CONFIRM_PASS)
        register_pass.send_keys(*PasswordOptions.INVALID_PASSWORD)

    def submit_register_btn(self):
        register_btn = self.browser.find_element(*RegistrationPageLocators.REGISTER_BTN)
        register_btn.submit()

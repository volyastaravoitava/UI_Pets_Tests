from .base_page import BasePage
from .locators import LoginPageLocators
from .testing_data import EmailOptions, PasswordOptions


class LoginPage(BasePage):

    def input_valid_email(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(*EmailOptions.VALID_EMAIL)

    def input_invalid_email(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(*EmailOptions.INVALID_EMAIL)

    def input_new_email(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(*EmailOptions.NEW_EMAIL)

    def input_valid_password(self):
        login_pass = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_pass.send_keys(*PasswordOptions.VALID_PASSWORD)

    def input_invalid_password(self):
        login_pass = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_pass.send_keys(*PasswordOptions.INVALID_PASSWORD)

    def submit_btn(self):
        submit_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        submit_btn.submit()

    def show_password(self):
        show_pass_btn = self.browser.find_element(*LoginPageLocators.SHOW_PASS_BTN)
        show_pass_btn.click()

    def hide_password(self):
        hide_pass_btn = self.browser.find_element(*LoginPageLocators.HIDE_PASS_BTN)
        hide_pass_btn.click()

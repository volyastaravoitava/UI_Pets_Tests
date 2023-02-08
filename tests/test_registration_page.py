import pytest
import time
from pages.registration_page import RegistrationPage


@pytest.mark.smoke
@pytest.mark.regression
def test_register_new_user(browser):  # Register new user with valid credentials
    link = 'http://34.141.58.52:8080/#/register'
    page = RegistrationPage(browser, link)
    page.open()
    page.input_new_email()
    time.sleep(3)
    page.input_valid_password()
    time.sleep(3)
    page.click_on_blank_space()
    time.sleep(3)
    page.confirm_valid_password()
    time.sleep(3)
    page.submit_register_btn()
    time.sleep(2)
    browser.save_screenshot('result_register_new_user.png')


@pytest.mark.critical_path
@pytest.mark.regression
def test_register_existing_user(browser):  # Trying to register existing user
    link = 'http://34.141.58.52:8080/#/register'
    page = RegistrationPage(browser, link)
    page.open()
    page.input_existing_email()
    time.sleep(3)
    page.input_valid_password()
    time.sleep(3)
    page.click_on_blank_space()
    time.sleep(3)
    page.confirm_valid_password()
    time.sleep(3)
    page.submit_register_btn()
    time.sleep(2)
    browser.save_screenshot('result_register_existing_user.png')


@pytest.mark.critical_path
@pytest.mark.regression
def test_register_with_invalid_email(browser):  # Trying to register with invalid email
    link = 'http://34.141.58.52:8080/#/register'
    page = RegistrationPage(browser, link)
    page.open()
    page.input_invalid_email()
    time.sleep(3)
    page.input_valid_password()
    time.sleep(3)
    page.click_on_blank_space()
    time.sleep(3)
    page.confirm_valid_password()
    time.sleep(3)
    page.submit_register_btn()
    time.sleep(2)
    browser.save_screenshot('result_register_with_invalid_email.png')


@pytest.mark.smoke
@pytest.mark.regression
def test_register_with_non_coinciding_passwords(browser):  # Pws in "Password" and "Confirm password" don't coincide
    link = 'http://34.141.58.52:8080/#/register'
    page = RegistrationPage(browser, link)
    page.open()
    page.input_new_email()
    time.sleep(3)
    page.input_valid_password()
    time.sleep(3)
    page.click_on_blank_space()
    time.sleep(3)
    page.input_invalid_password()
    time.sleep(3)
    page.submit_register_btn()
    time.sleep(2)
    browser.save_screenshot('result_register_with_non_coinciding_pw.png')


@pytest.mark.critical_path
@pytest.mark.regression
def test_register_with_blank_fields(browser):  # Trying to register with blank fields
    link = 'http://34.141.58.52:8080/#/register'
    page = RegistrationPage(browser, link)
    page.open()
    page.submit_register_btn()
    time.sleep(2)
    browser.save_screenshot('result_register_with_blank_fields.png')

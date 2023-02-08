from pages.login_page import LoginPage
import time
import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_login_with_valid_email_valid_pw(browser):  # Open profile page with valid email & valid password
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.input_valid_email()
    page.input_valid_password()
    page.submit_btn()
    time.sleep(2)
    browser.save_screenshot('result_login_with_valid_email_valid_pw.png')


@pytest.mark.critical_path
@pytest.mark.regression
def test_login_with_new_email(browser):  # Trying to log in with a new email
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.input_new_email()
    page.input_valid_password()
    page.submit_btn()
    time.sleep(2)
    browser.save_screenshot('result_login_with_new_email.png')


@pytest.mark.critical_path
@pytest.mark.regression
def test_login_with_invalid_email_valid_pw(browser):  # Trying to log in with invalid email & valid password
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.input_invalid_email()
    page.input_valid_password()
    page.submit_btn()
    time.sleep(2)
    browser.save_screenshot('result_login_with_invalid_email_valid_pw.png')


@pytest.mark.smoke
@pytest.mark.regression
def test_login_with_valid_email_invalid_pw(browser):  # Trying to log in with valid email & invalid password
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.input_valid_email()
    page.input_invalid_password()
    page.submit_btn()
    time.sleep(2)
    browser.save_screenshot('result_login_with_valid_email_invalid_pw.png')


@pytest.mark.critical_path
@pytest.mark.regression
def test_login_with_blank_fields(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.submit_btn()
    time.sleep(2)
    browser.save_screenshot('result_login_with_blank_fields.png')


@pytest.mark.extended
@pytest.mark.regression
def test_login_show_password(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.input_valid_email()
    page.input_valid_password()
    page.show_password()
    time.sleep(3)
    browser.save_screenshot('login_show_pw.png')


@pytest.mark.extended
@pytest.mark.regression
def test_login_hide_password(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.input_valid_email()
    page.input_valid_password()
    page.show_password()
    time.sleep(3)
    page.hide_password()
    time.sleep(3)
    browser.save_screenshot('login_hide_pw.png')

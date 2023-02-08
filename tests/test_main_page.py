import pytest
import time
from pages.main_page import MainPage


@pytest.mark.smoke
@pytest.mark.regression
def test_go_to_login_page(browser):   # 'Login' button in the header redirects to Login page
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(2)
    browser.save_screenshot('main_go_to_profile_page.png')


@pytest.mark.smoke
@pytest.mark.regression
def test_go_to_registration_page(browser):  # 'Registration' button in the header redirects to Registration page
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_registration_page()
    time.sleep(2)
    browser.save_screenshot('main_go_to_registration_page.png')


@pytest.mark.critical_path
@pytest.mark.regression
def test_filter_by_pet_type(browser):  # Filter by pet type function (dog)
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.filter_by_pet_type()
    time.sleep(2)
    browser.save_screenshot('main_filter_by_pet_type.png')


@pytest.mark.critical_path
@pytest.mark.regression
def test_filter_by_pet_name_existing_pet(browser):  # Filter by pet name function: existing pet name
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.filter_by_pet_name_positive()
    time.sleep(2)
    browser.save_screenshot('main_filter_by_pet_name_existing_pet.png')


def test_filter_by_pet_name_non_existing_pet(browser):  # Filter by pet name function: non-existing pet name
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.filter_by_pet_name_negative()
    time.sleep(2)
    browser.save_screenshot('main_filter_by_pet_name_non_existing_pet.png')


def test_open_pet_details(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.open_pet_details()
    time.sleep(2)
    browser.save_screenshot('main_open_pet_details.png')

from pages.pet_profile_page import PetProfilePage
from .test_login_page import test_login_with_valid_email_valid_pw
import time
import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_add_new_pet_page(browser):  # Adding a new pet into the pet profile
    test_login_with_valid_email_valid_pw(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = PetProfilePage(browser, link)
    page.open()
    page.go_to_add_new_pet_page()
    time.sleep(2)
    link = 'http://34.141.58.52:8080/#/pet-new/pet'
    page = PetProfilePage(browser, link)
    page.open()
    page.input_pet_name()
    page.select_pet_type()
    page.input_pet_age()
    page.select_pet_gender()
    page.add_pet_submit_btn()
    time.sleep(2)
    link = 'http://34.141.58.52:8080/#/pet-new/3875/ava'
    page = PetProfilePage(browser, link)
    page.open()
    page.upload_pet_picture()
    time.sleep(2)
    browser.save_screenshot('add_new_pet.png')


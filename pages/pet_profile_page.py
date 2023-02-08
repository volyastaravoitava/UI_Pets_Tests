from .base_page import BasePage
from .locators import PetProfileLocators
from .testing_data import PetData
import time


class PetProfilePage(BasePage):

    def go_to_add_new_pet_page(self):
        add_btn = self.browser.find_element(*PetProfileLocators.ADD_PET_BTN)
        add_btn.click()
        time.sleep(3)

    def input_pet_name(self):
        input_pet_name = self.browser.find_element(*PetProfileLocators.PET_NAME_INPUT)
        input_pet_name.click()
        input_pet_name.send_keys(*PetData.PET_NEW_NAME)

    def select_pet_type(self):
        select_pet_type = self.browser.find_element(*PetProfileLocators.PET_TYPE_DROPDOWN)
        select_pet_type.click()
        select_pet_type_cat = self.browser.find_element(*PetProfileLocators.PET_TYPE_CAT)
        select_pet_type_cat.click()

    def input_pet_age(self):
        input_pet_age = self.browser.find_element(*PetProfileLocators.PET_AGE_INPUT)
        input_pet_age.click()
        input_pet_age.send_keys(*PetData.PET_AGE)

    def select_pet_gender(self):
        select_pet_gender = self.browser.find_element(*PetProfileLocators.PET_GENDER_DROPDOWN)
        select_pet_gender.click()
        select_pet_gender_female = self.browser.find_element(*PetProfileLocators.PET_GENDER_FEMALE)
        select_pet_gender_female.click()

    def add_pet_submit_btn(self):
        add_pet_submit_btn = self.browser.find_element(*PetProfileLocators.PET_SUBMIT_BTN)
        add_pet_submit_btn.click()

    def upload_pet_picture(self):
        choose_pet_pic_btn = self.browser.find_element(*PetProfileLocators.CHOOSE_PET_PIC_BTN)
        choose_pet_pic_btn.click()
        picture_input = self.browser.find_element(*PetProfileLocators.PICTURE_INPUT)
        picture_input.send_keys('C:/Users/Olga/PycharmProjects/Selenium_UI_Tests/tests/hari_picture.jpg')
        time.sleep(3)
        choose_pet_pic_btn.click()
        time.sleep(3)

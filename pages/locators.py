from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    REGISTER_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(2) > a > span')
    PET_TYPE_DROPDOWN = (By.ID, 'typesSelector')
    PET_TYPE_DOG = (By.CLASS_NAME, 'p-dropdown-item')
    PET_NAME_INPUT = (By.ID, 'petName')
    DETAILS_BUTTON = (By.CLASS_NAME, 'p-button-label')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, 'login')
    LOGIN_PASS = (By.XPATH, '//*[@id="password"]/input')
    LOGIN_BTN = (By.XPATH, '//*[@id="pv_id_2_content"]/div/form/div[3]/button/span[2]')
    SHOW_PASS_BTN = (By.XPATH, '//*[@id="password"]/i[1]' )
    HIDE_PASS_BTN = (By.XPATH, '//*[@id="password"]/i[1]')


class RegistrationPageLocators:
    REGISTER_EMAIL = (By.ID, 'login')
    REGISTER_PASS = (By.CSS_SELECTOR, '#password > input')
    REGISTER_CONFIRM_PASS = (By.CSS_SELECTOR, '#confirm_password > input')
    REGISTER_BTN = (By.CLASS_NAME, 'p-button-label')
    BLANK_SPACE = (By.XPATH, '//*[@id="app"]/main/fieldset/legend')


class PetProfileLocators:
    ADD_PET_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/div[1]/div/div[1]/button')
    PET_NAME_INPUT = (By.ID, 'name')
    PET_TYPE_DROPDOWN = (By.ID, 'typeSelector')
    PET_TYPE_CAT = (By.ID, 'pv_id_2_1')
    PET_AGE_INPUT = (By.XPATH, '//*[@id="age"]/input')
    PET_GENDER_DROPDOWN = (By.ID, 'genderSelector')
    PET_GENDER_FEMALE = (By.ID, 'pv_id_3_1')
    PET_SUBMIT_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[1]')
    CHOOSE_PET_PIC_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div[2]/div/span')
    PICTURE_INPUT = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div[2]/div/span/input')

from selenium.webdriver.common.by import By


class BasePageLocators:
    NAME_INPUT= (By.ID, "userName")
    EMAIL_INPUT = (By.ID, "userEmail")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    SUBMIT = (By.ID, "submit")
    RESULT_NAME = (By.ID, "name")
    RESULT_EMAIL=(By.ID, "email")
    RESULT_CURRENT_ADDRESS = (By.CSS_SELECTOR, "[id='output'] [id='currentAddress']")
    RESULT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "[id='output'] [id='permanentAddress']")
    RESULT_TEXT = (By.ID, "output")

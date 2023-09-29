import time
from .lokators import BasePageLocators
from faker import Faker


class WorkPage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.faker = Faker()

    def open(self):
        self.browser.get(self.url)

    def fill_form(self):
        name = self.faker.name()
        email = self.faker.email()
        current_address = self.faker.city()
        permanent_address = self.faker.city()

        self.browser.find_element(*BasePageLocators.NAME_INPUT).send_keys(name)
        self.browser.find_element(*BasePageLocators.EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*BasePageLocators.CURRENT_ADDRESS).send_keys(current_address)
        self.browser.find_element(*BasePageLocators.PERMANENT_ADDRESS).send_keys(permanent_address)
        return name, email, current_address, permanent_address

    def submit_form(self):
        self.browser.find_element(*BasePageLocators.SUBMIT).click()

    def get_result_text(self):
        r_name = self.browser.find_element(*BasePageLocators.RESULT_NAME).text
        r_email = self.browser.find_element(*BasePageLocators.RESULT_EMAIL).text
        r_c_address = self.browser.find_element(*BasePageLocators.RESULT_CURRENT_ADDRESS).text
        r_p_address = self.browser.find_element(*BasePageLocators.RESULT_PERMANENT_ADDRESS).text
        r_text = self.browser.find_element(*BasePageLocators.RESULT_TEXT)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", r_text)
        result_text = r_text.text
        return r_name, r_email, r_c_address, r_p_address, result_text

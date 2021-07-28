from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from .locators import LoginPageLocators
import pytest

class LoginPage(BasePage):
	def __init__(self, *args, **kwargs):
		super(LoginPage, self).__init__(*args, **kwargs)

	def shold_be_input_fields(self):
		assert self.is_element_present_and_visibl(LoginPageLocators.INPUT_FIELDS[0],LoginPageLocators.INPUT_FIELDS[1])
		
	def go_the_main_page(self):
		email = self.driver.find_elements((*LoginPageLocators.INPUT_FIELDS))[0]
		email.send_keys('admin@admin.ad')
		passw = self.driver.find_elements((*LoginPageLocators.INPUT_FIELDS))[1]
		passw.send_keys('admin')
		passw.send_keys(Keys.RETURN)

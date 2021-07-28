from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
from .locators import MainPageLocators
from .loggers import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class BasePage:
	def __init__(self, driver, url):
		self.driver = driver
		self.url = url

	def open(self):
		self.driver.get(self.url)


	def element_equel_element(self, how, what, element_1, value, timeout=6):
		try:
			es = EC.visibility_of_element_located((how, what))
			element_2 = WebDriverWait(self.driver, timeout).until(es)
			element_2 = element_2.get_attribute(value)
			if str(element_2) == str(element_1):
				return True
			else:
				return False

		except TimeoutException:
			logging.error("Error message! Элемента нет")
			return False

	def save_element(self, how, what, element, timeout=5):
		try:
			es = EC.visibility_of_element_located((how, what))
			element = WebDriverWait(self.driver, timeout).until(es)
			return element
		except TimeoutException:
			logging.error("Error message! нет эелемента")
			return False

	def shold_be_search_text_equel_text(self, how, what, text):
		search = self.driver.find_element(how, what)
		search = search.get_attribute("value")
		if search == text:
			#print(search)
			return True
		logging.error("Error message! Поисковой запрос не соответсует категории")
		return False


	def check_url(self, url):
		if url in self.driver.current_url:
			return True
		logging.error("Error message! url адресс не соответвстует")
		return False

	def is_element_present(self, how, what):
		try:
			self.driver.find_element(how, what)
		except NoSuchElementException:
			logging.error("Error message! нет эелемента")
			return False
		return True

	def is_elements_present_i(self, how, what, i):
		try:
			self.driver.find_elements(how, what)[i]
		except NoSuchElementException:
			logging.error("Error message! нет эелемента")
			return False
		return True


	def is_element_present_and_visibl(self, how, what,  timeout=5):
		try:
			es = EC.visibility_of_element_located((how, what))
			WebDriverWait(self.driver, timeout).until(es)
		except TimeoutException:
			logging.error("Error message! нет элемента")
			return False
		return True

	def is_not_element_present(self, how, what, timeout=4):
		try:
			es = EC.presence_of_element_located((how, what))
			WebDriverWait(self.driver, timeout).until(es)
		except TimeoutException:
			return True
		logging.error("Error message! ( нет эелемента со временем )")
		return False

	def is_disappeared(self, how, what, timeout=4):
		try:
			es = EC.presence_of_element_located((how, what))
			WebDriverWait(self.driver, timeout, 1, TimeoutException).until_not(es)
		except TimeoutException:
			logging.error("Error message! element present(it shouldn't be)")
			return False

		return True

	def in_element(self, string, understr):
		if understr in string:
			return True
		else:
			logging.error("Error message!")
			return False


	def click_on_button(self, how, what):
		try:
			btn = self.driver.find_element(how, what)
			btn.click()
		except NoSuchElementException:
			logging.error("Error message!(не находит кнопку)")
			return False
		return True

	def text_element_equel_text(self,  how, what,number, text):
		try:
			link = self.driver.find_elements(By.CSS_SELECTOR,".widget thead tr th")[number]
			link = link.get_attribute('data-field')
			if str(link) != str(text):
				logging.error(f" { number } ссылка не соответсвует tensor.ru) - {link.text}")
				return False
		except NoSuchElementException:
			logging.error(f"Error message!( { number } ссылка не соответсвует {text})")
			return False
		return True 
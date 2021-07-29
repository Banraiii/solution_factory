from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import pytest
import time 

class MainPage(BasePage):
	def __init__(self, *args, **kwargs):
		super(MainPage, self).__init__(*args, **kwargs)

	def should_be_main_page(self):
		assert self.is_element_present_and_visibl(*MainPageLocators.ADD_PAYMENT_BUTTON),\
		'Нет кнопки'
		assert self.is_elements_present_i(*MainPageLocators.HEAD_TABEL, 0),\
		'должно присутствовать в DOM и видемо на страничке Заголовоки колонок'


	def should_be_add_btn(self):
		self.is_element_present_and_visibl(*MainPageLocators.ADD_PAYMENT_BUTTON)

	def should_be_tabel_in_form(self):
		assert self.is_element_present_and_visibl(*MainPageLocators.ADD_PAYMENT_BUTTON),\
		'Нет кнопки'
		time.sleep(0)
		assert self.text_element_equel_text(*MainPageLocators.HEAD_TABEL,0,'source'),\
		'Нет части таблицы с полями source'

		assert self.text_element_equel_text(*MainPageLocators.HEAD_TABEL,1,'status'),\
		'Нет части таблицы с полями status'

		assert self.text_element_equel_text(*MainPageLocators.HEAD_TABEL,2,'amount_fact'),\
		'Нет части таблицы с полями amount_fact'

		assert self.text_element_equel_text(*MainPageLocators.HEAD_TABEL,3,'date_fact'),\
		'Нет части таблицы с полями date_fact'
	
	def should_be_btn_in_main_page(self):
		assert self.is_element_present_and_visibl(*MainPageLocators.ADD_PAYMENT_BUTTON),\
		'Нет кнопки Над основной таблицей'

	def should_be_go_to_the_next_table(self):
		assert self.is_elements_present_i(*MainPageLocators.BOTOM_BTN,1),\
		'Нижняя кнопка не обнаруженна'
		list_l = self.driver.find_elements(*MainPageLocators.BOTOM_BTN)
		assert len(list_l) == 3,\
		'должно быть 3 кнопки(4 далее)'

	def create_new_payment(self):
		assert self.is_element_present_and_visibl(*MainPageLocators.ADD_PAYMENT_BUTTON),\
		'Нет кнопки'
		btn = self.driver.find_element(*MainPageLocators.ADD_PAYMENT_BUTTON)
		btn.click()

	def should_be_add_payment_form_form(self):
		assert self.is_element_present_and_visibl(*MainPageLocators.FORM_ADD_PAYMENT),\
		'Нет формы'

	def add_description_field(self):
		description = self.driver.find_elements(*MainPageLocators.TEXT_AREA_PAYMENT_FORM)[0]
		save = f'Kostyans { time.time() }'
		description.send_keys(save)
		return save

	def click_on_create_new_payment_in_payment_form(self):
		self.click_on_button(*MainPageLocators.BTN_ADD_IN_FORM_ADD_PAYMENT)

	def should_be_succesful_message(self):
		assert self.is_element_present_and_visibl(*MainPageLocators.MESSAGE_ABOUT_SUCCESFUL_ADD),\
		"Нет всплывающей подсказки о добавлении платежа"

	def save_url_number(self):
		time.sleep(1)
		return self.driver.current_url

	def go_to_the_main_page_of_the_breadcrumbs(self):
		assert self.is_element_present_and_visibl(*MainPageLocators.ADD_PAYMENT_BUTTON),\
		'Нет кнопки Над основной таблицей'
		self.click_on_button(*MainPageLocators.FIRST_ELEMENT_IN_TABLE_FOUND)

	def should_be_search_field(self):
		search = self.driver.find_elements(*MainPageLocators.FIRST_IN_TABLE_FOUND_DESCRIPTION)[-1]
		assert search != False,\
		'Нет поля поиска'


	def search_for_a_description(self, text):
		actionChains = ActionChains(self.driver)
		search_field = self.driver.find_elements(*MainPageLocators.SEACRH_FIELD_IN_TABLES)[-1]
		actionChains.move_to_element(search_field).click(search_field).send_keys(text).perform()
		time.sleep(1)
		search_field.send_keys(Keys.RETURN)
		time.sleep(1)

	def go_to_the_edit_payment(self):
		first_desc = self.is_element_present_and_visibl(*MainPageLocators.FIRST_ELEMENT_IN_TABLE_FOUND)
		actionChains = ActionChains(self.driver)
		search_field = self.driver.find_elements(*MainPageLocators.FIRST_IN_TABLE_FOUND_DESCRIPTION)[0]
		actionChains.move_to_element(search_field).click(search_field).perform()
		time.sleep(2)

	def should_be_previously_created_payment(self, url):
		new_description = self.driver.find_elements(*MainPageLocators.TEXT_AREA_PAYMENT_FORM)[0]	
		#if new_description.text != save_description:
		#	assert False,'description не совпадает с сохранённым'
		if self.driver.current_url != url:
			assert False,'Url не совпадает с сохранённым'
		return True
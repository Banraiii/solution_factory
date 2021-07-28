from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
import time

@pytest.mark.all_test
def test_user_can_log_in(setup_driver):
	link = f"https://finance.dev.fabrique.studio/"
	main_page = MainPage(setup_driver, link)
	main_page.should_be_tabel_in_form()
	main_page.should_be_btn_in_main_page()
	main_page.should_be_go_to_the_next_table()

@pytest.mark.all_test2
def test_user_can_log_in(setup_driver):
	link = f"https://finance.dev.fabrique.studio/"
	main_page = MainPage(setup_driver, link)
	main_page.create_new_payment()
	main_page.should_be_add_payment_form_form()
	main_page.add_description_field()
	main_page.click_on_create_new_payment_in_payment_form()
	save_link = main_page.save_url_number()
	main_page.should_be_succesful_message()
	main_page.go_to_the_main_page_of_the_breadcrumbs()
	main_page = MainPage(setup_driver, link)
	main_page.open()
	main_page.should_be_search_field()
	main_page.search_for_a_description('save_link')


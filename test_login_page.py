from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
import time


@pytest.mark.all_test
def test_user_can_log_in(driver):
	link = f"https://finance.dev.fabrique.studio/"
	login_page = LoginPage(driver, link)
	login_page.open()
	login_page.shold_be_input_fields()
	login_page.go_the_main_page()
	main_page = MainPage(driver, driver.current_url)
	main_page.should_be_main_page()
	time.sleep(2)
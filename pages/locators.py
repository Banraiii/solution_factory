from selenium.webdriver.common.by import By


class MainPageLocators():
	ADD_PAYMENT_BUTTON = (By.CSS_SELECTOR, ".pageLayout__actions button")
	HEAD_TABEL = (By.CSS_SELECTOR,".widget thead tr th")
	IMAGE_LINK_IMAGE = (By.LINK_TEXT, "Картинки")
	BODY_TABEL = (By.CSS_SELECTOR,".table table")
	BOTOM_BTN = (By.CSS_SELECTOR,".pagination__page .button")
	RADIO_BTN_ADD_PAYMENT_FORM = (By.CSS_SELECTOR,".checkbox__content .checkbox__label")
	FORM_ADD_PAYMENT = (By.CSS_SELECTOR,".payment-edit-page")
	TEXT_AREA_PAYMENT_FORM = (By.CSS_SELECTOR,".input__content textarea")
	BTN_ADD_IN_FORM_ADD_PAYMENT = (By.CSS_SELECTOR,".widget__footer .button--state-filled .button__content")
	MESSAGE_ABOUT_SUCCESFUL_ADD = (By.CSS_SELECTOR,".notification.notification--type-success .notification__body")
	BREADCRUMB_HOME_LINK = (By.CSS_SELECTOR,".breadcrumbs .breadcrumb__label")
	SEACRH_FIELD_IN_TABLES = (By.CSS_SELECTOR,".input__input")


class LoginPageLocators():
	INPUT_FIELDS = (By.CSS_SELECTOR, ".form-field__field input")


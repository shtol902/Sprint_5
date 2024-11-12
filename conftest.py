import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators


@pytest.fixture
def login_fixture():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")


    test_email = "shtol902@yandex.ru"
    test_password = "123456"

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.email_input_authorization_xpath))
    driver.find_element(*locators.email_input_authorization_xpath).send_keys(test_email)
    driver.find_element(*locators.password_input_authorization_xpath).send_keys(test_password)
    driver.find_element(*locators.authorization_button_xpath).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.order_button_xpath))

    yield driver
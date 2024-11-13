import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators
import urls
import data

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def login_fixture(driver):

    driver.get(urls.login_url)

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.email_input_authorization_xpath))
    driver.find_element(*locators.email_input_authorization_xpath).send_keys(data.test_user_mail)
    driver.find_element(*locators.password_input_authorization_xpath).send_keys(data.test_user_password)
    driver.find_element(*locators.authorization_button_xpath).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.order_button_xpath))
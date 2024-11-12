import random


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators

def test_registration_success():

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    test_name = f'Alexander'
    test_email = f'alex_shtol_15_{random.randint(100, 999)}@yandex.ru'
    test_password = f'{random.randint(100000, 999999)}'

    driver.find_element(*locators.name_input_registration_xpath).send_keys(test_name)
    driver.find_element(*locators.email_input_registration_xpath).send_keys(test_email)
    driver.find_element(*locators.password_input_registration_xpath).send_keys(test_password)
    driver.find_element(*locators.registration_button_xpath).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.heading_authorization))

    assert "login" in driver.current_url

    driver.quit()

def test_registration_text_error():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    test_name = f'Alexander'
    test_email = f'alex_shtol_15_{random.randint(100, 999)}@yandex.ru'
    test_password_error = f'{random.randint(1, 99999)}'

    driver.find_element(*locators.name_input_registration_xpath).send_keys(test_name)
    driver.find_element(*locators.email_input_registration_xpath).send_keys(test_email)
    driver.find_element(*locators.password_input_registration_xpath).send_keys(test_password_error)
    driver.find_element(*locators.registration_button_xpath).click()

    assert driver.find_element(*locators.message_incorect_password).text == "Некорректный пароль"

    driver.quit()
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators

def test_authorization_home_page():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.login_button_xpath))

    driver.find_element(*locators.login_button_xpath).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.heading_authorization))

    driver.find_element(*locators.email_input_authorization_xpath).send_keys("shtol902@yandex.ru")
    driver.find_element(*locators.password_input_authorization_xpath).send_keys("123456")
    driver.find_element(*locators.authorization_button_xpath).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.order_button_xpath))

    assert driver.find_element(*locators.order_button_xpath).text == "Оформить заказ"

    driver.quit()

def test_authorization_personal_account_button():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.personal_account_button_xpath))

    driver.find_element(*locators.personal_account_button_xpath).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.heading_authorization))

    driver.find_element(*locators.email_input_authorization_xpath).send_keys("shtol902@yandex.ru")
    driver.find_element(*locators.password_input_authorization_xpath).send_keys("123456")
    driver.find_element(*locators.authorization_button_xpath).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.order_button_xpath))

    assert driver.find_element(*locators.order_button_xpath).text == "Оформить заказ"

    driver.quit()


def test_authorization_through_registration_form():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.auth_button_in_reg_form_xpath))

    driver.find_element(*locators.auth_button_in_reg_form_xpath).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.heading_authorization))

    driver.find_element(*locators.email_input_authorization_xpath).send_keys("shtol902@yandex.ru")
    driver.find_element(*locators.password_input_authorization_xpath).send_keys("123456")
    driver.find_element(*locators.authorization_button_xpath).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.order_button_xpath))

    assert driver.find_element(*locators.order_button_xpath).text == "Оформить заказ"

    driver.quit()


def test_authorization_through_forgot_password_form():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.auth_button_in_forgot_form_xpath))

    driver.find_element(*locators.auth_button_in_forgot_form_xpath).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.heading_authorization))

    driver.find_element(*locators.email_input_authorization_xpath).send_keys("shtol902@yandex.ru")
    driver.find_element(*locators.password_input_authorization_xpath).send_keys("123456")
    driver.find_element(*locators.authorization_button_xpath).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.order_button_xpath))

    assert driver.find_element(*locators.order_button_xpath).text == "Оформить заказ"

    driver.quit()
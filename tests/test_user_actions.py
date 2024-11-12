import locators
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_access_click_personal_account(login_fixture):
    driver = login_fixture
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(locators.personal_account_button_xpath))

    driver.find_element(*locators.personal_account_button_xpath).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.personal_account_text))

    assert driver.find_element(*locators.personal_account_text).text == "В этом разделе вы можете изменить свои персональные данные"

    driver.quit()

def test_access_click_constructor_from_personal_account(login_fixture):
    driver = login_fixture
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(locators.personal_account_button_xpath))

    driver.find_element(*locators.personal_account_button_xpath).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.constructor_button_xpath))

    driver.find_element(*locators.constructor_button_xpath).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.order_button_xpath))

    assert driver.find_element(*locators.order_button_xpath).text == "Оформить заказ"

    driver.quit()

def test_access_unauthorization(login_fixture):
    driver = login_fixture
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(locators.personal_account_button_xpath))

    driver.find_element(*locators.personal_account_button_xpath).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.unauthorization_button_xpath))

    driver.find_element(*locators.unauthorization_button_xpath).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.authorization_button_xpath))

    assert driver.find_element(*locators.authorization_button_xpath).text == "Войти"

    driver.quit()

def test_success_scroll_sauce(login_fixture):
    driver = login_fixture
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(locators.sauce_button_xpath))

    driver.find_element(*locators.sauce_button_xpath).click()
    sauce_button_xpath = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.sauce_button_xpath))

    assert "current" in sauce_button_xpath.get_attribute("class")

    driver.quit()


def test_filling_scroll_filling(login_fixture):
    driver = login_fixture
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(locators.filling_button_xpath))

    driver.find_element(*locators.filling_button_xpath).click()
    filling_button_xpath = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.filling_button_xpath))

    assert "current" in filling_button_xpath.get_attribute("class")

    driver.quit()


def test_success_scroll_bread(login_fixture):
    driver = login_fixture
    bread_button_xpath = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locators.bread_button_xpath))

    assert "current" in bread_button_xpath.get_attribute("class")

    driver.quit()
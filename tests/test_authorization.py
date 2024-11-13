from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators
import urls
import data

class TestClassAuthorization:
    def test_authorization_home_page(self, driver):

        driver.get(urls.base_url)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.login_button_xpath))

        driver.find_element(*locators.login_button_xpath).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.heading_authorization))

        driver.find_element(*locators.email_input_authorization_xpath).send_keys(data.test_user_mail)
        driver.find_element(*locators.password_input_authorization_xpath).send_keys(data.test_user_password)
        driver.find_element(*locators.authorization_button_xpath).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.order_button_xpath))

        assert driver.find_element(*locators.order_button_xpath).text == "Оформить заказ"


    def test_authorization_personal_account_button(self, driver):

        driver.get(urls.base_url)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.personal_account_button_xpath))

        driver.find_element(*locators.personal_account_button_xpath).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.heading_authorization))

        driver.find_element(*locators.email_input_authorization_xpath).send_keys(data.test_user_mail)
        driver.find_element(*locators.password_input_authorization_xpath).send_keys(data.test_user_password)
        driver.find_element(*locators.authorization_button_xpath).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.order_button_xpath))

        assert driver.find_element(*locators.order_button_xpath).text == "Оформить заказ"



    def test_authorization_through_registration_form(self, driver):

        driver.get(urls.register_url)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.auth_button_in_reg_form_xpath))

        driver.find_element(*locators.auth_button_in_reg_form_xpath).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.heading_authorization))

        driver.find_element(*locators.email_input_authorization_xpath).send_keys(data.test_user_mail)
        driver.find_element(*locators.password_input_authorization_xpath).send_keys(data.test_user_password)
        driver.find_element(*locators.authorization_button_xpath).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.order_button_xpath))

        assert driver.find_element(*locators.order_button_xpath).text == "Оформить заказ"



    def test_authorization_through_forgot_password_form(self, driver):

        driver.get(urls.forgot_password_url)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.auth_button_in_forgot_form_xpath))

        driver.find_element(*locators.auth_button_in_forgot_form_xpath).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.heading_authorization))

        driver.find_element(*locators.email_input_authorization_xpath).send_keys(data.test_user_mail)
        driver.find_element(*locators.password_input_authorization_xpath).send_keys(data.test_user_password)
        driver.find_element(*locators.authorization_button_xpath).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(locators.order_button_xpath))

        assert driver.find_element(*locators.order_button_xpath).text == "Оформить заказ"


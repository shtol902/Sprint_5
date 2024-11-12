from selenium.webdriver.common.by import By

# Страница регистрации
name_input_registration_xpath = (By.XPATH, "//fieldset[1]//div[1]//div[1]//input[1]") # Поле ввода имени
email_input_registration_xpath = (By.XPATH, "//fieldset[2]//div[1]//div[1]//input[1]") # Поле ввода email
password_input_registration_xpath = (By.XPATH, "//input[@name='Пароль']") # Поле ввода пароля
registration_button_xpath = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]") #Кнопка "Зарегистрироваться"
message_incorect_password = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")
auth_button_in_reg_form_xpath = (By.XPATH, "//a[contains(text(),'Войти')]")


#Страница авторизации
heading_authorization = (By.XPATH, "//h2[contains(text(),'Вход')]") #Заголовок "Вход"
email_input_authorization_xpath = (By.XPATH, "//input[@name='name']") #Поле ввода email
password_input_authorization_xpath = (By.XPATH, "//input[@name='Пароль']") #Поле ввода пароля
authorization_button_xpath = (By.XPATH, "//button[contains(text(),'Войти')]") #Кнопка "Войти"



#Главная страница
login_button_xpath = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]") # Кнопка "Войти в аккаунт"
order_button_xpath = (By.XPATH, "//button[contains(text(),'Оформить заказ')]") # Кнопка "Оформить заказ"
personal_account_button_xpath = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]") # Кнопка "Личный кабинет"
bread_button_xpath = (By.XPATH, "//span[contains(text(),'Булки')]/parent::div") #Кнопка "Булки"
sauce_button_xpath = (By.XPATH, "//span[contains(text(),'Соусы')]/parent::div") #Кнопка "Соусы"
filling_button_xpath = (By.XPATH, "//span[contains(text(),'Начинки')]/parent::div") #Кнопка "Начинки"

#Страница восстановления пароля
auth_button_in_forgot_form_xpath = (By.XPATH, "//a[contains(text(),'Войти')]") #Кнопка "Войти"

#Личный кабинет
personal_account_text = (By.XPATH, "//p[@class='Account_text__fZAIn text text_type_main-default']") #Текст под меню
constructor_button_xpath = (By.XPATH, "//header[@class='AppHeader_header__X9aJA pb-4 pt-4']//li[1]//a[1]") #Кнопка "Конструктор"
unauthorization_button_xpath = (By.XPATH, "//button[contains(text(),'Выход')]") #Кнопка "Выход"

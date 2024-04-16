import pytest
from settings import valid_email, valid_password
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('./chromedriver.exe')
    pytest.driver.implicitly_wait(10)
    #Переход на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')
    yield
    pytest.driver.quit()

@pytest.fixture()
def go_to_my_pets():

    #Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    #Ввод email
    pytest.driver.find_element_by_id('email').send_keys(valid_email)

    #Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
    #Ввод пароля
    pytest.driver.find_element_by_id('pass').send_keys(valid_password)

    #Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))

    #Нажатие на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

    #Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))

    #Нажатие на ссылку "Мои питомцы"
    pytest.driver.find_element_by_link_text("Мои питомцы").click()

    #Неявное ожидание
    myDynamicElement = pytest.driver.find_element_by_id("all_my_pets")
import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import configparser

config_path = os.path.abspath('config.ini')
config = configparser.ConfigParser()
config.read('config.ini')

print(config.sections())


@pytest.fixture()
def driver(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture()
def driver_incognito(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--enable-features=AllowLocationOnDesktop")
    time.sleep(2)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()
    driver.quit()


class TestDataSignin:
    Url = config.get('Signin', 'url')
    valid_email = config.get('Signin', 'valid_Email')
    valid_password = config.get('Signin', 'valid_Password')
    invalid_email = config.get('Signin', 'invalid_Email')
    invalid_password = config.get('Signin', 'invalid_Password')


user1 = TestDataSignin()


class TestDataSignup:
    name = config.get('Signup', 'name')
    brokerage = config.get('Signup', 'brokerage')
    email = config.get('Signup', 'email')
    mobile = config.get('Signup', 'mobile')
    address = config.get('Signup', 'address')
    city = config.get('Signup', 'city')
    postal_code = config.get('Signup', 'postal_code')
    card_name = config.get('Signup', 'card_name')
    card_number = config.get('Signup', 'card_number')
    exp_date = config.get('Signup', 'exp_date')
    cvc = config.get('Signup', 'cvc')


user2 = TestDataSignup()


class TestSetPassword:
    url = config.get('Set_password', 'url')
    password = config.get('Set_password', 'password')
    confirm_password = config.get('Set_password', 'confirm_Password')
    not_match = config.get('Set_password', 'not_Match')


set_pass = TestSetPassword()


class TestLead:
    cus_Url = config.get('Lead', 'cus_url')
    cus_Name = config.get('Lead', 'cus_name')
    cus_Mail = config.get('Lead', 'cus_mail')
    cus_Phone = config.get('Lead', 'cus_phone')
    cus_Address = config.get('Lead', 'cus_address')
    cus_City = config.get('Lead', 'cus_city')
    cus_Postal = config.get('Lead', 'cus_postal')
    cus_Message = config.get('Lead', 'cus_message')


lead = TestLead()

import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    #chrome_options.add_argument("--enable-features=AllowLocationOnDesktop")
    time.sleep(2)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()
    driver.quit()


class TestDataSignin:
    Url = "https://test.usehomeleads.com/"
    valid_email = "sanzidamaisha2068@gmail.com"
    valid_password = "123456"
    invalid_email = "sanzidaafrin1000@gmail.com"
    invalid_password = "11234567"


user1 = TestDataSignin()


class TestDataSignup:
    name = "Robert"
    brokerage = "Robert Clinton"
    email = "sanzidaafrin098385@gmail.com"
    mobile = "6134526784"
    address = "113 Starrs Rd"
    city = "Yarmouth"
    postal_code = "B5A 0A1"
    card_name = "Hillary Clinton"
    card_number = "2452 1786 3217 6312"
    exp_date = "04/24"
    cvc = "3423"


user2 = TestDataSignup()


class TestSetPassword:
    url = "https://test.usehomeleads.com/set-password?uId=6593b49c2397e81dfc941cef"
    password = "1234567"
    confirm_password = "1234567"
    not_match = "123456"


set_pass = TestSetPassword()


class TestLead:
    cus_url = "https://test.usehomeleads.com/customer-register"
    cus_name = "User"
    cus_mail = "user26@gmail.com"
    cus_phone = "6132677778"
    cus_address = "20 5th St,"
    cus_city = "Courtenay"
    cus_postal = "V6P 1N1"
    cus_message = "This is test."


lead = TestLead()

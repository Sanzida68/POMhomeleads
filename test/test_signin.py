import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from test.pages.SignInPage import SigninPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()


def test_signin(driver):
    signin_page = SigninPage(driver)
    signin_page.open_page("https://test.usehomeleads.com/")
    signin_page.signin_button()
    signin_page.enter_email("sanzidamaisha2068@gmail.com")
    signin_page.enter_pass("123456")
    signin_page.enter_signin()
    time.sleep(3)

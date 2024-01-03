import time

from test.pages.HomePage import HomePage
from test.pages.SignInPage import SigninPage


def test_signin(driver):
    HomePage(driver).for_signin_page("https://test.usehomeleads.com/")
    signin_page = SigninPage(driver)
    signin_page.enter_email("sanzidamaisha2068@gmail.com")
    signin_page.enter_pass("123456")
    signin_page.enter_signin()
    time.sleep(3)


def invalid_email_valid_pass(driver):
    HomePage(driver).for_signin_page("https://test.usehomeleads.com/")
    signin_page = SigninPage(driver)
    signin_page.enter_email("sanzidaafrin1000@gmail.com")
    signin_page.enter_pass("123456")
    signin_page.enter_signin()
    time.sleep(3)


def valid_email_invalid_pass(driver):
    HomePage(driver).for_signin_page("https://test.usehomeleads.com/")
    signin_page = SigninPage(driver)
    signin_page.enter_email("sanzidamaisha2068@gmail.com")
    signin_page.enter_pass("1234567")
    signin_page.enter_signin()
    time.sleep(3)


def empty_field(driver):
    HomePage(driver).for_signin_page("https://test.usehomeleads.com/")
    signin_page = SigninPage(driver)
    signin_page.enter_email("")
    signin_page.enter_pass("")
    signin_page.enter_signin()
    time.sleep(3)

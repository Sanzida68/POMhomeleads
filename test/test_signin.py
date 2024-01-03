import time
import pytest

from test.conftest import TestDataSignin
from test.pages.HomePage import HomePage
from test.pages.SignInPage import SigninPage


@pytest.mark.usefixtures("driver")
class TestSignin:

    def test_signin(self, driver):
        HomePage(driver).for_signin_page(TestDataSignin.Url)
        SigninPage(driver).for_login(TestDataSignin.valid_email, TestDataSignin.valid_password)
        time.sleep(3)

    def test_invalid_email_valid_pass(self, driver):
        HomePage(driver).for_signin_page(TestDataSignin.Url)
        SigninPage(driver).for_login(TestDataSignin.invalid_email, TestDataSignin.valid_password)
        time.sleep(3)

    def test_valid_email_invalid_pass(self, driver):
        HomePage(driver).for_signin_page(TestDataSignin.Url)
        SigninPage(driver).for_login(TestDataSignin.valid_email, TestDataSignin.invalid_password)
        time.sleep(3)

    def test_empty_field(self, driver):
        HomePage(driver).for_signin_page(TestDataSignin.Url)
        SigninPage(driver).for_login("", "")
        time.sleep(3)

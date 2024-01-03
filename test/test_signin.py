import time
import pytest
from test.pages.HomePage import HomePage
from test.pages.SignInPage import SigninPage


@pytest.mark.usefixtures("driver")
class Test_signin:

    def test_signin(self):
        HomePage(self).for_signin_page("https://test.usehomeleads.com/")
        SigninPage(self).for_login("sanzidamaisha2068@gmail.com", "123456")
        time.sleep(3)

    def invalid_email_valid_pass(self):
        HomePage(self).for_signin_page("https://test.usehomeleads.com/")
        SigninPage(self).for_login("sanzidaafrin1000@gmail.com", "123456")
        time.sleep(3)

    def valid_email_invalid_pass(self):
        HomePage(self).for_signin_page("https://test.usehomeleads.com/")
        SigninPage(self).for_login("sanzidamaisha2068@gmail.com", "1234567")
        time.sleep(3)

# def empty_field(driver):
# HomePage(driver).for_signin_page("https://test.usehomeleads.com/")
# signin_page = SigninPage(driver)
# signin_page.enter_email("")
# signin_page.enter_pass("")
# signin_page.enter_signin()
# time.sleep(3)

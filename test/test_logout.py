import time

from test.pages.LogOutPage import LogoutPage
from test.pages.SignInPage import SigninPage


def test_logout(driver):
    signin = SigninPage(driver)
    signin.for_login("https://test.usehomeleads.com/", "sanzidamaisha2068@gmail.com", "123456")

    logout = LogoutPage(driver)
    logout.click_profile()
    logout.click_logout()
    time.sleep(3)

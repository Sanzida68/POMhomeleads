import time

from test.pages.HomePage import HomePage
from test.pages.LogOutPage import LogoutPage
from test.pages.SignInPage import SigninPage


def test_logout(driver):
    HomePage(driver).for_signin_page("https://test.usehomeleads.com/")
    signin = SigninPage(driver)
    signin.for_login("sanzidamaisha2068@gmail.com", "123456")
    logout = LogoutPage(driver)
    logout.click_profile()
    time.sleep(1)
    logout.click_logout()
    time.sleep(3)

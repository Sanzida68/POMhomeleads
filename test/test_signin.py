import time
from test.pages.SignInPage import SigninPage


def test_signin(driver):
    signin_page = SigninPage(driver)
    signin_page.open_page("https://test.usehomeleads.com/")
    signin_page.signin_button()
    signin_page.enter_email("sanzidamaisha2068@gmail.com")
    signin_page.enter_pass("123456")
    signin_page.enter_signin()
    time.sleep(3)

import time
from test.pages.AccountActivationPage import AccountActivePage


def test_set_password(driver):
    set_password = AccountActivePage(driver)
    set_password.open_page("https://test.usehomeleads.com/set-password?uId=6593b49c2397e81dfc941cef")
    set_password.set_password("1234567")
    set_password.set_con_password("1234567")
    set_password.set_button()
    time.sleep(3)

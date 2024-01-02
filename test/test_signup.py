import time
from test.pages.SignupPage import SignupPage


def test_signup(driver):
    signup_page = SignupPage(driver)
    signup_page.open("https://test.usehomeleads.com/")
    signup_page.signup_button()
    signup_page.full("Hillary")
    signup_page.brokerage("Hillary Clinton")
    signup_page.email_address("sanzidaafrin098385@gmail.com")
    signup_page.mobile("6134526784")
    signup_page.address("113 Starrs Rd")
    signup_page.province(driver)
    signup_page.city("Yarmouth")
    signup_page.postal_code("B5A 0A1")
    signup_page.agreement()
    signup_page.step1()
    time.sleep(2)
    signup_page.card_holder("Hillary Clinton")
    signup_page.card_number("2452 1786 3217 6312")
    signup_page.expire("04/23")
    signup_page.cvc("3423")
    signup_page.step2()
    time.sleep(2)
    signup_page.step3()

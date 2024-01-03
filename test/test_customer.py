import time

from test.pages.CustomerPage import CustomerPage


def test_customer(driver):
    customer_lead = CustomerPage(driver)
    customer_lead.page("https://test.usehomeleads.com/customer-register")
    customer_lead.enter_button()
    time.sleep(2)
    customer_lead.enter_name("Robert")
    customer_lead.enter_mail("user23@gmail.com")
    customer_lead.enter_phone("1635248764")
    customer_lead.enter_address("1020 W 54th Ave")
    customer_lead.enter_city("Vancouver")
    customer_lead.enter_province(driver)
    customer_lead.enter_postal("V6P 1N1")
    customer_lead.enter_message("This is test.")
    customer_lead.enter_submit()
    customer_lead.enter_popup()

    time.sleep(3)

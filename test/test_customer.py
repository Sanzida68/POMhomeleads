import time

import pytest

from test.conftest import lead
from test.pages.CustomerPage import CustomerPage


@pytest.mark.usefixtures("driver")
class TestCustomer:
    def test_customer(self, driver):
        CustomerPage(driver).for_customer_lead(url=lead.cus_url, cus_n=lead.cus_name, cus_email=lead.cus_mail,
                                               cus_phone=lead.cus_phone, cus_address=lead.cus_address,
                                               cus_city=lead.cus_city, cus_postal=lead.cus_postal,
                                               cus_message=lead.cus_message)
        time.sleep(3)

    def test_with_mandatory_field(self, driver):
        CustomerPage(driver).for_customer_lead(url=lead.cus_url, cus_n=lead.cus_name, cus_email=lead.cus_mail,
                                               cus_phone=lead.cus_phone, cus_address=lead.cus_address,
                                               cus_city=lead.cus_city, cus_postal=lead.cus_postal,
                                               cus_message="")

    def test_without_mandatory_field(self, driver):
        CustomerPage(driver).for_customer_lead(url=lead.cus_url, cus_n="", cus_email="",
                                               cus_phone="", cus_address="",
                                               cus_city="", cus_postal="",
                                               cus_message="")

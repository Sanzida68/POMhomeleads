import time

import pytest

from test.conftest import lead
from test.pages.CustomerPage import CustomerPage


@pytest.mark.usefixtures("driver_incognito")
class TestCustomer:
    def test_customer(self, driver_incognito):
        CustomerPage(driver_incognito).for_customer_lead(url=lead.cus_Url, cus_n=lead.cus_Name, cus_email=lead.cus_Mail,
                                                         cus_phone=lead.cus_Phone, cus_address=lead.cus_Address,
                                                         cus_city=lead.cus_City, cus_postal=lead.cus_Postal,
                                                         cus_message=lead.cus_Message)
        time.sleep(3)

    def test_with_mandatory_field(self, driver_incognito):
        CustomerPage(driver_incognito).for_customer_lead(url=lead.cus_Url, cus_n=lead.cus_Name, cus_email=lead.cus_Mail,
                                                         cus_phone=lead.cus_Phone, cus_address=lead.cus_Address,
                                                         cus_city=lead.cus_City, cus_postal=lead.cus_Postal,
                                                         cus_message="")

    def test_without_mandatory_field(self, driver_incognito):
        CustomerPage(driver_incognito).for_customer_lead(url=lead.cus_Url, cus_n="", cus_email="",
                                                         cus_phone="", cus_address="",
                                                         cus_city="", cus_postal="",
                                                         cus_message="")

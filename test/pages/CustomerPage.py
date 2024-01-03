from selenium.webdriver.common.by import By


class CustomerPage:
    def __init__(self, driver):
        self.driver = driver

        self.customer_button_xpath = (By.XPATH, "//button[@class='sc-gKHVLF hLJjqo ms-auto']")
        self.customer_name = (By.NAME, "name")
        self.customer_email_name = (By.NAME, "email")
        self.customer_phone_name = (By.NAME, "mobileNumber")
        self.customer_address_name = (By.NAME, "address")
        self.customer_city_name = (By.NAME, "city")
        self.customer_province_xpath = (By.XPATH, "//div[@class='w-100 position-relative']")
        self.customer_postal_code_name = (By.NAME, "postalCode")
        self.customer_message = (By.NAME, "message")
        self.customer_submit_xpath = (By.XPATH, "//span[@class='font-weight-semibold ']")
        self.customer_popup_xpath = (By.XPATH, "//button[@class='sc-gKHVLF jdfJhN']")

    def page(self, url):
        self.driver.get(url)

    def enter_button(self):
        self.driver.find_element(*self.customer_button_xpath).click()

    def enter_name(self, cus_n):
        self.driver.find_element(*self.customer_name).send_keys(cus_n)

    def enter_mail(self, cus_email):
        self.driver.find_element(*self.customer_email_name).send_keys(cus_email)

    def enter_phone(self, cus_phone):
        self.driver.find_element(*self.customer_phone_name).send_keys(cus_phone)

    def enter_address(self, cus_address):
        self.driver.find_element(*self.customer_address_name).send_keys(cus_address)

    def enter_city(self, cus_city):
        self.driver.find_element(*self.customer_city_name).send_keys(cus_city)

    def enter_province(self, driver):
        self.driver.find_element(*self.customer_province_xpath).click()

        for x in range(1, 11):
            dd = f"//ul[@class='sc-fEyylQ eNreKR']//li[@class='sc-idyqAC cBRBVe'][{x}]"
            a = driver.find_element(By.XPATH, dd)
            b = a.text
            print(b)

            if b == "British Columbia":
                a.click()
                break

    def enter_postal(self, cus_postal):
        self.driver.find_element(*self.customer_postal_code_name).send_keys(cus_postal)

    def enter_message(self, cus_message):
        self.driver.find_element(*self.customer_message).send_keys(cus_message)

    def enter_submit(self):
        self.driver.find_element(*self.customer_submit_xpath).click()

    def enter_popup(self):
        self.driver.find_element(*self.customer_popup_xpath).click()

from selenium.webdriver.common.by import By


class SignupPage:
    def __init__(self, driver):
        self.driver = driver

        self.signup_button_xpath = (By.XPATH, "//button[@class='sc-gKHVLF iECspq']")
        self.full_name = (By.NAME, "fullName")
        self.brokerage_name = (By.NAME, "brokerage")
        self.email_name = (By.NAME, "email")
        self.mobile_name = (By.NAME, "mobileNumber")
        self.address_name = (By.NAME, "address")
        self.province_field_xpath = (By.XPATH, "//div[@class='w-100 position-relative']")

        for x in range(1, 11):
            self.a = f"//ul[@class='sc-fEyylQ eNreKR']//li[@class='sc-idyqAC cBRBVe'][{x}]"
            element = driver.find_element(By.XPATH, self.a)
            text = element.text

            if text == "Nova Scotia":
                break

        self.city_name = (By.NAME, "city")
        self.postal_code_name = (By.NAME, "postalCode")
        self.agree_name = (By.NAME, "agreement")
        self.submit_xpath = (By.XPATH, "//button[@class='sc-gKHVLF cNEmgP mt-4']")
        self.holder_name = (By.NAME, "cardHolderName")
        self.card_no_name = (By.NAME, "cardNumber")
        self.exp_date_name = (By.NAME, "cardExpireYear")
        self.cvc_name = (By.NAME, "cardCvc")
        self.submit1_xpath = (By.XPATH, "//button[@class='sc-gKHVLF cNEmgP mt-4']")
        self.submit2_xpath = (By.XPATH, "//button[@class='sc-gKHVLF cNEmgP mt-4']")

    def open_page(self, url):
        self.driver.get(url)

    def signup_button(self):
        self.driver.find_element(*self.signup_button_xpath).click()

    def full(self, fn):
        self.driver.find_element(*self.full_name).send_keys(fn)

    def brokerage(self, br):
        self.driver.find_element(*self.brokerage_name).send_keys(br)

    def email_address(self, email_add):
        self.driver.find_element(*self.email_name).send_keys(email_add)

    def mobile(self, m):
        self.driver.find_element(*self.mobile_name).send_keys(m)

    def address(self, add):
        self.driver.find_element(*self.address_name).send_keys(add)

    def province(self):
        self.driver.find_element(*self.province_field_xpath).click()

    def city(self, c):
        self.driver.find_element(*self.city_name).send_keys(c)

    def postal_code(self, pc):
        self.driver.find_element(*self.postal_code_name).send_keys(pc)

    def agreement(self):
        self.driver.find_element(*self.agree_name).click()

    def step1(self):
        self.driver.find_element(*self.submit_xpath).click()

    def card_holder(self, ch):
        self.driver.find_element(*self.holder_name).send_keys(ch)

    def card_number(self, cn):
        self.driver.find_element(*self.card_no_name).send_keys(cn)

    def expire(self, ex):
        self.driver.find_element(*self.exp_date_name).send_keys(ex)

    def cvc(self, cv):
        self.driver.find_element(*self.cvc_name).send_keys(cv)

    def step2(self):
        self.driver.find_element(*self.submit1_xpath).click()

    def step3(self):
        self.driver.find_element(*self.submit2_xpath).click()












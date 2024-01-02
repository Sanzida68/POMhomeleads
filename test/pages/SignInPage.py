from selenium.webdriver.common.by import By


class SigninPage:
    def __init__(self, driver):
        self.driver = driver

        self.email_name = (By.NAME, "email")
        self.password_name = (By.NAME, "password")
        self.login_button_xpath = (By.XPATH, "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained "
                                             "MuiButton-containedPrimary MuiButton-sizeMedium "
                                             "MuiButton-containedSizeMedium MuiButton-fullWidth MuiButton-root "
                                             "MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium "
                                             "MuiButton-containedSizeMedium MuiButton-fullWidth mui-style-udkv93']")
        self.sign_in_button_xpath = (By.XPATH, "//button[@class='sc-gKHVLF bZUscr me-4']")

    def open_page(self, url):
        self.driver.get(url)

    def signin_button(self):
        self.driver.find_element(*self.sign_in_button_xpath).click()

    def enter_email(self, email):
        self.driver.find_element(*self.email_name).send_keys(email)

    def enter_pass(self, password):
        self.driver.find_element(*self.password_name).send_keys(password)

    def enter_signin(self):
        self.driver.find_element(*self.login_button_xpath).click()

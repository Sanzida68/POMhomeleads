from selenium.webdriver.common.by import By


class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

        self.profile_path = (By.XPATH, "//*[name()='path' and @d='M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 "
                                       "1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z']")
        self.logout_xpath = (By.XPATH, f"//li[@class='MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-root MuiMenuItem-gutters mui-style-1il4pon'][2]//span[@class='MuiTouchRipple-root mui-style-w0pj6f']")

    def click_profile(self):
        self.driver.find_element(*self.profile_path).click()

    def click_logout(self):
        self.driver.find_element(*self.logout_xpath).click()

from pages.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    sign_in_button_xpath = "//button[@class='sc-gKHVLF bZUscr me-4']"

    def click_on_sign_in(self):
        return self.element_click("sign_in_button_xpath", self.sign_in_button_xpath)

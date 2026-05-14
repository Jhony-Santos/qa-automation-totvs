from pages.base_page import BasePage


class HomePage(BasePage):

    URL = "https://automationexercise.com"

    SIGNUP_LOGIN_BUTTON = "a[href='/login']"
    PRODUCTS_BUTTON = "a[href='/products']"

    def access_home_page(self):
        self.navigate(self.URL)

    def click_signup_login(self):
        self.click(self.SIGNUP_LOGIN_BUTTON)

    def click_products(self):
        self.click(self.PRODUCTS_BUTTON)
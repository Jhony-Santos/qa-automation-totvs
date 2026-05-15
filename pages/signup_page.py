from pages.base_page import BasePage


class SignupPage(BasePage):

    NAME_INPUT = "input[data-qa='signup-name']"
    EMAIL_INPUT = "input[data-qa='signup-email']"
    SIGNUP_BUTTON = "button[data-qa='signup-button']"

    GENDER_MALE = "#id_gender1"
    PASSWORD_INPUT = "#password"

    DAY_SELECT = "#days"
    MONTH_SELECT = "#months"
    YEAR_SELECT = "#years"

    FIRST_NAME_INPUT = "#first_name"
    LAST_NAME_INPUT = "#last_name"
    ADDRESS_INPUT = "#address1"

    COUNTRY_SELECT = "#country"

    STATE_INPUT = "#state"
    CITY_INPUT = "#city"
    ZIPCODE_INPUT = "#zipcode"
    MOBILE_INPUT = "#mobile_number"

    CREATE_ACCOUNT_BUTTON = "button[data-qa='create-account']"

    ACCOUNT_CREATED_MESSAGE = "ACCOUNT CREATED!"
    CONTINUE_BUTTON = "a[data-qa='continue-button']"
    DELETE_ACCOUNT_BUTTON = "a[href='/delete_account']"
    ACCOUNT_DELETED_MESSAGE = "ACCOUNT DELETED!"

    def start_signup(self, user):
        self.fill(self.NAME_INPUT, user["name"])
        self.fill(self.EMAIL_INPUT, user["email"])

        self.click(self.SIGNUP_BUTTON)

        self.wait_for_visible(self.GENDER_MALE)

    def fill_account_information(self, user):
        self.click(self.GENDER_MALE)

        self.fill(self.PASSWORD_INPUT, user["password"])

        self.page.locator(self.DAY_SELECT).select_option("10")
        self.page.locator(self.MONTH_SELECT).select_option("5")
        self.page.locator(self.YEAR_SELECT).select_option("1995")

    def fill_address_information(self, user):
        self.fill(self.FIRST_NAME_INPUT, user["first_name"])
        self.fill(self.LAST_NAME_INPUT, user["last_name"])

        self.fill(self.ADDRESS_INPUT, user["address"])

        self.page.locator(self.COUNTRY_SELECT).select_option("Canada")

        self.fill(self.STATE_INPUT, user["state"])
        self.fill(self.CITY_INPUT, user["city"])
        self.fill(self.ZIPCODE_INPUT, user["zipcode"])
        self.fill(self.MOBILE_INPUT, user["mobile_number"])

    def create_account(self):
        self.click(self.CREATE_ACCOUNT_BUTTON)

    def validate_account_created(self):
        self.text_visible(self.ACCOUNT_CREATED_MESSAGE)

    def continue_after_account_created(self):
        self.click(self.CONTINUE_BUTTON)

    def delete_account(self):
        self.click(self.DELETE_ACCOUNT_BUTTON)

    def validate_account_deleted(self):
        self.text_visible(self.ACCOUNT_DELETED_MESSAGE)
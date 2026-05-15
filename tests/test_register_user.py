import pytest

from pages.home_page import HomePage
from pages.signup_page import SignupPage
from utils.data_factory import UserFactory


@pytest.mark.web
@pytest.mark.regression
def test_register_new_user_successfully(page):
    user = UserFactory.create_user()

    home_page = HomePage(page)
    signup_page = SignupPage(page)

    home_page.access_home_page()
    home_page.click_signup_login()

    signup_page.start_signup(user)
    signup_page.fill_account_information(user)
    signup_page.fill_address_information(user)
    signup_page.create_account()

    signup_page.validate_account_created()
    signup_page.continue_after_account_created()

    signup_page.delete_account()
    signup_page.validate_account_deleted()
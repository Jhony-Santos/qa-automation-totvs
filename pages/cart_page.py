from pages.base_page import BasePage
from playwright.sync_api import expect


class CartPage(BasePage):

    PRODUCT_NAME = ".cart_description h4 a"
    PRODUCT_PRICE = ".cart_price p"
    PRODUCT_QUANTITY = ".cart_quantity button"
    PRODUCT_TOTAL = ".cart_total_price"

    def validate_product_quantity(self, expected_quantity):
        expect(self.page.locator(self.PRODUCT_QUANTITY)).to_have_text(str(expected_quantity))

    def get_unit_price(self):
        price_text = self.page.locator(self.PRODUCT_PRICE).inner_text()
        return self._convert_price_to_number(price_text)

    def get_total_price(self):
        total_text = self.page.locator(self.PRODUCT_TOTAL).inner_text()
        return self._convert_price_to_number(total_text)

    def validate_total_price(self, expected_quantity):
        unit_price = self.get_unit_price()
        actual_total = self.get_total_price()
        expected_total = unit_price * expected_quantity

        assert actual_total == expected_total, (
            f"Expected total price {expected_total}, but got {actual_total}"
        )

    @staticmethod
    def _convert_price_to_number(price_text):
        return int(price_text.replace("Rs.", "").strip())
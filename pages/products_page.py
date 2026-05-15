from pages.base_page import BasePage


class ProductsPage(BasePage):

    FIRST_PRODUCT_VIEW_BUTTON = "a[href='/product_details/1']"
    PRODUCT_NAME = ".product-information h2"
    PRODUCT_PRICE = ".product-information span span"
    QUANTITY_INPUT = "#quantity"
    ADD_TO_CART_BUTTON = "button.cart"
    CART_MODAL = "#cartModal"
    VIEW_CART_LINK = "a[href='/view_cart']"

    def open_first_product_details(self):
        self.click(self.FIRST_PRODUCT_VIEW_BUTTON)

    def get_product_name(self):
        return self.page.locator(self.PRODUCT_NAME).inner_text().strip()

    def get_product_price(self):
        price_text = self.page.locator(self.PRODUCT_PRICE).inner_text()
        return self._convert_price_to_number(price_text)

    def set_quantity(self, quantity):
        self.fill(self.QUANTITY_INPUT, str(quantity))

    def add_product_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def go_to_cart(self):
        self.page.locator(self.CART_MODAL).locator(self.VIEW_CART_LINK).click()

    @staticmethod
    def _convert_price_to_number(price_text):
        return int(price_text.replace("Rs.", "").strip())
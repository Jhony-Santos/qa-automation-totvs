from pages.base_page import BasePage



class ProductsPage(BasePage):

    FIRST_PRODUCT_VIEW_BUTTON = "a[href='/product_details/1']"
    QUANTITY_INPUT = "#quantity"
    ADD_TO_CART_BUTTON = "button.cart"
    VIEW_CART_LINK = "u"

    def open_first_product_details(self):
        self.click(self.FIRST_PRODUCT_VIEW_BUTTON)

    def set_quantity(self, quantity):
        self.page.locator(self.QUANTITY_INPUT).fill(str(quantity))

    def add_product_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def go_to_cart(self):
        self.page.get_by_text("View Cart").click()
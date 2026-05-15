from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_add_four_units_to_cart_and_validate_summary(page):
    quantity = 4

    home_page = HomePage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    home_page.access_home_page()
    home_page.click_products()

    products_page.open_first_product_details()
    products_page.set_quantity(quantity)
    products_page.add_product_to_cart()
    products_page.go_to_cart()

    cart_page.validate_product_quantity(quantity)
    cart_page.validate_total_price(quantity)
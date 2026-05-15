import requests


class ProductsApi:

    BASE_URL = "https://automationexercise.com"

    def get_products_list(self):
        return requests.get(
            f"{self.BASE_URL}/api/productsList",
            timeout=30
        )
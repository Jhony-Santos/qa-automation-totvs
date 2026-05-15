import pytest

from api.products_api import ProductsApi


@pytest.mark.api
@pytest.mark.regression
def test_get_products_list_should_return_status_code_200_and_valid_products():
    products_api = ProductsApi()

    response = products_api.get_products_list()

    assert response.status_code == 200

    response_body = response.json()

    assert response_body is not None
    assert response_body["responseCode"] == 200
    assert "products" in response_body
    assert isinstance(response_body["products"], list)
    assert len(response_body["products"]) > 0

    required_fields = ["id", "name", "price", "brand", "category"]

    for product in response_body["products"]:
        for field in required_fields:
            assert field in product
            assert product[field] is not None
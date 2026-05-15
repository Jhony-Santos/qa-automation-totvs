from api.products_api import ProductsApi


def test_get_products_list_should_return_status_code_200_and_valid_products():
    products_api = ProductsApi()

    response = products_api.get_products_list()

    assert response.status_code == 200

    response_body = response.json()

    assert response_body is not None
    assert "products" in response_body
    assert isinstance(response_body["products"], list)
    assert len(response_body["products"]) > 0

    first_product = response_body["products"][0]

    assert first_product["id"] is not None
    assert first_product["name"] is not None
    assert first_product["price"] is not None
    assert first_product["brand"] is not None
    assert first_product["category"] is not None
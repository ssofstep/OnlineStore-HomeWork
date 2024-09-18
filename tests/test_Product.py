import pytest

from src.Product import Product


@pytest.fixture
def class_product() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


def test_init(class_product: Product) -> None:
    assert class_product.name == "Iphone 15"
    assert class_product.description == "512GB, Gray space"
    assert class_product.price == 210000.0
    assert class_product.quantity == 8

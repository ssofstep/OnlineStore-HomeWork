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


def test_new_product(class_product: Product) -> None:
    class_product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert class_product


@pytest.mark.parametrize("price1, price2", ([100, 100], [-100, 210000.0]))
def test_price(class_product: Product, price1: float, price2: float) -> None:
    class_product.price = price1
    assert class_product.price == price2

import pytest

from src.Category import Category
from src.Product import Product


@pytest.fixture
def class_category() -> Category:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство коммуникации и получения дополнительных функций",
        [
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ],
    )


def test_init(class_category: Category) -> None:
    assert class_category.name == "Смартфоны"
    assert class_category.description == "Смартфоны, как средство коммуникации и получения дополнительных функций"
    assert class_category.products[0].name == "Samsung Galaxy S23 Ultra"
    assert class_category.category_count == 1
    assert class_category.product_count == 3

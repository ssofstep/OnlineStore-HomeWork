import pytest

from src.LawnGrass import LawnGrass
from src.Smartphone import Smartphone


@pytest.fixture
def class_lawngrass() -> LawnGrass:
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20,
                     "Россия", "7 дней", "Зеленый")


def test_init(class_lawngrass: LawnGrass) -> None:
    assert class_lawngrass.name == "Газонная трава"
    assert class_lawngrass.description == "Элитная трава для газона"
    assert class_lawngrass.price == 500.0
    assert class_lawngrass.quantity == 20
    assert class_lawngrass.country == "Россия"
    assert class_lawngrass.germination_period == "7 дней"
    assert class_lawngrass.color == "Зеленый"


def test_add_true(class_lawngrass: LawnGrass) -> None:
    assert class_lawngrass.__add__(
        LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США",
                  "5 дней", "Темно-зеленый")) == 16750.0

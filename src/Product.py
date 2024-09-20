class Product:
    """Класс, который представляет продукты"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод, который инициализирует экземпляры класса"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_dict: dict) -> "Product":
        name, description, price, quantity = product_dict.values()
        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        if price == 0 or price < 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price

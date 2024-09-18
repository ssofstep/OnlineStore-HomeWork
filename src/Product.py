class Product:
    """Класс, который представляет продукты"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод, который инициализирует экземпляры класса"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

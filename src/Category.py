class Category:
    """Класс, который представляет категории"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """Метод, который инициализирует экземпляры класса"""
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)

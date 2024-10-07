from src.Product import Product


class Category:
    """Класс, который представляет категории"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """Метод, который инициализирует экземпляры класса"""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self) -> str:
        str_products = ""
        for product in self.__products:
            str_products += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
        return str_products

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {Category.product_count} шт."

    def middle_price(self) -> float:
        try:
            middle_price: float = sum(i.price for i in self.__products) / len(self.__products)
        except ZeroDivisionError:
            return 0.0
        else:
            return middle_price

"""Модуль моделей данных."""


from exceptions import (
    ProductError,
    InvalidQuantityError,
    InvalidPriceError,
    InvalidConditionError,
    WriteOffError,
)


class ProductCard:
    """Класс, предоставляющий карточку товара."""
    
    ALLOWED_CONDITIONS = (
    "Новое",
    "Новый остаток",
    "Повреждено",
    "Новая партия",
    "Испорчено",
    "Остаток",
    "Неликвид",
    "Уценённое",
)
    
    def __init__ (
            self,
            product_id: str,
            name: str,
            quantity: int,
            condition: str,
            supplier: str,
            manufacturer: str,
            price: float,
            location: str,
            city: str,
    ) -> None:
        """
        Инициализирует объект карточки товара.

        Args:
            product_id (int): Уникальный идентификатор товара.
            name (str): Наименование товара.
            quantity (int): Количество товара.
            condition (str): Состояние товара.
            supplier (str): Поставщик товара.
            manufacturer (str): Производитель товара.
            price (float): Стоимость товара.
            location (str): Местоположение товара.
            city (str): Город хранения товара.
        
        Raises:
            InvalidQuantityError: Если количество отрицательное.
            InvalidPriceError: Если цена отрицательная.
            InvalidConditionError: Если состояние недопустимо.
        """
        
        if quantity < 0:
            
            raise InvalidQuantityError(
                "Количество не может быть отрицательным."
            )
        
        if price < 0:
            
            raise InvalidPriceError(
                "Стоимость не может быть отрицательной."
            )
        
        if condition not in self.ALLOWED_CONDITIONS:
            
            raise InvalidConditionError("Недопустимое состояние.")

        self._id = product_id
        self._name = name
        self._quantity = quantity
        self._condition = condition
        self._supplier = supplier
        self._manufacturer = manufacturer
        self._price = price
        self._location = location
        self._city = city

    """Геттеры."""
    
    @property
    def id(self) -> str:
        
        return self._id
    
    @property
    def name(self) -> str:
        
        return self._name
    
    @property
    def quantity(self) -> int:
        
        return self._quantity
    
    @property
    def condition(self) -> str:
       
        return self._condition
    
    @property
    def supplier(self) -> str:
        
        return self._supplier
    
    @property
    def manufacturer(self) -> str:
        
        return self._manufacturer

    @property
    def price(self) -> float:
        
        return self._price

    @property
    def location(self) -> str:
        
        return self._location

    @property
    def city(self) -> str:
        
        return self._city
    
    """Сеттеры."""
    
    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @quantity.setter
    def quantity(self, value: int) -> None:
        if value < 0:
            
            raise InvalidQuantityError("Количество не может быть отрицательным.")
        self._quantity = value

    @condition.setter
    def condition(self, value: str) -> None:
        if value not in self.ALLOWED_CONDITIONS:
            
            raise InvalidConditionError("Недопустимое состояние.")
        self._condition = value

    @supplier.setter
    def supplier(self, value: str) -> None:
        self._supplier = value

    @manufacturer.setter
    def manufacturer(self, value: str) -> None:
        self._manufacturer = value

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            
            raise InvalidPriceError("Цена не может быть отрицательной.")
        self._price = value

    @location.setter
    def location(self, value: str) -> None:
        self._location = value

    @city.setter
    def city(self, value: str) -> None:
        self._city = value


class ProductManager:
    """Менеджер товаров."""

    def __init__(self) -> None:
        self.products = {}

    def add_product(self, product: ProductCard) -> None:
        """
        Добавляет товар в систему.

        Args:
            product (ProductCard): Объект карточки товара.

        Returns:
            None
        """
        
        self.products[product.id] = product

    def get_product(self, product_id: str) -> ProductCard | None:
        """
        Возвращает товар по его идентификатору.

        Args:
            product_id (str): Идентификатор товара.
        
        Returns:
            ProductCard | None: Объект товара, если найден,
            иначе None.
        """
        
        return self.products.get(product_id)

    def delete_product(self, product_id: str) -> None:
        """
        Удаляет товар из системы по ID.

        Args:
            product_id (str): Идентификатор товара.
        
        Raises:
            Exception: Если товар не найден.
        
        Returns:
            None
        """
        
        if product_id not in self.products:
            
            raise Exception("Товар не найден.")
        
        del self.products[product_id]

    def generate_id(self) -> str:
        """
        Генерирует новый уникальный ID вида TXXX.

        Returns:
            str: Новый уникальный идентификатор.
        """

        if not self.products:
            
            return "T001"

        numbers = []

        for product_id in self.products.keys():
            number = int(product_id.replace("T", ""))
            numbers.append(number)

        max_number = max(numbers)

        new_number = max_number + 1

        return f"T{new_number:03d}"

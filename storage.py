"""Модуль работы с файлами."""


import json
from models import ProductCard


def load_from_txt(filename: str) -> list[ProductCard]:
    """
    Загружает товары из TXT-формата.
    
    Формат строки файла:
    №;ID;Наименование;Количество;Состояние;
    Поставщик;Производитель;Стоимость;Местоположение;Город

    Args:
        filename (str): Имя TXT-файла.

    Returns:
        list[ProductCard]: Список объектов товаров.
    """
    
    products = []

    with open(filename, "r", encoding = "utf-8") as file:
        next(file)

        for line in file:
            parts = line.strip().split(";")

            product_id = parts[1]
            name = parts[2]
            quantity = int(parts[3])
            condition = parts[4]
            supplier = parts[5]
            manufacturer = parts[6]
            price = float(parts[7].replace(" руб.", ""))
            location = parts[8]
            city = parts[9]

            product = ProductCard(
                product_id,
                name,
                quantity,
                condition,
                supplier,
                manufacturer,
                price,
                location,
                city,
            )

            products.append(product)

    return products

def load_from_json(filename: str) -> list[ProductCard]:
    """
    Загружает товары из JSON-файла.

    Args:
        filename (str): Имя JSON-файла.

    Returns:
        list[ProductCard]: Список объектов товаров.
    """
    
    products = []

    with open(filename, "r", encoding = "utf-8") as file:
        data = json.load(file)
    
    for item in data:
        product = ProductCard(
            item["id"],
            item["name"],
            item["quantity"],
            item["condition"],
            item["supplier"],
            item["manufacturer"],
            item["price"],
            item["location"],
            item["city"],
        )
        products.append(product)

    return products

def save_to_json(filename: str, products: dict) -> None:
    """
    Сохраняет текущие товары в JSON-файл.

    Args:
        filename (str): Имя JSON-файла.
        products (dict[str, ProductCard]): Словарь товаров.

    Returns:
        None
    """

    data = []

    for product in products.values():
        data.append({
            "id": product.id,
            "name": product.name,
            "quantity": product.quantity,
            "condition": product.condition,
            "supplier": product.supplier,
            "manufacturer": product.manufacturer,
            "price": product.price,
            "location": product.location,
            "city": product.city
        })
    
    with open(filename, "w", encoding = "utf-8") as file:
        json.dump(data, file, ensure_ascii = False, indent = 4)

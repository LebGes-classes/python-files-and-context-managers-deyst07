"""Точка входа в программу."""


from models import ProductManager
import storage
from menu import Menu


def main() -> None:
    """
    Основная функция программы.

    Returns:
        None
    """

    manager = ProductManager()

    print("1 - Загрузить TXT")
    print("2 - Загрузить JSON")
    print("3 - Пустая база")

    choice = input("Выбор: ")

    if choice == "1":
        products = storage.load_from_txt("data.txt")
        
        for product in products:
            manager.add_product(product)

    elif choice == "2":
        products = storage.load_from_json("data.json")
        
        for product in products:
            manager.add_product(product)

    menu = Menu(manager, storage)
    menu.run()


if __name__ == "__main__":
    main()

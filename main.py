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

    is_running = True

    while is_running:
        print("\nВыберите источник данных: ")
        print("1 - Загрузить TXT")
        print("2 - Загрузить JSON")
        print("3 - Пустая база")

        choice = input("Выбор: ")

        if choice == "1":
            products = storage.load_from_txt("data.txt")
            
            for product in products:
                manager.add_product(product)

            is_running = False

        elif choice == "2":
            products = storage.load_from_json("data.json")
            
            for product in products:
                manager.add_product(product)
            
            is_running = False

        elif choice == "3":
            
            print("Создана пустая база.")
            
            is_running = False

        else:
            
            print("Неверный ввод. Попробуйте снова.")

    menu = Menu(manager, storage)
    menu.run()

    save_choice = input("Сохранить изменения в JSON? (y/n): ")

    if save_choice.lower() == "y":
        storage.save_to_json("data.json", manager.products)


if __name__ == "__main__":
    main()

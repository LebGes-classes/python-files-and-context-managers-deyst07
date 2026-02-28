"""Модуль пользовательского интерфейса."""


from exceptions import ProductError
from models import ProductCard


class Menu:
    """Класс консольного меню."""

    def __init__(self, manager, storage) -> None:
        self.manager = manager
        self.storage = storage
        self.is_running = True

    def run(self) -> None:
        """
        Запускает основной цикл меню.

        Returns:
            None
        """

        while self.is_running:
            
            print("\n1 - Показать товары")
            print("2 - Добавить товар")
            print("3 - Изменить товар")
            print("4 - Удалить товар")
            print("5 - Сохранить в JSON")
            print("0 - Выход")

            choice = input("Выбор: ")

            try:
                match choice:
                    case "1":
                        self.show_products()
                    case "2":
                        self.add_product()
                    case "3":
                        self.edit_product()
                    case "4":
                        product_id = input("ID: ")
                        self.manager.delete_product(product_id)
                    case "5":
                        self.storage.save_to_json("data.json", self.manager.products)
                        
                        print("Сохранено.")
                    case "0":
                        self.is_running = False
                    case _:
                        
                        print("Неверный ввод.")
            
            except ProductError as error:
                
                print("Ошибка:", error)

    def show_products(self) -> None:
        """
        Выводит все товары в виде таблицы.

        Returns:
            None
        """

        if not self.manager.products:
            
            print("Список товаров пуст.")
            
            return

        print("\n" + "=" * 130)
        print(
            "№ | ID    | Наименование                           | Кол-во | Состояние        | Поставщик               | Производитель      | Цена   | Место       | Город"
        )
        print("=" * 130)

        number = 1

        for product in self.manager.products.values():
            print(
                f"{number:<2} | "
                f"{product.id:<5} | "
                f"{product.name[:35]:<35} | "
                f"{product.quantity:<7} | "
                f"{product.condition[:16]:<16} | "
                f"{product.supplier[:23]:<23} | "
                f"{product.manufacturer[:18]:<18} | "
                f"{product.price:<6} | "
                f"{product.location[:11]:<11} | "
                f"{product.city}"
            )
            number += 1

        print("=" * 130)

    def add_product(self) -> None:
        """
        Добавляет новый товар в систему.

        Returns:
            None
        """

        product_id = self.manager.generate_id()

        print(f"Сгенерирован ID: {product_id}")

        name = input("Наименование: ")
        quantity = int(input("Количество: "))
        condition = input("Состояние: ")
        supplier = input("Поставщик: ")
        manufacturer = input("Производитель: ")
        price = float(input("Цена: "))
        location = input("Местоположение: ")
        city = input("Город: ")

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

        self.manager.add_product(product)

        print("Товар добавлен.")
    
    def edit_product(self) -> None:
        """
        Изменяет характеристики товара.

        Returns:
            None
        """

        product_id = input("ID товара: ")
        product = self.manager.get_product(product_id)

        if not product:
            
            print("Товар не найден.")
            
            return

        is_editing = True

        while is_editing:
            
            print("\nЧто изменить?")
            print("1 - Наименование")
            print("2 - Количество")
            print("3 - Состояние")
            print("4 - Поставщик")
            print("5 - Производитель")
            print("6 - Цена")
            print("7 - Местоположение")
            print("8 - Город")
            print("0 - Назад")

            choice = input("Выбор: ")

            try:
                if choice == "1":
                    product.name = input("Новое наименование: ")

                elif choice == "2":
                    product.quantity = int(input("Новое количество: "))

                elif choice == "3":
                    product.condition = input("Новое состояние: ")

                elif choice == "4":
                    product.supplier = input("Новый поставщик: ")

                elif choice == "5":
                    product.manufacturer = input("Новый производитель: ")

                elif choice == "6":
                    product.price = float(input("Новая цена: "))

                elif choice == "7":
                    product.location = input("Новое местоположение: ")

                elif choice == "8":
                    product.city = input("Новый город: ")

                elif choice == "0":
                    is_editing = False

                else:
                    
                    print("Неверный ввод.")

            except Exception as error:
                
                print("Ошибка:", error)

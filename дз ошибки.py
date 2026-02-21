STATUS = ['принято к учёту', 'состоит на учёте', 'в ремонте', 'списано', 'зарезервировано']


class ItemCards:
    list_of_cards = []

    def __init__(self, name: str, count: int, status: str, supplier: str,
                 manufacturer: str, price: float, location: str, size: str,
                 country_of_origin: str, strength: str, card_id: int) -> None:
        """Инициализация/конструктор класса.

                Args:
                    name: Наименование.
                    count: Количество.
                    status: Статус.
                    supplier: Поставщик.
                    manufacturer: Производитель .
                    price: Цена.
                    location: Местоположение .
                    size: Размер.
                    country_of_origin: Страна производства.
                    strength: Прочность .
                    card_id: ID товара.
        """

        for card in ItemCards.list_of_cards:
            if card.get_card_id() == card_id:
                raise ValueError(f"Карточка с ID {card_id} уже существует")

        self.__name = name
        self.__count = count
        self.__status = status
        self.__supplier = supplier
        self.__manufacturer = manufacturer
        self.__price = price
        self.__location = location
        self.__size = size
        self.__country_of_origin = country_of_origin
        self.__strength = strength
        self.__card_id = card_id

        # Добавляем карточку в общий список
        ItemCards.list_of_cards.append(self)

    # Сеттер и геттер для card_id
    def set_card_id(self, card_id: int) -> None:
        """Сеттер для ID товара.

                Args:
                    card_id: ID товара.
        """

        if isinstance(card_id, int) and card_id >= 0:
            # Проверяем уникальность ID (исключая текущую карточку)
            for card in ItemCards.list_of_cards:
                if card != self and card.get_card_id() == card_id:
                    raise ValueError(f"Карточка с ID {card_id} уже существует")
            self.__card_id = card_id
        else:
            raise ValueError("ID карточки должно быть целым положительным числом")

    def get_card_id(self) -> int:
        """Геттер для ID товара.

                Returns:
                    card_id: ID товара.
        """

        return self.__card_id

    # Сеттер и геттер для name
    def set_name(self, name: str) -> None:
        """Сеттер для наименования товара.

                Args:
                    name: наименования товара.
        """

        if isinstance(name, str) and name.strip():
            self.__name = name.strip()
        else:
            raise ValueError("Наименование должно быть строкой и не может быть пустым")

    def get_name(self) -> str:
        """Геттер для наименования товара.

                Returns:
                    name: наименования товара.
        """

        return self.__name

    # Сеттер и геттер для count
    def set_count(self, count: int) -> None:
        """Сеттер для количества товара.

                Args:
                    count: количество товара.
        """

        if isinstance(count, int) and count >= 0:
            self.__count = count
        else:
            raise ValueError("Количество должно быть целым положительным числом")

    def get_count(self) -> int:
        """Геттер для количества товара.

                Returns:
                    count: количество товара.
        """

        return self.__count

    # Сеттер и геттер для status
    def set_status(self, status: str) -> None:
        """Сеттер для статуса товара.

                Args:
                    status: статус товара.
        """

        if isinstance(status, str) and status.strip():
            if status not in STATUS:
                raise ValueError(f'Статус должен быть одним из: {", ".join(STATUS)}')
            self.__status = status
        else:
            raise ValueError("Статус должен быть строкой и не может быть пустым")

    def get_status(self) -> str:
        """Геттер для размера товара.

                Returns:
                    status:статус товара.
        """

        return self.__status

    # Сеттер и геттер для supplier
    def set_supplier(self, supplier):
        """Сеттер для поставщика.

                Args:
                    supplier: поставщик.
        """

        if isinstance(supplier, str) and supplier.strip():
            self.__supplier = supplier.strip()
        else:
            raise ValueError("Поставщик должен быть строкой и не может быть пустым")

    def get_supplier(self) -> str:
        """Геттер для поставщика.

                Returns:
                    supplier: поставщик.
        """

        return self.__supplier

    # Сеттер и геттер для manufacturer
    def set_manufacturer(self, manufacturer: str) -> None:
        """Сеттер для производителя.

                Args:
                    manufacturer: производитель.
        """

        if isinstance(manufacturer, str) and manufacturer.strip():
            self.__manufacturer = manufacturer.strip()
        else:
            raise ValueError("Производитель должен быть строкой и не может быть пустым")

    def get_manufacturer(self) -> str:
        """Геттер для производителя.

                Returns:
                    manufacturer: производитель.
        """

        return self.__manufacturer

    # Сеттер и геттер для price
    def set_price(self, price: float) -> None:
        """Сеттер для стоимости товара.

                 Args:
                     price: стоимость товара.
        """

        if isinstance(price, (int, float)):
            if price >= 0:
                self.__price = float(price)
            else:
                raise ValueError("Стоимость должна быть неотрицательным числом")
        else:
            raise ValueError("Стоимость должна быть числом")

    def get_price(self) -> float:
        """Геттер для стоимости товара.

                Returns:
                    price: стоимость товара.
        """

        return self.__price

    # Сеттер и геттер для location
    def set_location(self, location: str) -> None:
        """Сеттер для местоположения товара.

                Args:
                    location: местоположение товара.
        """

        if isinstance(location, str) and location.strip():
            self.__location = location.strip()
        else:
            raise ValueError("Местоположение должно быть строкой и не может быть пустым")

    def get_location(self) -> str:
        """Геттер для местоположения товара.

                Returns::
                    location: местоположение товара.
        """

        return self.__location

    # Сеттер и геттер для size
    def set_size(self, size: str) -> None:
        """Сеттер для размера товара.

                Args:
                    size: размера товара.
        """

        if isinstance(size, str) and size.strip():
            self.__size = size.strip()
        else:
            raise ValueError("Размер должен быть строкой и не может быть пустым")

    def get_size(self) -> str:
        """Геттер для размера товара.

                Returns:
                    size: размера товара.
        """

        return self.__size

    # Сеттер и геттер для country_of_origin
    def set_country_of_origin(self, country_of_origin: str) -> None:
        """Сеттер для страны производства.

                Args:
                    country_of_origin: страна производства.
        """

        if isinstance(country_of_origin, str) and country_of_origin.strip():
            self.__country_of_origin = country_of_origin.strip()
        else:
            raise ValueError("Страна происхождения должна быть строкой и не может быть пустой")

    def get_country_of_origin(self) -> str:
        """Геттер для страны производства.

                Returns:
                     country_of_origin: страна производства.
        """

        return self.__country_of_origin

    # Сеттер и геттер для strength
    def set_strength(self, strength: str) -> None:
        """Сеттер для прочности товара.

                Args:
                    strength: прочность товара.
        """

        if isinstance(strength, str) and strength.strip():
            self.__strength = strength.strip()
        else:
            raise ValueError("Прочность должна быть строкой и не может быть пустой")

    def get_strength(self) -> str:
        """Геттер для прочности товара.

                Returns:
                    strength: прочность товара.
        """

        return self.__strength

    # Списание карточки
    def write_off_card(self) -> None:
        """Метод для списания карты"""

        if self.__status not in ['принято к учёту', 'состоит на учёте']:
            raise ValueError(
                f"Невозможно списать товар со статусом '{self.__status}'. "
                "Списание разрешено только при статусах: 'принято к учёту' или 'состоит на учёте'"
            )
        if self.__count <= 0:
            raise ValueError("Невозможно списать товар с нулевым количеством")

        self.__status = 'списано'
        self.__count = 0

    # Метод для получения всех данных карточки
    def show_all_data(self) -> dict:
        """Метод для вывода всех данных о товаре

                Returns:
                    словарь со значениями и данными из карточки
        """

        return {
            'ID товара': self.__card_id,
            'Наименование': self.__name,
            'Количество': self.__count,
            'Статус': self.__status,
            'Поставщик': self.__supplier,
            'Производитель': self.__manufacturer,
            'Стоимость': self.__price,
            'Местоположение': self.__location,
            'Размер': self.__size,
            'Страна производства': self.__country_of_origin,
            'Прочность': self.__strength
        }


def menu():
    """Метод для работы пользовательского меню"""

    while True:
        print("\n     МЕНЮ     ")
        print("1. Создать карточку")
        print("2. Показать все карточки")
        print("3. Найти карточку по ID")
        print("4. Изменить карточку")
        print("5. Списать товар")
        print("6. Удалить карточку")
        print("0. Выход")

        choice = input("Выберите действие: ")

        match choice:
            case '1':
                create()
            case '2':
                show_all()
            case '3':
                find()
            case '4':
                edit()
            case '5':
                write_off()
            case '6':
                delete()
            case '0':
                break


def create():
    """Метод для создания карточки товара"""

    try:
        new_card = None
        id_ok = False
        while not id_ok:
            card_id = int(input("ID карточки: "))
            id_ok = True
            for card in ItemCards.list_of_cards:
                if card.get_card_id() == card_id:
                    print("Такой ID уже существует!")
                    id_ok = False

        name = input("Наименование: ")
        count = int(input("Количество: "))

        print("Статусы:")
        print("1 - принято к учёту")
        print("2 - состоит на учёте")
        print("3 - в ремонте")
        print("4 - списано")
        print("5 - зарезервировано")

        s_ok = False
        while not s_ok:
            s = int(input("Выберите статус (1-5): "))
            if 1 <= s <= 5:
                status = STATUS[s - 1]
                s_ok = True
            else:
                print("Введите число от 1 до 5")

        supplier = input("Поставщик: ")
        manufacturer = input("Производитель: ")
        price = float(input("Стоимость: "))
        location = input("Местоположение: ")
        size = input("Размер: ")
        country = input("Страна происхождения: ")
        strength = input("Прочность: ")

        new_card = ItemCards(name, count, status, supplier, manufacturer, price,
                             location, size, country, strength, card_id)
        print(new_card.show_all_data())

    except:
        print("Ошибка при создании карточки")


def show_all():
    """Метод для вывода всех карточек"""

    if not ItemCards.list_of_cards:
        print("Карточек нет")
    else:
        for card in ItemCards.list_of_cards:
            print(card.show_all_data())


def find():
    """Метод для нахождения определенной карточки"""

    try:
        card_id = int(input("Введите ID карточки: "))
        found = False
        for card in ItemCards.list_of_cards:
            if card.get_card_id() == card_id:
                card.show_all_data()
                found = True
        if not found:
            print("Карточка не найдена")
    except:
        print("Ошибка ввода")


def edit():
    """Метод для изменения карточки товара"""

    try:
        card_id = int(input("Введите ID карточки: "))
        card = None
        for c in ItemCards.list_of_cards:
            if c.get_card_id() == card_id:
                card = c

        if card is None:
            print("Карточка не найдена")
            return

        print("Что хотите изменить?")
        print("1 - наименование")
        print("2 - количество")
        print("3 - статус")
        print("4 - поставщика")
        print("5 - производителя")
        print("6 - стоимость")
        print("7 - местоположение")
        print("8 - размер")
        print("9 - страну происхождения")
        print("10 - прочность")

        choice2 = input("Ваш выбор: ")

        match choice2:
            case '1':
                card.set_name(input("Новое наименование: "))
            case '2':
                card.set_count(int(input("Новое количество: ")))
            case '3':
                print("1 - принято к учёту")
                print("2 - состоит на учёте")
                print("3 - в ремонте")
                print("4 - списано")
                print("5 - зарезервировано")
                s = int(input("Новый статус (1-5): "))
                card.set_status(STATUS[s - 1])
            case '4':
                card.set_supplier(input("Новый поставщик: "))
            case '5':
                card.set_manufacturer(input("Новый производитель: "))
            case '6':
                card.set_price(float(input("Новая стоимость: ")))
            case '7':
                card.set_location(input("Новое местоположение: "))
            case '8':
                card.set_size(input("Новый размер: "))
            case '9':
                card.set_country_of_origin(input("Новая страна происхождения: "))
            case '10':
                card.set_strength(input("Новая прочность: "))
    except:
        print(" Ошибка при редактировании")


def write_off():
    """Метод для cписания карточки товара"""

    try:
        card_id = int(input("Введите ID карточки: "))
        found = False
        for card in ItemCards.list_of_cards:
            if card.get_card_id() == card_id:
                found = True
                print(f"Товар: {card.get_name()}")
                print(f"Текущий статус: {card.get_status()}")
                print(f"Количество: {card.get_count()}")

                card.write_off_card()

        if not found:
            print("Карточка не найдена")

    except:
        print(" Ошибка при списании")


def delete():
    """Метод для удаления карточки товара"""
    
    try:
        card_id = int(input("Введите ID карточки: "))
        found = False
        i = 0
        while i < len(ItemCards.list_of_cards):
            if ItemCards.list_of_cards[i].get_card_id() == card_id:
                found = True
                if ItemCards.list_of_cards[i].get_status() == 'списано':
                    del ItemCards.list_of_cards[i]
                    print(" Карточка удалена")
                    i = i - 1

                else:
                    print("Можно удалять только списанные товары")
            i = i + 1

        if not found:
            print("Карточка не найдена")

    except:
        print(" Ошибка при удалении")


menu()






















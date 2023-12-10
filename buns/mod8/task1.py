class Transport:
    def __init__(self, coordinates: tuple[float, float], speed: int, brand: str, year: int, number: str):
        self.__coordinates: coordinates
        self.__speed = speed
        self.__brand = brand
        self.__year = year
        self.__number = number

    @property
    def coordinates(self) -> tuple:
        if len(self.__coordinates) == 2:
            return self.__coordinates

    @coordinates.setter
    def coordinates(self, coordinates: tuple) -> None:
        flag = True
        for coordinate in coordinates:
            if not isinstance(coordinate, float):
                flag = False
        if flag:
            self.__coordinates = coordinates

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed: int) -> None:
        if isinstance(speed, int):
            self.__speed = speed

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand_name) -> None:
        if isinstance(brand_name, str):
            self.__brand = brand_name

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: int) -> None:
        if isinstance(year, int):
            self.__year = year

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: str) -> None:
        if isinstance(number, str):
            self.__number = number


    def __str__(self):
        '''
           Представление всей информации для вывода в методе print()
        '''
        return (f"Координаты: x = {self.coordinates[0]}, y = {self.coordinates[1]}\n"
                f"Скорость: {self.speed}\n"
                f"Бренд: {self.brand}\n"
                f"Год выпуска: {self.year}\n"
                f"Номер: {self.number}")

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        """
        Присутствие транспортного средства в пределах заданной области
        pos_x, pos_y - координата левого верхнего угла области
        length, width - длина и ширина области
        """
        if (pos_x < self.coordinates[0] < pos_x + width and
                pos_y - length < self.__coordinates[1] < pos_y):
            return True
        return False


class Passenger:
    def __init__(self, passengers_capacity: int, number_of_passengers: int):
        self.__passengers_capacity = passengers_capacity
        self.__number_of_passengers = number_of_passengers
    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity) -> None:
        if isinstance(passengers_capacity, int):
            self.__passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers) -> None:
        if isinstance(number_of_passengers, int):
            if number_of_passengers <= self.__passengers_capacity:
                self.__number_of_passengers = number_of_passengers


class Cargo:
    def __init__(self, carrying: bool, name: str, address: str):
        self.__carrying = carrying
        self.__name = name
        self.__address = address
    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying) -> None:
        if isinstance(carrying, bool):
            self.__carrying = carrying

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if isinstance(name, str):
            self.__name = name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str) -> None:
        if isinstance(address, str):
            self.__address = address

class Plane(Transport):
    def __init__(self, coordinates: tuple[float, float], speed: int, brand: str,
                 year: int, number: str, height: int):
        super().__init__(coordinates, speed, brand, year, number)
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height) -> None:
        if isinstance(height, int):
            self.__height = height


class Auto(Transport):
    def __init__(self, coordinates: tuple[float, float], speed: int, brand: str,
                 year: int, number: str, body_type: str, color: str, height: int):
        super().__init__(coordinates, speed, brand, year, number)
        self.__body_type = body_type
        self.__color = color
        self.__height = height

    @property
    def body_type(self):
        return self.__body_type

    @body_type.setter
    def body_type(self, body_type) -> None:
        if isinstance(body_type, str):
            self.__body_type = body_type

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color) -> None:
        if isinstance(color, str):
            self.__color = color

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height) -> None:
        if isinstance(height, int):
            self.__height = height

class Ship(Transport):
    def __init__(self, port: str, coordinates: tuple[float, float], speed: int, brand: str,
                 year: int, number: str, color: str, height: int):
        super().__init__(coordinates, speed, brand, year, number)
        self.__port = port
        self.__color = color
        self.__height = height

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color) -> None:
        if isinstance(color, str):
            self.__color = color

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height) -> None:
        if isinstance(height, int):
            self.__height = height

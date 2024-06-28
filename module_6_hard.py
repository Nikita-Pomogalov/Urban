import math
from colorama import Fore


class Figure:
    sides_count = 0

    def __init__(self, color, sides):
        self.__color = color
        self.__sides = sides

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
            print(f'Цвет изменён на {self.__color}')
        else:
            print('Цвет не изменён')

    def __is_valid_sides(self, *args):
        if len(args) == len(self.__sides):
            for side in args:
                if isinstance(side, int) and side > 0:
                    return True
                else:
                    return False
        else:
            return False

    def get_sides(self):
        if self.sides_count == 1:
            return [*self.__sides]
        return self.__sides

    def set_sides(self, *count):
        if len(count) == self.sides_count:
            self.__sides = count

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        a=[]
        for i in sides:
            a.append(i)
            if len(a) > 1:
                sides = 1
                super().__init__(color, sides)
            else:
                radius = i / (2 * math.pi)
                super().__init__(color, radius)

    def get_radius(self):
        return self.get_sides()[0] / 2

    def get_square(self):
        square = self.get_sides()[0] * self.get_sides()[0] * math.pi
        return f'Площадь круга: {square}'


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        a = []
        for i in sides:
            a.append(i)
        if len(a) != 3:
            sides = 1
            super().__init__(color, sides)
        else:
            super().__init__(color, sides)

    def get_square(self):
        a, b, c = self.get_sides()
        half_per = (a + b + c) / 2
        s = math.sqrt(half_per * (half_per - a) * (half_per - b) * (half_per - c))
        return s

    def get_height(self):
        a, b, c = self.get_sides()
        height = (self.get_square() * 2) / a
        return height


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        a = []
        for i in sides:
            a.append(i)
            if len(a) == 1:
                super().__init__(color, [*sides] * 12)
            else:
                sides = 1
                super().__init__(color, [sides] * 12)

    def get_volume(self):
        return self.get_sides()[0] ** 3


# Проверка по условию задания __________________________________________________________________________________________
print(Fore.BLUE, 'ПРОВЕРКА ПО УСЛОВИЮ ЗАДАНИЯ')
circle1 = Circle((200, 200, 100), 10, 1, 3, 3) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
cube1.set_color(300, 70, 15) # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
circle1.set_sides(15) # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
print(Fore.BLUE, 'КОНЕЦ ПРОВЕРКИ ПО УСЛОВИЮ ЗАДАНИЯ')

# Дополнительная проверка_______________________________________________________________________________________________
# Для Circle
print(Fore.RED, f'\n\nДОПОЛНИТЕЛЬНАЯ ПРОВЕРКА')
print(Fore.YELLOW, '\nКРУГ')
print(circle1.get_square())  # circle.set_sides(15)
print(circle1.get_radius()) # Если 15 имеется ввиду диаметр (длина стороны), то радиус это половина диаметра


# Для треугольника (Для куба все проверки в примере пройдены)
print(Fore.GREEN, '\nТРЕУГОЛЬНИК')
tr1 = Triangle((100, 100, 100), 3, 5, 4)
print(tr1.get_color())
print(tr1.get_sides())
print(tr1.get_height())
print(tr1.get_square())

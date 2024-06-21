# class Human:
#     head = True
#     _legs = True
#     __arms = True
#
#     def say_hello(self):
#         print('Здраствуйте')
#
#     def about(self):
#         print(self.head)
#         print(self._legs)
#         print(self.__arms)
#
# class Student(Human):
#     pass
#     # def about(self):
#     #     print('Я студент')
#
#
# class Teacher(Human):
#     pass
#
# human = Human()
# human.about()
#
# student = Student()

import re
class Vehicle:
        __COLOR_VARIANTS_ = ['blue', 'red', 'green', 'black', 'white', 'YELLOW']
        __COLOR_VARIANTS = []
        for x in __COLOR_VARIANTS_:
            x = x.lower()
            __COLOR_VARIANTS.append(x)

        def __init__(self, owner, model, color, engine_power):
            self.owner = owner
            self.__model = str(model)
            self.__engine_power = int(engine_power)
            self.__color = str(color)
            if self.__color in self.__COLOR_VARIANTS:
                print('all good')
            else:
                self.__color = "Не определён"

        def get_model(self):
            print(f'Модель: {self.__model}')

        def get_horsepower(self):
            print(f'Мощность двигателя: {self.__engine_power}')

        def get_color(self):
            print(f'Цвет: {self.__color}')

        def print_info(self):
            self.get_model()
            self.get_horsepower()
            self.get_color()
            print(f'Владелец: {self.owner}')

        def set_color(self, new_color):
            if new_color.lower() in self.__COLOR_VARIANTS:
                self.__color = new_color
                print(f'Цвет изменен на {new_color.lower()}')
            else:
                print(f'Невозможно покрасить в {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()
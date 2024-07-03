class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers

        self.__is_valid_vin(self.__vin)
        self.__is_valid_numbers(self.__numbers)

    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int) == False:
            raise IncorrectVinNumber(message='Некорректный тип vin номер')
        elif not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber(message='Неверный диапозон для vin номера')
        else:
            return True

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str) == False:
            raise IncorrectCarNumbers(message='Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers(message='Неверная длина номера')
        else:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


# Модель 1 (Будет создан)

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

# Модель 2 (Неверный диапозон Vin)

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

# Модель 3 (Неверная длина номера)

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')


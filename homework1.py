num1 = 3
num2 = 5
sum = num1 + num2
print(sum)
result = sum + num1 * num2
print(result)


#NEW HOMETASK 

# 1st program
result = 9 ** 0.5 * 5
print(result)  # Ожидаемый результат: 15.0

# 2nd program
result = (9.99 > 9.98) and (1000 != 1000.1)
print(result)  # Ожидаемый результат: True

# 3rd program
without_priority = 2 * 2 + 2
with_priority = 2 * (2 + 2)
comparison_result = without_priority == with_priority

print(without_priority)  # Вывод: 6
print(with_priority)      # Вывод: 8
print(comparison_result)  # Ожидаемый результат: False

# 4th program
number_str = '123.456'
number_float = float(number_str)  # Преобразование в дробное число
shifted_number = number_float * 10  # Умножаем на 10, чтобы получить 1234.56
first_digit_after_decimal = int(shifted_number) % 10  # Получаем первую цифру после запятой

print(first_digit_after_decimal)  # Ожидаемый результат: 4

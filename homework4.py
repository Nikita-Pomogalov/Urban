immutable_var = (2, 'Hello', [1, 3], True)
print(immutable_var)
# immutable_var[2] = 15 - невозможная операция, так как
# выведется ошибка, которая сообщает о том, что кортеж не поддерживает обращение по элементам

mutable_list = [3, 'Привет', True, 5]
mutable_list[3] = False
print(mutable_list)
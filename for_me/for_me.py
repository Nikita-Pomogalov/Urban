# def by_3(x):
#     return x * 3
#
#
# def is_odd(x):
#     return x % 2
#
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]
# result = [x * y for x in my_numbers for y in they_numbers if x % 2 and y // 2]
# print(result)

# import time
#
# start_time = time.time()
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# result = (x ** 3000 for x in my_numbers)
# print(result)
#
# for elem in result:
#     print(elem)
#
# finish_time = time.time()
# print(f'Время в миллисекундах: {(finish_time - start_time)*1000}')

# list_1 = [1, 5, 9, 29, 4]
# list_2 = [5, 2, 9, 1, 2]
#
#
# ran = range(10, 30)
# zp = zip(list_1, list_2)
# mp = map(str, list_1)
#
# print(ran, zp, mp)
# print(list(ran))
# print(list(zp))
# print(list(mp))

# my_func = lambda x: x + 10
# print(my_func(x=42))
# print(type(my_func))
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# res = map(lambda x: x + 10, my_numbers)
# print(list(res))
#
# def get_multiplier_v1(n):
#     if n == 2:
#         def multiplier(x):
#             return x * 2
#
#     elif n == 3:
#         def multiplier(x):
#             return x * 3
#
#     else:
#         raise Exception('Я могу сделать умножения только на 2 или на 3')
#
#     return multiplier
#
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# by_2 = get_multiplier_v1(2)
# by_3 = get_multiplier_v1(3)
#
# result = map(by_2, my_numbers)
# print(list(result))
# result = map(by_3, my_numbers)
# print(list(result))





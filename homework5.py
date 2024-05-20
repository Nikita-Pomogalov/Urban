my_list = ['apple', 'banana', 'qiwi', 'pineapple', 'peach']
print('List: ' + str(my_list))
print('First element: ' + my_list[0])
print('Last element: ' + my_list[-1])
sublist = my_list[2:4]
print('Sublist: ' + str(sublist))
my_list[2] = 'orange'
print('Modified list: ' + str(my_list))
print(' ')

my_dict = {'apple': 'яблоко', 'banana': 'банан', 'qiwi': 'киви', 'pineapple': 'ананас', 'peach': 'персик'}
print('Dictionary: ' + str(my_dict))
print('Translation: ' + str(my_dict['apple']))
my_dict['banana'] = 'уже не банан' # Изменение значения для ключа
my_dict['pear'] = 'груша' # Добавление нового ключа
print('Modified dictionary: ' + str(my_dict))


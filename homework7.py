print('Словари')

my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(my_dict)
print('Existing value: ' + str(my_dict.get('Masha')))
print('Not existing value: ' + str(my_dict.get('Igor')))
my_dict['Kamila'] = 1981
my_dict['Artem'] = 1915
print('Deleted value: ' + str(my_dict.pop('Egor')))
print('Modified dictionary:', my_dict)

print('Множества')

my_set = {1, 'Яблоко', 42.314, 1, 'Яблоко'}
print('Set:', my_set)
my_set.add(13)
my_set.add((5, 6, 1.6))
my_set.remove(1)
print('Modified set:', my_set)
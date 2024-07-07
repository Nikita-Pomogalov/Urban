first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(f) - len(s) for f,s in zip(first, second) if len(f) != len(s))

second_result = (True if len(first[i]) == len(second[i]) else False for i in range(len(first)) if len(first) == len(second))

print(list(first_result))
print(list(second_result))
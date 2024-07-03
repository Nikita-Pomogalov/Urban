def custom_write(file_name, strings):
    string_positions = {}
    with open(file_name, 'w', encoding='utf8') as file:
        list = 1
        for i in strings:
            start = file.tell()
            file.write(i + '\n')
            string_positions[(list, start)] = i
            list += 1
        return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

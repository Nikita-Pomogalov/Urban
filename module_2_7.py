def get_multiplied_digits(number):
    if number == 0:
        number = 1
        str_number = str(number)
        first = int(str_number[0])
        if len(str_number) == 1:
            return first
        else:
            return first * get_multiplied_digits(int(str_number[1:]))
    else:
        str_number = str(number)
        first = int(str_number[0])
        if len(str_number) == 1:
            return first
        else:
            return first * get_multiplied_digits(int(str_number[1:]))


print(get_multiplied_digits(int(input("Введите число: "))))



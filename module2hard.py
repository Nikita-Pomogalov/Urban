import random
counts_1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
counts_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
counts_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
password = []

number_1 = random.choice(counts_1)

check = set()

for i in counts_2:
    for j in counts_3:
        x = i + j
        pair = (i, j)
        reverse_pair = (j, i)
        if x >= 3:
            if i == j:
                continue
            elif number_1 % x == 0 and pair not in check and reverse_pair not in check:
                password.append(i)
                password.append(j)
                check.add(pair)


print(number_1, ' - ', *password, sep='')


from statistics import mean


grades =  [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_dict = sorted(list(students)) # Делаем из множества список и сортируем его по алфавиту
grades_new = [] # Будущий новый список средних арифметических
average_rating = {} # Будущий итоговый список
num = 0
count = 0
for i in grades:
    counts = grades[count] # вытаскивает список чисел из большого списка
    counts = mean(counts) # С помощью функции mean() находим среднее арифметическое списка чисел, который является
                          # элементом списка
    grades_new.append(counts) # Добавляем полученное значение в новый список средних арифметических
    count += 1
for i in students_dict:
    average_rating[students_dict[num]] = grades_new[num].__float__() # Берём из полученного сортированного списка имён
                                                                     # значение и этому значению даём первое значение из
                                                                     # списка средних арифметических
    num += 1
print(average_rating)

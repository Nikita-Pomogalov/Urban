import numpy as np
import matplotlib.pyplot as plt

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(a)
print(a[a < 5]) # Все знаемния массива меньше 5
print(a.ndim)  # Размер массива
print(a.size) # общее кол-во элементов

b = np.arange(2, 9, 2) # Массив с дипозоном равномерно расположенных интервалов (От 2 до 9 с шагом 2)
print(b)

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
print(sum(arr), '- Сумма всех чисел массива')
print(arr * 2, '- умножение всех элементов массива на 2')

print(np.sort(arr)) # Сортировка по возрастанию

data = np.array([1, 2])
ones = np.ones(2, dtype=int)
print(data + ones) # Cложение, также можно и с другими вычислениями

print(data - ones)
print(data * data)


fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
plt.show()                           # Show the figure.

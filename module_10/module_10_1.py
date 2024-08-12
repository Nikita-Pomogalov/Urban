from time import sleep
import requests
from datetime import datetime
from threading import Thread

time_start = datetime.now()


def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            if i == word_count:
                print(f'Завершилась запись в файл {file_name}')
                f.write(f'Какое-то слово №{i}\n')
            else:
                f.write(f'Какое-то слово №{i}\n')
                sleep(0.1)

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

time_end = datetime.now()
time_res = time_end - time_start

time_start_2 = datetime.now()


thr_1 = Thread(target=wite_words(10, 'example5.txt'))
thr_2 = Thread(target=wite_words(30, 'example6.txt'))
thr_3 = Thread(target=wite_words(200, 'example7.txt'))
thr_4 = Thread(target=wite_words(10, 'example8.txt'))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

time_end_2 = datetime.now()
time_res_2 = time_end_2 - time_start_2

print(time_res)
print(time_res_2)





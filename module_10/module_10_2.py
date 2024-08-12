from threading import Thread
from time import sleep


class Knight(Thread):
    enemies = 100

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        for i in range(1, self.enemies // self.power + 1):
            if self.enemies <= self.power:
                self.enemies -= self.power
                print(f'{self.name} одржал победу спустя {i} дней(дня)!')
            else:
                self.enemies -= self.power
                print(f'{self.name} сражается {i} день(дня), осталось {self.enemies} воинов')
                sleep(1)

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')







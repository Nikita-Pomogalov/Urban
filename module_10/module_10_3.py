import time
from random import randint
from time import sleep
from threading import Thread, Lock


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            rand = randint(50, 500)
            self.balance += rand
            print(f'Пополнение: {rand}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for _ in range(100):
            rand = randint(50, 500)
            print(f'Запрос на {rand}')
            if rand <= self.balance:
                self.balance -= rand
                print(f'Снятие: {rand}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён. Недостаточно средств')
                self.lock.locked()
            sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk, ))
th2 = Thread(target=Bank.take, args=(bk, ))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')




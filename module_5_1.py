
class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, start, new_floor):
        if start > new_floor:
            print('Ошибка')

        while start <= new_floor:
            if start < 1:
                print('Ошибка')
                break
            print(start)
            start += 1
            if start > self.number_of_floors:
                print(f'Такого этажа не существует в {self.name}')
                break


h1 = House('ЖК Горский', 18)
h2 = House("Домик в деревне", 2)
h1.go_to(1, 5)


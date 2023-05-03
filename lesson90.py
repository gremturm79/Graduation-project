import random


class Cats:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        if self.name == 'no name' and self.age == '0':
            print(f'Родилось {count} котят')
            print(f'{Cats.__name__} Имя: {self.name}, Возраст: {self.age} года, Пол: {self.sex}')
        elif self.sex == 'F':
            print(f'{self.name} is good girl!')
        elif self.sex == 'M':
            print(f'{self.name} is good boy!')

    def print_info(self):
        print(f'{self.name}, {self.age}, {self.sex}')

    def __getitem__(self, item):
        return self.sex

    def __setitem__(self, key, values):
        self.sex = values

    def __add__(self, other):
        if not isinstance(other, Cats):
            raise ArithmeticError('Правый операнд должен быть Cats')
        else:
            global count
            lst = ['F', 'M']
            self.name = 'no name'
            self.age = '0'
            count = random.randint(0, 6)
            if count == 0:
                print(f'Котята ещё не родились')
            for i in range(count):
                a = random.randint(0, 1)
                self.sex = lst[a]
                Cats(self.name, self.age, self.sex)


cat = Cats('Poly', '2', 'F')
cat1 = Cats('Tom', '3', 'M')
cat2 = cat + cat1


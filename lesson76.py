class Account:
    '''
    Класс Account предназначен для ведения счёта прихода и расхода средств, имеет методы: открытия счёта,
    отображения текущего счёта, вывода средств, пополнения счёта, начисления процентов, перевода рублей в доллары,
    перевода рублей в евро, закрытия счёта.
    '''
    rate_usd = 0.013
    rate_eur = 0.011
    suffix_usd = 'USD'
    suffix_eur = 'EUR'
    suffix = 'RUB'

    def __init__(self, num, surname, percent, value=0):
        self.__num = num
        self.__surname = surname
        self.__percent = percent
        self.__value = value
        print(f'Счёт #{self.__num} принадлежащий {self.__surname} был открыт.')
        print('*' * 44)

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    @property
    def num(self):  # метод возвращает значение счёта
        return self.__num

    @num.setter
    def num(self, num):  # метод устанавливает значение счёта и делает проверку значения на тип данных str и isdigit
        if isinstance(num, str) and num.isdigit():
            self.__num = num
        else:
            raise TypeError('номер счёта должен иметь тип данных str и состоять из чисел')

    @num.deleter
    def num(self): # метод удаляет значение счёта
        print('*' * 44)
        print(f'Счёт с #{self.__num} принадлежащий {self.__surname} был закрыт.')
        del self.__num

    @property
    def surname(self): # метод возвращает имя владельца счёта
        return self.__surname

    @surname.setter
    def surname(self, surname): # метод устанавливает имя владельца счёта
        if isinstance(surname, str) and surname.isalpha():
            self.__surname = surname
        else:
            raise TypeError('Имя владельца не должно содержать цифр')

    @property
    def percent(self):  # метод возвращает значение процента
        return self.__percent

    @percent.setter
    def percent(self, percent):  # метод устанавливает значение процента и проверяет значения на тип данных float и str
        if isinstance(percent, float) and not isinstance(percent, str):
            self.__percent = percent
        else:
            raise TypeError('проценты должны быть вещественным числом и не быть строкой')

    @property
    def value(self):  # возврат значения текущего счёта
        return self.__value

    @value.setter
    def value(self, val):  # установка значения баланса с проверкой является ли значение целым числом
        try:
            val = int(val)
            if isinstance(val, int):
                self.__value += val
                print(f'{val} {Account.suffix} было успешно добавлено')
                self.print_balance()
            else:
                raise TypeError('значение баланса должно быть целым числом')
        except:
            print('значение не является числом')
        finally:
            print('не число')

    def add_percents(self):
        self.__value += self.__value * self.__percent
        print(f'Проценты были успешно начислены !')
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.__value:
            print(f'К сожалению у вас нет {val} {Account.suffix}')
        else:
            self.__value -= val
            print(f'{val} {Account.suffix} было успешно снято')
        self.print_balance()

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f'Состояние счёта {usd_val} {Account.suffix_usd}')

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f'Состояние счёта {eur_val} {Account.suffix_eur}')

    def print_balance(self):
        print(f'Текущий баланс {self.value} {Account.suffix}')

    def print_info(self):
        print(f'Информация о счёте')
        print('-' * 25)
        print(f'#{self.num}')
        print(f'Владелец: {self.surname}')
        self.print_balance()
        print(f'Проценты {self.percent: .0%}')
        print('-' * 25)


acc = Account('12345', 'Долгих', 0.03, 1000)
acc.print_balance()
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()

Account.set_usd_rate(2)
acc.convert_to_usd()

Account.set_eur_rate(3)
acc.convert_to_eur()
print()
# acc.surname = 'Дюма' # смена имени пользователя счёта
# acc.num = '11122' # смена номера счёта через декоратор
# acc.percent = 0.15 # смена процентной ставки при помощи декоратора
acc.print_info()  # вывод информации о счёте
# acc.value = 5000 # добавление средств на счёт при помощи декоратора
print()
acc.add_percents()
print()
acc.withdraw_money(3000)
print()
acc.withdraw_money(100)
print()
# acc.add_money(5000)

print()
acc.withdraw_money(3000)
acc.print_info()
del acc.num



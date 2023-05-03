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

    def __del__(self):
        print('*' * 44)
        print(f'Счёт с #{self.__num} принадлежащий {self.__surname} был закрыт.')

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def get_num(self):  # метод возвращает номер счёта
        print(self.__num)

    def set_num(self, num):  # метод устанавливает номер счёта
        self.__num = num
        return self.__num

    def get_surname(self):  # метод возвращает имя владельца
        print(self.__surname)

    def set_surname(self, surname):  # метод устанавливает имя владельца
        self.__surname = surname

    def get_percent(self):  # метод возвращает значение процента счёта
        print(self.__percent)

    def set_percent(self, percent):
        self.__percent = percent  # метод устанавливает процент счёта

    def get_value(self):  # метод возвращает баланс счёта
        print(self.__value)

    def set_value(self, value):  # метод устанавливает баланс счёта
        self.__value = value

    def add_percents(self):
        self.__value += self.__value * self.__percent
        print(f'Проценты были успешно начислены !')
        self.print_balance()

    def edit_owner(self, surname):
        self.__surname = surname

    def withdraw_money(self, val):
        if val > self.__value:
            print(f'К сожалению у вас нет {val} {Account.suffix}')
        else:
            self.__value -= val
            print(f'{val} {Account.suffix} было успешно снято')
        self.print_balance()

    def add_money(self, val):
        self.__value += val
        print(f'{val} {Account.suffix} было успешно добавлено')
        self.print_balance()

    def convert_to_usd(self):
        usd_val = Account.convert(self.__value, Account.rate_usd)
        print(f'Состояние счёта {usd_val} {Account.suffix_usd}')

    def convert_to_eur(self):
        eur_val = Account.convert(self.__value, Account.rate_eur)
        print(f'Состояние счёта {eur_val} {Account.suffix_eur}')

    def print_balance(self):
        print(f'Текущий баланс {self.__value} {Account.suffix}')

    def print_info(self):
        print(f'Информация о счёте')
        print('-' * 25)
        print(f'#{self.__num}')
        print(f'Владелец: {self.__surname}')
        self.print_balance()
        print(f'Проценты {self.__percent: .0%}')
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
acc.edit_owner('Дюма')
# acc.set_num(7896)
# acc.set_surname('Иванов')
# acc.set_percent(0.05)
# acc.set_value(10000)
acc.print_info()
print()
acc.add_percents()
print()
acc.withdraw_money(3000)
print()
acc.withdraw_money(100)
print()
acc.add_money(5000)
print()
acc.withdraw_money(3000)
print()
print()
acc.get_num()

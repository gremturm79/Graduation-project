class Books:
    '''
    Класс Books устанавливает: название книги, год выпуска, тираж, жанр книги, автора, цену книги
    '''
    title = 'title'
    year = 'year'
    circulation = 'circulation'
    genre = 'genre'
    author = 'author'
    price = 'price'

    def books_fields(self, title, year, circulation, genre, author, price): # функция для установки свойств экземпляра
        # класса, и отображения в консоли
        self.title = title
        self.year = year
        self.circulation = circulation
        self.genre = genre
        self.author = author
        self.price = price
        print('Книжный магазин'.center(41, '-'))
        print('Название книги:'.ljust(20, ' '), title.rjust(20, ' '))
        print('Год выпуска:'.ljust(20, ' '), year.rjust(20, ' '))
        print('Название издателя:'.ljust(20, ' '), circulation.rjust(20, ' '))
        print('Жанр:'.ljust(20, ' '), genre.rjust(20, ' '))
        print('Автор:'.ljust(20, ' '), author.rjust(20, ' '))
        print('Цена:'.ljust(20, ' '), price.rjust(20, ' '))
        print('=' * 41)

    def set_title(self, title):  # установить название книги
        self.title = title

    def get_title(self):  # получить название книги
        return self.title

    def set_year(self, year):  # установить год выпуска
        self.year = year

    def get_year(self):  # получить год выпуска
        return self.year

    def set_circulation(self, circulation):  # установить тираж книги
        self.circulation = circulation

    def get_circulation(self):  # получить тираж книги
        return self.circulation

    def set_genre(self, genre):  # установить жанр книги
        self.genre = genre

    def get_genre(self):  # получить жанр книги
        return self.genre

    def set_author(self, author): # установить автора книги
        self.author = author

    def get_author(self):  # получить автора книги
        return self.author

    def set_price(self, price):  # установить цену книги
        self.price = price

    def get_price(self):  # получить цену книги
        return self.price


p1 = Books()
p1.books_fields('Python для чайников', '2019', '500', 'Образование', 'Мюллер Джон Пол', '1200 рублей')

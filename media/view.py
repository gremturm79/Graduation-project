def add_title(title):  # декоратор для методов класса UserInterface
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f'{title}'.center(50, '='))
            output = func(*args, **kwargs)
            print('=' * 50)
            return output

        return wrap

    return wrapper


class UserInterface:

    @add_title('Ввод пользовательских данных')
    def wait_user_answer(self):  # метод вывода информации для пользователя по функциональности приложения и вывод
        # пользовательского ввода

        print('Действия с фильмами:')
        print('1 - добавление фильма''\n2 - каталог фильмов''\n3 - просмотр определённого фильма'
              '\n4 - удаление фильма''\nq - выход из программы')
        user_answer = input('Выберите вариант действия: ')
        return user_answer

    @add_title('Создание фильма:')
    def add_user_film(self):  # метод записи пользователем всех данных фильма, тип данных dict()
        dict_film = {
            'название': None,
            'жанр': None,
            'режиссёр': None,
            'год': None,
            'продолжительность': None
        }
        for key in dict_film:
            dict_film[key] = input(f'Введите {key} фильма: ')
        return dict_film

    @add_title('Список фильмов')
    def show_all_films(self, films):  # метод вывода информации всех существующих фильмов
        for ind, films in enumerate(films, 1):
            print(f'{ind}. {films}')

    @add_title('Ввод названия фильма:')
    def get_user_film(self):  # метод ввода фильма пользователем для последующей передачи
        # значения в метод get_single_film
        user_film = input('Введите название фильма: ')
        return user_film

    @add_title('Просмотр фильма:')
    def show_single_film(self, film):  # метод просмотра данных о фильме
        for key in film:
            print(f'{key} фильма - {film[key]}')

    @add_title('Сообщение об ошибке:')  # метод вывода информации при отсутствии фильма
    def show_incorrect_name_error(self, user_film):
        print(f'Фильма с названием {user_film} не существует')

    @add_title('Удаление фильма')
    def remove_single_film(self, film):  # вывод информации об удалении информации
        print(f'Фильм {film} - был удалён')

    @add_title('Сообщение об ошибке:')
    def show_incorrect_answer_error(self, answer):  # метод сообщает об ошибке при отсутствии такой командной строки
        print(f'Варианта {answer} - не существует')

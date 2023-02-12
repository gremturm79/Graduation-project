def add_title(method):  # аргументом является метод класса
    if method.__name__ == 'wait_user_answer':
        def wrap(self):  # аргументом является экземпляр класса
            print(' Ввод пользовательских данных '.center(50, '='))
            res = method(self)
            print('=' * 50)
            return res

        return wrap
    elif method.__name__ == 'add_user_article':
        def wrap(self):  # аргументом является экземпляр класса
            print(' Создание статьи '.center(50, '='))
            res = method(self)
            print('=' * 50)
            return res

        return wrap
    elif method.__name__ == 'show_all_articles':
        def wrap(self, articles):  # аргументом является экземпляр класса
            print(' Список статей: '.center(50, '='))
            res = method(self, articles)
            print('=' * 50)
            return res

        return wrap


class UserInterface:

    @add_title
    def wait_user_answer(self):
        # print(' Ввод пользовательских данных '.center(50, '='))
        print('Действия со статьями:')
        print('1 - создание статьи''\n2 - просмотр статей''\nq - выход из программы')
        user_answer = input('Выберите вариант действия: ')
        # print('=' * 50)
        return user_answer

    @add_title
    def add_user_article(self):
        dict_article = {
            'название': None,
            'автор': None,
            'количество страниц': None,
            'описание': None
        }
        # print(' Создание статьи '.center(50, '='))
        for key in dict_article:
            dict_article[key] = input(f'Введите {key} статьи: ')
        # print('=' * 50)
        return dict_article

    @add_title
    def show_all_articles(self, articles):
        # print(' Список статей: '.center(50, '='))
        for ind, articles in enumerate(articles, 1):
            print(f'{ind}. {articles}')
        # print('=' * 50)

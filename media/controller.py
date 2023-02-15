from view import UserInterface
from model import MediaModel


class Controller:
    '''
    Класс Controller переопределяет потоки данных в запросах пользователя при вводе команд приложения media
    '''
    def __init__(self):
        self.user_interface = UserInterface()  # объект модуля view класса UserInterface
        self.media_model = MediaModel()  # объект модуля model класса MediaModel

    def run(self):
        answer = None
        while answer != 'q':
            answer = self.user_interface.wait_user_answer()  # получения данных с пользовательского ввода
            self.check_user_answer(answer)  # метод проверки команды введённой пользователем для дальнейшей обработки
            # этой команды, по условиям созданных в этом методе, answer аргумент полученный от пользователя

    def check_user_answer(self, answer):
        '''
        Метод check_user_answer контролирует вызовы команд введённых пользователем.
        :param answer: аргумент полученный от пользователя.
        :return: Возвращает ожидаемый результат пользователю при его запросе
        (в зависимости от аргумента определяет маршрут вызова функций классов из импортированных модулей)
        '''
        if answer == '1':
            film = self.user_interface.add_user_film()
            self.media_model.add_film(film)
        elif answer == '2':
            films = self.media_model.get_all_films()
            self.user_interface.show_all_films(films)
        elif answer == '3':
            media_film = self.user_interface.get_user_film()  # запрос названия фильма, для получения информации о нём
            try:
                film = self.media_model.get_single_film(media_film)  # получение данных фильма
            except KeyError:
                self.user_interface.show_incorrect_name_error(media_film)
            else:
                self.user_interface.show_single_film(film)
        elif answer == '4':
            film_name = self.user_interface.get_user_film() # запрос названия фильма, для получения информации о нём
            try:
                film = self.media_model.remove_film(film_name)  # удаление данных фильма
            except KeyError:
                self.user_interface.show_incorrect_name_error(film_name)
            else:
                self.user_interface.remove_single_film(film)

        elif answer == 'q':
            self.media_model.save_data()  # метод сохранения данных
        else:
            self.user_interface.show_incorrect_answer_error(answer)

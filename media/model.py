import pickle
import os


class Media:
    '''
    Класс Media инициализирует полученные аргументы для дальнейшего использования их как значения словаря в
    классе MediaModel
    '''
    def __init__(self, film, genre, director, year, time):
        self.film = film
        self.genre = genre
        self.director = director
        self.year = year
        self.time = time

    def __str__(self):
        return f'{self.film} ({self.genre})'


class MediaModel:
    '''
    Класс MediaModel определяет работу с данными приложения media при помощи своих методов: add_film, get_all_films,
    get_single_film,
    remove_film, load_data, save_data.
    '''
    def __init__(self):
        self.db_name = 'db.txt'
        self.medias = self.load_data()

    def add_film(self, dict_media):  # метод записи данных полученных из метода add_user_film
        media = Media(*dict_media.values())  # объект в котором содержатся значения экземпляра класса
        self.medias[media.film] = media

    def get_all_films(self):  # метод получения данных всех существующих фильмов при запросе №2
        return self.medias.values()

    def get_single_film(self, user_film):  # метод возвращает данные фильма по запросу №3 в метод show_single_film
        media = self.medias[user_film]
        dict_medias = {
            'название': media.film,
            'жанр': media.genre,
            'режиссёр': media.director,
            'год': media.year,
            'длительность': media.time
        }
        return dict_medias

    def remove_film(self, user_film):  # метод удаления данных по запросу №4
        return self.medias.pop(user_film)

    def load_data(self):  # метод открытия файла базы данных при его существование, а иначе возвращения словаря
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):  # метод сохранения данных при закрытии программы, запись в текстовый файл
        with open(self.db_name, 'wb') as f:
            pickle.dump(self.medias, f)

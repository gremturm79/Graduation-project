import json
import string
import random


def get_person():
    name = string.ascii_lowercase  # перечисление букв из набора ASCII в нижнем регистре
    rand_string = ''.join(random.choices(name, k=8))
    nums = string.digits  # перечисление цифр из набора цифр ASCII
    rand_nums = ''.join(random.choices(nums, k=10))

    person = {
        'name': rand_string,
        'tel': rand_nums
    }
    return person


def write_json(person_dict):
    '''
    Функция создание файла json
    :param person_dict: принимает аргумент типа данных словарь
    :return: возвращает json файл
    '''
    keys_string = string.ascii_lowercase
    rand_keys = ''.join(random.choices(keys_string, k=8))
    try:
        data = json.load(open('person.json'))
    except FileNotFoundError:
        data = dict()  # создаём словарь
    for i in range(5):
        data[rand_keys] = person_dict  # добавление в словарь вложенных данных типа dict полученных из get_person()
    with open('person.json', 'w') as file:  # создание файла и запись
        json.dump(data, file, indent=2)  # кодирование файла в формат json


for i in range(5):
    write_json(get_person())

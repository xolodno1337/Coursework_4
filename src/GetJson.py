import json
from src.AbstractJson import AbstractJson


class GetJson(AbstractJson):
    """ Класс для сохранения информации о вакансиях в JSON-файл. """

    def __str__(self):
        """ Представление класса GetJson для пользователей. """
        return 'Класс для сохранения информации о вакансиях в JSON-файл.'

    def save_vacancy(self, data):
        """ Сохранение вакансий в файле. """
        with open('vacancy.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def read_vacancy(self):
        """ Чтение файла с вакансиями. """
        with open('vacancy.json', encoding='utf-8') as file:
            return json.load(file)

    def delete_vacancy(self):
        """ Удаление информации о вакансиях. """
        with open('vacancy.json', 'w', encoding='utf-8') as file:
            json.dump([], file, indent=4, ensure_ascii=False)

import requests
from src.AbstractAPI import AbstractApi


class GetAPI(AbstractApi):
    """ Класс для работы с API сервиса с вакансиями. """

    def __init__(self, name_vacancy):
        self.all_vacancy = {}
        self.url_get = 'https://api.hh.ru/vacancies/'
        self.data = {'text': name_vacancy, 'page': 1, 'only_with_salary': 'true'}

    def __str__(self):
        """ Представление класса GetAPI для пользователей. """
        return 'Класс для работы с API сервиса с вакансиями.'

    def get_vacancy(self):
        """ Подключение к API сервису с вакансиями. """
        response = requests.get(self.url_get, params=self.data, headers={'Content-Type': 'application/json; '
                                                                                         'charset=utf-8'})
        return response.json()

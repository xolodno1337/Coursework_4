import json

import pytest
import requests
from requests import Response

from src.GetApi import GetAPI
from src.GetJson import GetJson


def test_get_vacancy():
    """ Тест на подключение к API сервису с вакансиями. """
    url_get = 'https://api.hh.ru/vacancies/'
    response = requests.get(url_get)
    if isinstance(response, dict):
        raise TypeError


def test_comparison_pay():
    """ Тест сравнения зарплат."""
    pass


def test_save_vacancy():
    """ Тест сохранения вакансий в файле. """
    pass


def test_read_vacancy():
    """ Тест на чтение файла с вакансиями."""
    pass


def test_delete_vacancy():
    """ Тест удаления информации о вакансии. """
    pass

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

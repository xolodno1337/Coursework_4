import requests
import pytest
from src.Vacancy import Vacancy


def test_get_vacancy():
    """ Тест на подключение к API сервису с вакансиями. """
    url_get = 'https://api.hh.ru/vacancies/'
    response = requests.get(url_get)
    if isinstance(response, dict):
        raise TypeError


@pytest.fixture
def vacancy_python():
    return Vacancy('Python разработчик (Middle)',
                   'https://api.hh.ru/vacancies/97164750?host=hh.ru',
                   'Опыт в работе со следующим стеком: <highlighttext>Python</highlighttext>3 (3.6-3.9, от '
                   'проекта к проекту). PostgreSQL как основная БД.',
                   'Поддержка и развитие текущих проектов компании. Разработка новых проектов.'
                   ' Проектирование архитектуры и самостоятельность в принятии технических решений.',
                   'От 1 года до 3 лет',
                   'Полная занятость',
                   80000, 200000)


def test_init(vacancy_python):
    """ Тест на инициализацию класса Vacancy. """
    assert vacancy_python.name == 'Python разработчик (Middle)'
    assert vacancy_python.url_job == 'https://api.hh.ru/vacancies/97164750?host=hh.ru'
    assert vacancy_python.requirement == ('Опыт в работе со следующим стеком: <highlighttext>Python</highlighttext>3'
                                          ' (3.6-3.9, от проекта к проекту). PostgreSQL как основная БД.')
    assert vacancy_python.description == ('Поддержка и развитие текущих проектов компании. Разработка новых проектов. '
                                          'Проектирование архитектуры и самостоятельность в принятии технических решений.')
    assert vacancy_python.experience == 'От 1 года до 3 лет'
    assert vacancy_python.work_schedule == 'Полная занятость'
    assert vacancy_python.pay_from == 80000
    assert vacancy_python.pay_to == 200000

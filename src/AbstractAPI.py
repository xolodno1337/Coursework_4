from abc import ABC, abstractmethod


class AbstractApi(ABC):
    """ Абстрактный класс для работы с API сервиса с вакансиями. """

    @abstractmethod
    def __str__(self):
        """ Представление класса для пользователей. """
        pass

    @abstractmethod
    def get_vacancy(self):
        """ Подключение к API сервису с вакансиями. """
        pass

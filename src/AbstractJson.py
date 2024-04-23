from abc import ABC, abstractmethod


class AbstractJson(ABC):
    """Абстрактный класс для добавления и получения данных из файла. """

    @abstractmethod
    def __str__(self):
        """ Представление класса GetJson для пользователей. """
        pass

    @abstractmethod
    def save_vacancy(self, data):
        """ Сохранение вакансий в файле. """
        pass

    @abstractmethod
    def read_vacancy(self):
        """ Чтение файла с вакансиями. """
        pass

    @abstractmethod
    def delete_vacancy(self):
        """ Удаление информации о вакансиях. """
        pass

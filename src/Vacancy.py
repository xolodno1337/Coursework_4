class Vacancy:
    """ Класс для работы с вакансиями. """
    name: str   # Название вакансии
    url_job: str    # Ссылка на вакансию
    requirement: str   # Необходимые навыки
    description: str   # Описание вакансии
    experience: str   # Опыт работы
    work_schedule: str   # График работы
    pay_from: int   # Зарплата от
    pay_to: int   # Зарплата до

    def __init__(self, name, url_job, requirement, description, experience, work_schedule, pay_from, pay_to):
        self.name = name
        self.url_job = url_job
        self.requirement = requirement
        self.description = description
        self.experience = experience
        self.work_schedule = work_schedule
        self.pay_from = pay_from
        self.pay_to = pay_to

    def __repr__(self):
        """ Представление класса Vacancy. """
        return f"""
        Название вакансии: {self.name}
        Ссылка на вакансию: {self.url_job}
        Необходимые навыки: {self.requirement}
        Обязанности: {self.description}
        Опыт работы: {self.experience}
        График работы: {self.work_schedule}
        Зарплата: {self.pay_from} - {self.pay_to}
        """

    def __gt__(self, other):
        """ Метод сравнения зарплат. """
        if not isinstance(other.pay_to, int) or not isinstance(self.pay_to, int):
            return self.pay_from > other.pay_from
        return self.pay_to > other.pay_to

    def __lt__(self, other):
        """ Метод сравнения зарплат. """
        if not isinstance(other.pay_to, int) or not isinstance(self.pay_to, int):
            return self.pay_from < other.pay_from
        else:
            return self.pay_to < other.pay_to

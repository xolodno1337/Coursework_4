class Vacancy:
    """ Класс для работы с вакансиями. """
    name: str   # Название вакансии
    url_job: str    # Ссылка на вакансию
    description: str   # Описание вакансии
    experience: str   # Опыт работы
    work_schedule: str   # График работы
    pay: float   # Зарплата

    def __init__(self, name, url_job, description, experience, work_schedule, pay):
        self.name = name
        self.url_job = url_job
        self.description = description
        self.experience = experience
        self.work_schedule = work_schedule
        self.pay = pay


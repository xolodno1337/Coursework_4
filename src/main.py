from src.GetApi import GetAPI
from src.GetJson import GetJson


def user_interaction():
    """Функция для взаимодействия с пользователем """
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")   # Пример: 100000 - 150000
    vacancy = GetAPI(search_query)
    vacancy_json = GetJson()
    vacancy_json.save_vacancy(vacancy.get_vacancy())

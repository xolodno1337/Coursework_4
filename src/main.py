from src.GetApi import GetAPI
from src.GetJson import GetJson
from src.Vacancy import Vacancy
from src.func import filter_word, sorted_salary, get_top


def user_interaction():
    """Функция для взаимодействия с пользователем. """
    platforms = ['HeadHunter']
    search_query = input('Введите поисковый запрос: ').title()
    filter_words = input('Введите ключевые слова для фильтрации вакансий: ').title().split()

    vacancy = GetAPI(search_query)
    vacancy_json = GetJson()
    vacancy_json.save_vacancy(vacancy.get_vacancy())
    list_vacancy = [
        Vacancy(
            name=i['name'],
            url_job=i['url'],
            requirement=i['snippet']['requirement'] if i['snippet']['requirement'] else 'Нет описания',
            description=i['snippet']['responsibility'] if i['snippet']['responsibility'] else 'Нет описания',
            experience=i['experience']['name'],
            work_schedule=i['employment']['name'],
            pay_from=i['salary']['from'] if i['salary']['from'] else i['salary']['to'],
            pay_to=i['salary']['to'] if i['salary']['to'] else i['salary']['from'])
        for i in vacancy_json.read_vacancy()['items']]

    f_vacancy = filter_word(filter_words, list_vacancy)
    while True:
        command = input('Введите команду 1 для сортировки по зарплате, 2 - для вывода количество вакансий в топ N,'
                        ' 3 - для изменения вакансии, 0 - для выхода их программы: ')
        if command == '1':
            salary_range = list(map(int, input('Введите диапазон зарплат, пример: 100000 - 150000: ').split('-')))
            i = sorted_salary(salary_range, f_vacancy)
            continue
        elif command == '2':
            top_n = int(input('Введите количество вакансий для вывода в топ N: '))
            v = get_top(top_n, f_vacancy)
            continue
        elif command == '3':
            user_interaction()
        elif command == '0':
            print('Надеемся нашли, что искали')
        break


user_interaction()

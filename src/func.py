def filter_word(filter_words, list_vacancy):
    """Функция фильтрации вакансий по ключевому слову. """
    filter_vacancy = set()
    for i in filter_words:
        for v in list_vacancy:
            if v.description and (i in v.name or v.description or v.requirement):
                filter_vacancy.add(v)
    return filter_vacancy


def sorted_salary(salary_range, f_vacancy):
    """ Функция сортировки по зарплате. """
    for item in f_vacancy:
        if salary_range[0] < item.pay_to < salary_range[1]:
            print(item)


def get_top(top_n, f_vacancy):
    """ Функция по сортировке необходимого кол-ва вакансий. """
    for vacancy in list(sorted(f_vacancy, reverse=True))[:top_n]:
        print(vacancy)

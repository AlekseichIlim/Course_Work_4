from src.HH_API import HeadHunterAPI
from src.Vacancies import Vacancy
from src.SaveJSON import JSONSaver


def filter_vacancies(vacancies_list, words):
    """
    Возвращает список вакансий с ключевыми словами в описании
    """

    filtered_list = []
    for vacancy in vacancies_list:
        for word in words:
            if word.lower() in vacancy.name.lower():
                filtered_list.append(vacancy)
    if len(filtered_list) != 0:
        return filtered_list
    else:
        print('По данным ключевым словам вакансий не найдено.')


def get_vacancies_by_salary(filtered_vacancies, salary_from_to):
    """
    Возвращает список вакансий, зарплата которых, попала в требуемый диапазон
    """

    filtered_list = []
    range_salary = salary_from_to.split(' - ')
    for vacancy in filtered_vacancies:
        if int(range_salary[0]) <= vacancy.salary <= int(range_salary[1]):
            filtered_list.append(vacancy)
    return filtered_list


def sort_vacancies(vacancies):
    """
    Сортирует вакансии по зарплате(вакансия с самой большой зарплатой выводится первой)
    """

    sort_list = sorted(vacancies, reverse=True)
    return sort_list


def get_top_vacancies(vacancies, count):
    """
    Оставляет необходимое количество вакансий
    """

    top_list = vacancies[0:count]
    return top_list


def print_vacancies(vacancies):
    """
    Выводит информацию о вакансиях в соответствии с запросом
    """

    for vacancy in vacancies:
        print(vacancy)


def user_interaction():
    """
    Функция взаимодействия с пользователем
    """
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат(#Пример: 100000 - 150000): ")

    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    json_saver = JSONSaver()
    json_saver.add_vacancy(top_vacancies)

    if top_n > len(sorted_vacancies):
        print(f'\nПо вашему запросу нашлось только {len(sorted_vacancies)} вакансий')

    print_vacancies(top_vacancies)





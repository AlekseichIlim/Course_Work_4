import pytest
import requests
from src.Vacancies import Vacancy


class HeadHunterAPI:
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 1, 'area': 113}
        self.vacancies = []

    def load_vacancies(self, keyword):
        """
        Создает список вакансий в России по запросу
        """
        self.__params['text'] = keyword
        self.__params['currency'] = 'RUR'
        while self.__params.get('page') != 5:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.__params['page'] += 1

    def get_vacancies(self, keyword):
        """
        Возвращает список вакансий
        """
        self.load_vacancies(keyword)
        return self.vacancies


@pytest.fixture
def vacancies_fix():
    tests_API = HeadHunterAPI()
    return tests_API.get_vacancies('Python')


@pytest.fixture
def vacancy_fix_1():
    return Vacancy('Програмист', 'Рашка', 1000, '24/7', 'ya.ru')


@pytest.fixture
def vacancy_fix_2():
    return Vacancy('Програмист', 'Рашка', 0, '24/7', 'ya.ru')


@pytest.fixture
def objects_fix_1(vacancies_fix):
    objects_list = Vacancy.cast_to_object_list(vacancies_fix)
    return objects_list

@pytest.fixture
def objects_fix_2():
    v_1 = Vacancy('Програмист начальный', 'Рашка', 200, '24/7', 'ya.ru')
    v_2 = Vacancy('Програмист стажер', 'Рашка', 100, '24/7', 'ya.ru')
    v_3 = Vacancy('Програмист опытный', 'Рашка', 300, '24/7', 'ya.ru')
    objects_list = [v_1, v_2, v_3]
    return objects_list

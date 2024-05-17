import requests
from abc import ABC, abstractmethod


class Parser(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_vacancies(self):
        pass


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 10, 'area': 113}
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

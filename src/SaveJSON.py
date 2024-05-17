import json
from abc import ABC, abstractmethod


class Save(ABC):

    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class JSONSaver(Save):

    def add_vacancy(self, vacancy):
        """
        Записывает список вакансий в JSON файл
        """
        with open('../data/vacancies.json', 'w', encoding="utf-8") as f:
            json.dump(vacancy, f, ensure_ascii=False)

    def get_data(self):
        """
        Выводит данные о названиях вакансий из файла JSON
        """
        with open('../data/vacancies.json', 'r') as f:
            data = json.load(f)
            for i in data:
                print(i['name'])

    def delete_vacancy(self):
        """
        Удаляет данные о вакансиях
        """
        with open('../data/vacancies.json', 'w') as f:
            f.write('')

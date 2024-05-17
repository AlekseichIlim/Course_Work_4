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
        with open('/home/atshnik/PycharmProjects/Course_Work_4/pythonProject/data/vacancies.json', 'w', encoding="utf-8") as f:
            f.write(json.dumps(vacancy, default=lambda x: x.__dict__, ensure_ascii=False))

    def get_data(self):
        """
        Выводит данные о названиях вакансий из файла JSON
        """
        with open('/home/atshnik/PycharmProjects/Course_Work_4/pythonProject/data/vacancies.json', 'r') as f:
            data = json.load(f)
            if type(data) is dict:
                print(data['name'])
            else:
                for i in data:
                    print(i['name'])

    def delete_vacancy(self):
        """
        Удаляет данные о вакансиях
        """
        with open('/home/atshnik/PycharmProjects/Course_Work_4/pythonProject/data/vacancies.json', 'w') as f:
            f.write('')

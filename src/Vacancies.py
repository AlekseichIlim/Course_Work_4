from abc import ABC, abstractmethod


class BaseVacancy(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Vacancy(BaseVacancy):
    """
    Клacc для создания объекта вакансии
    """

    def __init__(self, name, area, salary, schedule, url):
        super().__init__()
        self.name = name
        self.area = area
        self.verify_salary(salary)
        self.schedule = schedule
        self.url = url

    def __repr__(self):
        return f'{self.__class__.__name__}'

    def __str__(self):
        return f'\nНазвание вакансии: {self.name}\nМесто работы: {self.area}\nЗарплата: {self.salary}\nГрафик: {self.schedule}\nСсылка: {self.url}'

    def __lt__(self, other):
        return self.salary < other.salary

    @classmethod
    def sorted_by_salary(cls, list_vacancies):
        """
        Сортирует список вакансий по зарплате
        """
        vacancies_sort = sorted(list_vacancies)
        return vacancies_sort

    @classmethod
    def cast_to_object_list(cls, list_vacancies):
        """
        Преобразование набора данных из списка вакансий в список объектов класса Vacancy
        """
        object_list = []
        for vacancy in list_vacancies:
            object_list.append(
                cls(vacancy['name'], vacancy['area']['name'], vacancy['salary'], vacancy['schedule']['name'],
                    vacancy['url']))
        return object_list

    def verify_salary(self, salary):
        if salary is not None:
            if not isinstance(salary, int):
                if isinstance(salary, dict):
                    if 'from' and 'to' not in salary:
                        raise KeyError('Аргумент salary должен содержать ключ "from" и "to"')
                    else:
                        if salary['from'] is None:
                            self.__salary = salary['to']
                        else:
                            self.__salary = salary['from']
                else:
                    self.__salary = 0
            else:
                self.__salary = salary
        else:
            self.__salary = 0

    @property
    def salary(self):

        if self.__salary == None:
            self.__salary = 0
        return self.__salary

    @salary.setter
    def salary(self, other):
        self.__salary = other
        return self.__salary

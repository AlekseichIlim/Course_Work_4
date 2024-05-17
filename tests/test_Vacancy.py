import pytest
from src.Vacancies import Vacancy


def test_init(vacancy_fix_1):
    """
    Тестирует __init__
    """
    assert vacancy_fix_1.name == 'Програмист'
    assert vacancy_fix_1.area == 'Рашка'
    assert vacancy_fix_1.salary == 1000
    assert vacancy_fix_1.schedule == '24/7'
    assert vacancy_fix_1.url == 'ya.ru'


def test_str(capsys):
    """
    Тестирует print экземпляра
    """
    test_v = Vacancy('Програмист', 'Рашка', 1000, '24/7', 'ya.ru')
    print(test_v)
    message = capsys.readouterr()
    assert message.out == ('\n'
                           'Название вакансии: Програмист\n'
                           'Место работы: Рашка\n'
                           'Зарплата: 1000\n'
                           'График: 24/7\n'
                           'Ссылка: ya.ru\n')


def test_lt(capsys, vacancy_fix_1, vacancy_fix_2):
    """
    Тестирует метод __lt__
    """
    print(vacancy_fix_1 > vacancy_fix_2)
    message = capsys.readouterr()
    assert message.out == 'True\n'


def test_cast_to_object_1(objects_fix_1):
    """
    Тестирует метод создания списка объектов класса Vacancy
    """
    assert type(objects_fix_1) == list


def test_cast_to_object_2(objects_fix_1):
    """
    Проверяет класс объектов в списке
    """
    for i in objects_fix_1:
        assert type(i) == Vacancy


def test_sorted_by_salary(capsys, objects_fix_2):
    """
    Тестирует метод сортировки экземпляров
    """
    sortted_list = Vacancy.sorted_by_salary(objects_fix_2)
    for i in sortted_list:
        print(i.salary)
    message = capsys.readouterr()
    assert message.out == '100\n200\n300\n'

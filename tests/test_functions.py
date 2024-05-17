import pytest
from src.functions import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies
from src.Vacancies import Vacancy


def test_filter_vacancies(capsys, objects_fix_2):
    filter_vacancies(objects_fix_2, '')
    message = capsys.readouterr()
    assert message.out == 'По данным ключевым словам вакансий не найдено.\n'


def test_get_vacancies_by_salary(objects_fix_2):
    sort_list = get_vacancies_by_salary(objects_fix_2, '100 - 200')
    assert len(sort_list) == 2


def test_sort_vacancies(capsys, objects_fix_2):
    sort_list = sort_vacancies(objects_fix_2)
    for i in sort_list:
        print(i.salary)
    message = capsys.readouterr()
    assert message.out == '300\n200\n100\n'


def test_get_top_vacancies(objects_fix_1):
    sort_list = get_top_vacancies(objects_fix_1, 2)
    assert len(sort_list) == 2


def test_print_vacancies(capsys, objects_fix_2):
    print_vacancies(objects_fix_2)
    message = capsys.readouterr()
    assert message.out == ('\n'
                           'Название вакансии: Програмист начальный\n'
                           'Место работы: Рашка\n'
                           'Зарплата: 200\n'
                           'График: 24/7\n'
                           'Ссылка: ya.ru\n'
                           '\n'
                           'Название вакансии: Програмист стажер\n'
                           'Место работы: Рашка\n'
                           'Зарплата: 100\n'
                           'График: 24/7\n'
                           'Ссылка: ya.ru\n'
                           '\n'
                           'Название вакансии: Програмист опытный\n'
                           'Место работы: Рашка\n'
                           'Зарплата: 300\n'
                           'График: 24/7\n'
                           'Ссылка: ya.ru\n')

import pytest
from src.Vacancies import Vacancy

"""
Тест валидации, геттеров и сеттеров атрибута salary класса Vacancy
"""

vacancy1 = Vacancy('Програмист', 'Рашка', 1000, '24/7', 'ya.ru')
vacancy2 = Vacancy('Програмист', 'Рашка', None, '24/7', 'ya.ru')
vacancy3 = Vacancy('Програмист', 'Рашка', {'to': 100, 'from': 200}, '24/7', 'ya.ru')
vacancy4 = Vacancy('Програмист', 'Рашка', {'to': 100, 'from': None}, '24/7', 'ya.ru')
vacancy5 = Vacancy('Програмист', 'Рашка', {'to': None, 'from': None}, '24/7', 'ya.ru')
vacancy6 = Vacancy('Програмист', 'Рашка', {'to': None, 'from': 200}, '24/7', 'ya.ru')
vacancy7 = Vacancy('Програмист', 'Рашка', '', '24/7', 'ya.ru')


def test_get_salary_1():
    assert vacancy1.salary == 1000
    assert vacancy2.salary == 0
    assert vacancy3.salary == 200
    assert vacancy4.salary == 100
    assert vacancy5.salary == 0
    assert vacancy6.salary == 200
    assert vacancy7.salary == 0


def test_get_salary_keys():
    with pytest.raises(KeyError):
        Vacancy('Програмист', 'Россия', {'от': 100, 'до': 200}, '24/7', 'ya.ru')


def test_set_salary():
    vacancy1.salary = 500
    assert vacancy1.salary == 500


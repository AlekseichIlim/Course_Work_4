import json
from src.SaveJSON import JSONSaver

def test_add_vacancy(capsys, vacancy_fix_1):
    j_saver = JSONSaver()
    j_saver.add_vacancy(vacancy_fix_1)
    with open('/home/atshnik/PycharmProjects/Course_Work_4/pythonProject/data/vacancies.json', 'r', encoding="utf-8") as f:
        print(json.load(f))
    message = capsys.readouterr()
    assert message.out == ("{'name': 'Програмист', 'area': 'Рашка', '_Vacancy__salary': 1000, "
 "'schedule': '24/7', 'url': 'ya.ru'}\n")

def test_get_data(capsys, vacancy_fix_1):
    j_saver = JSONSaver()
    j_saver.add_vacancy(vacancy_fix_1)
    j_saver.get_data()
    message = capsys.readouterr()
    assert message.out == 'Програмист\n'

def test_delete_vacancy(vacancy_fix_1):
    j_saver = JSONSaver()
    j_saver.add_vacancy(vacancy_fix_1)
    j_saver.delete_vacancy()
    with open('/home/atshnik/PycharmProjects/Course_Work_4/pythonProject/data/vacancies.json', 'r') as f:
        assert len(f.readlines()) == 0

from src.HH_API import HeadHunterAPI

vacancies_API = HeadHunterAPI()
keyword = 'Python'

def test_get_vacancies_1():
    assert vacancies_API.get_vacancies(keyword) != None


def test_get_vacancies_2():
    assert len(vacancies_API.get_vacancies(keyword)) == 500


def test_get_vacancies_3(vacancies_fix):
    assert type(vacancies_fix) == list

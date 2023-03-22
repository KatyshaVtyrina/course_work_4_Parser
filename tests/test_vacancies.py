from classes.vacanсy import Vacancy, HHVacancy, SJVacancy
from utils.utils import get_vacancies


def test_get_attributes_hh(get_info_hh):
    """Ожидается получение атрибутов экземпляра HHVacancy"""
    hh = HHVacancy(get_info_hh)
    assert hh.name == "Программист Python Junior"
    assert hh.salary is None
    assert hh.url == "https://hh.ru/vacancy/77146976"
    assert hh.description == "Обеспечивать работоспособность и доступность бизнес-систем компании."
    assert hh.date_published == '16.03.2023 17:55:48'


def test_get_attributes_sj(get_info_sj):
    """Ожидается получение атрибутов экземпляра SJVacancy"""
    sj = SJVacancy(get_info_sj)
    assert sj.name == "Senior 1С программист"
    assert sj.salary == {'from': 0,
                         'to': 200000,
                         'currency': 'rub'}
    assert sj.url == "https://www.superjob.ru/vakansii/senior-1s-programmist-45570129.html"
    assert sj.description == "Компания Альфасклад предоставляет складские услуги физическим и юридическим лицам."
    assert sj.date_published == '14.03.2023 13:09:20'


def test_get_salary(vacancies):
    data = get_vacancies(vacancies)
    assert data[-1].get_salary() == 'не указана'
    assert data[0].get_salary() == 'не указана'
    assert data[1].get_salary() == "до 200000 руб/мес"
    assert data[2].get_salary() == "от 90000 руб/мес"
    assert data[3].get_salary() == 'не указана'
    assert data[4].get_salary() == "от 100000 руб/мес"
    assert data[5].get_salary() == "до 100000 руб/мес"
    assert data[6].get_salary() == "от 60000 до 220000 руб/мес"


def test_gt_and_lt(vacancies):
    data = get_vacancies(vacancies)
    assert data[0].__gt__(data[1]) is True
    assert data[0].__lt__(data[1]) is False


def test_str_vacancy(vacancies):
    vacancy = Vacancy(vacancies[0])
    assert vacancy.__str__() == 'Вакансия - Программист Python Junior, заработная плата - не указана'


def test_str_hh_vacancy(vacancies):
    hh = HHVacancy(vacancies[1])
    assert hh.__str__() == 'HH: Python разработчик, зарплата: до 200000 руб/мес'


def test_str_sj_vacancy(vacancies):
    sj = SJVacancy(vacancies[8])
    assert sj.__str__() == 'SJ: DevOps Engineer, зарплата: от 60000 до 250000 руб/мес'


from classes.engine import HH, SuperJob
from classes.vacanсy import HHVacancy, SJVacancy
from utils.utils import print_info, check_search, get_top_vacancies_by_date, get_vacancies, \
    get_top_vacancies_by_to_salary


def test_print_info(capsys):
    """Ожидается вывод построчно с нумерацией, если список, либо вывод строки"""
    print_info("не указана зарплата")
    captured = capsys.readouterr()
    assert captured.out == "не указана зарплата\n"
    print_info([1, 2])
    captured = capsys.readouterr()
    assert captured.out == '1 - 1\n' \
                           '2 - 2\n'


def test_check_search(hh, sj):
    """Ожидается проверка вакансии на существование"""
    hh2 = HH("aaaaaaaaaa")
    sj2 = SuperJob('aaaaaaaaa')
    assert check_search(hh, sj) is True
    assert check_search(hh2, sj2) is False


def test_get_vacancies(vacancies):
    """Ожидается получение экземпляров HHVacancy/SJVacancy"""
    assert isinstance(get_vacancies(vacancies), list)
    assert isinstance(get_vacancies(vacancies)[0], HHVacancy)
    assert isinstance(get_vacancies(vacancies)[-1], SJVacancy)


def test_get_top_vacancies_by_date(vacancies):
    """Ожидается сортировка по дате от большей к меньшей"""
    assert get_top_vacancies_by_date(vacancies, 3)[0].date_published == "16.03.2023 17:55:48"
    assert get_top_vacancies_by_date(vacancies, 3)[-1].date_published == "16.03.2023 13:09:47"


def test_get_top_vacancies_by_to_salary(vacancies, vacancies_no_salary):
    """Ожидается сортировка по зарплате from"""
    assert get_top_vacancies_by_to_salary(vacancies, 3)[0].salary == {"from": 100000,
                                                                      "currency": "RUR",
                                                                      "gross": False}

    assert get_top_vacancies_by_to_salary(vacancies, 3)[-1].salary == {"from": 70000,
                                                                       "to": 230000,
                                                                       "currency": "rub"}

    assert get_top_vacancies_by_to_salary(vacancies_no_salary, 2) == "В вакансиях не указана зарплата"

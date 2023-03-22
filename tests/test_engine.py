from classes.connector import Connector
from classes.engine import HH, SuperJob, Engine


def test_get_connector(path_connector):
    """Ожидается возврат экземпляра Connector"""
    assert isinstance(Engine.get_connector(path_connector), Connector)


def test_get_format_date_hh():
    """Ожидается форматирование даты"""
    assert HH.get_format_date('2023-03-13T07:54:44+0300') == '13.03.2023 07:54:44'


def test_get_format_date_sj():
    """Ожидается форматирование даты"""
    assert SuperJob.get_format_date(1678788560) == '14.03.2023 13:09:20'


def test_get_request_hh(hh, hh_no_experience):
    """Ожидается ответ на запрос в формате dict или обработка исключения"""
    assert type(hh.get_request()) is dict
    assert type(hh_no_experience.get_request()) is dict

    HH.URL = ''
    assert hh.get_request() == print('Не удается получить данные')

    HH.URL = 'https://api.hh.ru/vacancies'


def test_get_request_sj(sj, sj_no_experience):
    """Ожидается ответ на запрос в формате dict или обработка исключения"""
    assert type(sj.get_request()) is dict
    assert type(sj_no_experience.get_request()) is dict

    SuperJob.URL = ''
    assert sj.get_request() == print('Не удается получить данные')

    SuperJob.URL = 'https://api.superjob.ru/2.0/vacancies/'


def test_get_info_vacancy_hh(hh_json, get_info_hh):
    """Ожидается получение информации о вакансии в нужном формате"""
    hh = HH('')
    assert HH.get_info_vacancy(hh, data=hh_json) == get_info_hh


def test_get_info_vacancy_sj(sj_json, get_info_sj):
    """Ожидается получение информации о вакансии в нужном формате"""
    sj = SuperJob('')
    assert SuperJob.get_info_vacancy(sj, data=sj_json) == get_info_sj


def test_get_vacancy_hh(hh):
    """Ожидается получение списка вакансий"""
    assert isinstance(hh.get_vacancies(), list)


def test_get_vacancy_sj(sj):
    """Ожидается получение списка вакансий"""
    assert isinstance(sj.get_vacancies(), list)

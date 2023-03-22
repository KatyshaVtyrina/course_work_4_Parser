import json
import pytest
import os

from classes.connector import Connector
from classes.engine import HH, SuperJob


@pytest.fixture
def path_connector():
    return os.path.join('tests', 'test_data/test_connector.json')


@pytest.fixture
def connector():
    file = os.path.join('tests', 'test_data/test_connector.json')
    return Connector(file)


@pytest.fixture
def hh():
    return HH('python')


@pytest.fixture
def hh_no_experience():
    return HH('python', 'noExperience')


@pytest.fixture
def sj():
    return SuperJob('python')


@pytest.fixture
def sj_no_experience():
    return SuperJob('python', 'noExperience')


@pytest.fixture
def hh_json():
    path = os.path.join('tests', 'test_data/test_hh.json')
    with open(path) as file:
        data = json.load(file)
    return data


@pytest.fixture
def sj_json():
    path = os.path.join('tests', 'test_data/test_sj.json')
    with open(path) as file:
        data = json.load(file)
    return data


@pytest.fixture
def get_info_hh():
    info = {
        'source': 'HeadHunter',
        'name': "Программист Python Junior",
        'url': "https://hh.ru/vacancy/77146976",
        'description': "Обеспечивать работоспособность и доступность бизнес-систем компании.",
        'salary': None,
        'date_published': '16.03.2023 17:55:48'
    }
    return info


@pytest.fixture
def get_info_sj():
    info = {
        'source': 'SuperJob',
        'name': "Senior 1С программист",
        'url': "https://www.superjob.ru/vakansii/senior-1s-programmist-45570129.html",
        'description': "Компания Альфасклад предоставляет складские услуги физическим и юридическим лицам.",
        'salary': {'from': 0,
                   'to': 200000,
                   'currency': 'rub'},
        'date_published': '14.03.2023 13:09:20'
    }
    return info


@pytest.fixture
def vacancies():
    path = os.path.join('tests', 'test_data/test_all_vacancies.json')
    with open(path) as file:
        data = json.load(file)
    return data


@pytest.fixture
def vacancies_no_salary():
    path = os.path.join('tests', 'test_data/test_salary_none.json')
    with open(path) as file:
        data = json.load(file)
    return data

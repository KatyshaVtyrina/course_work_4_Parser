import datetime
from abc import ABC, abstractmethod
import requests
import os
from classes.connector import Connector


class Engine(ABC):

    @abstractmethod
    def get_request(self):
        """Запрос вакансий через API"""
        ...

    @staticmethod
    def get_connector(file_name: str) -> Connector:
        """ Возвращает экземпляр класса Connector """
        return Connector(file_name)


class HH(Engine):
    URL = 'https://api.hh.ru/vacancies'

    def __init__(self, search: str, experience=None):
        """Инициализируется запросом пользователя"""
        self.search = search
        self.__params = {'text': f'{self.search}', 'page': 0, 'per_page': 100}
        if experience is not None:
            self.__params['experience'] = experience

    @staticmethod
    def get_format_date(date: str) -> str:
        """Возвращает отформатированную дату"""
        date_format = datetime.datetime.fromisoformat(date).strftime("%d.%m.%Y %X")
        return date_format

    def get_request(self):
        """Запрос вакансий через API"""
        try:
            response = requests.get(self.URL, self.__params)
            if response.status_code == 200:
                return response.json()

        except requests.RequestException:
            print('Не удается получить данные')

    def get_info_vacancy(self, data: dict) -> dict:
        """Получаем информацию о вакансии"""
        info = {
            'source': 'HeadHunter',
            'name': data['name'],
            'url': data['alternate_url'],
            'description': data.get('snippet').get('responsibility'),
            'salary': data.get('salary'),
            'date_published': self.get_format_date(data['published_at'])
        }
        return info

    def get_vacancies(self) -> list:
        """Получаем информацию о вакансии для дальнейшей записи в файл и создания экземпляров Vacancy"""
        vacancies = []
        page = 0
        while True:
            self.__params['page'] = page
            data = self.get_request()
            for vacancy in data.get('items'):
                if vacancy in vacancies:
                    continue

                elif vacancy.get('salary') is not None and vacancy.get('salary').get('currency') is not None:
                    if vacancy.get('salary').get('currency') == "RUR":
                        vacancies.append(self.get_info_vacancy(vacancy))
                    else:
                        continue
                else:
                    vacancies.append(self.get_info_vacancy(vacancy))

            if data.get('pages') - page <= 1:
                break

            elif len(vacancies) >= 500:
                break

            else:
                page += 1

        return vacancies


class SuperJob(Engine):

    HEADERS = {"X-Api-App-Id": os.environ["SUPERJOB_API_KEY"]}
    URL = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self, search: str):
        """Инициализируется запросом пользователя"""
        self.search = search
        self.__params = {'keywords': f'{self.search}', 'count': 100,  'page': 0}

    @staticmethod
    def get_format_date(date: int) -> str:
        """Возвращает отформатированную дату"""
        date_format = datetime.datetime.fromtimestamp(date).strftime("%d.%m.%Y %X")
        return date_format

    def get_request(self):
        """Запрос вакансий через API"""
        try:
            response = requests.get(url=self.URL, headers=self.HEADERS, params=self.__params)
            if response.status_code == 200:
                return response.json()
        except requests.RequestException:
            print('Не удается получить данные')

    def get_info_vacancy(self, data: dict) -> dict:
        """Получаем информацию о вакансии"""
        salary = {'from': data['payment_from'],
                  'to': data['payment_to'],
                  'currency': data['currency']}
        info = {
            'source': 'SuperJob',
            'name': data['profession'],
            'url': data['link'],
            'description': data.get('client').get('description'),
            'salary': salary,
            'experience': data.get('experience').get('title'),
            'date_published': self.get_format_date((data['date_published'])),
        }
        return info

    def get_vacancies(self) -> list:
        """Получает список всех вакансий"""
        vacancies = []
        for i in range(10):
            self.__params['page'] = i
            data = self.get_request()
            for vacancy in data['objects']:
                if vacancy in vacancies:
                    continue
                elif vacancy.get('currency') is not None:
                    if vacancy.get('currency') == "rub":
                        vacancies.append(self.get_info_vacancy(vacancy))
                    else:
                        continue
                else:
                    vacancies.append(self.get_info_vacancy(vacancy))
            if len(vacancies) >= 500:
                break
        return vacancies

    def get_vacancies_no_experience(self) -> list:
        """Получает список всех вакансий без опыта работы"""
        vacancies = []
        for i in range(10):
            self.__params['page'] = i
            data = self.get_request()
            for vacancy in data.get('objects'):
                if vacancy.get('experience').get('title') == 'Без опыта':
                    if vacancy in vacancies:
                        continue
                    elif vacancy.get('currency') is not None:
                        if vacancy.get('currency') == "rub":
                            vacancies.append(self.get_info_vacancy(vacancy))
                        else:
                            continue
                    else:
                        vacancies.append(self.get_info_vacancy(vacancy))
            if len(vacancies) >= 500:
                break

        return vacancies


hh = SuperJob('python')

import json


class Vacancy:
    __slots__ = ('__name', '__url', '__description', '__salary', '__data_date_published')

    def __init__(self, data: dict):

        self.__name = data['name']
        self.__url = data['url']
        self.__description = data['description']
        self.__salary = data['salary']
        self.__data_date_published = data['date_published']

    def __str__(self):
        return f'Вакансия - {self.name}, заработная плата - {self.salary}'

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    @property
    def description(self):
        return self.__description

    def __get_salary(self) -> str:
        """Возвращает зарплату в отформативанном виде"""
        if self.__salary is not None:

            if self.__salary['from'] is None and self.__salary['to'] is None:
                return 'не указана'

            elif self.__salary['from'] is None:
                return f" до {self.__salary['to']} руб/мес"

            elif self.__salary['to'] is None:
                return f" от {self.__salary['from']} руб/мес"

            elif self.__salary['from'] != 0 and self.__salary['to'] != 0:
                return f" от {self.__salary['from']} до {self.__salary['to']} руб/мес"

            elif self.__salary['from'] == 0 and self.__salary['to'] == 0:
                return 'не указана'

            elif self.__salary['from'] == 0 and self.__salary['to'] != 0:
                return f" до {self.__salary['to']} руб/мес"

            elif self.__salary['from'] != 0 and self.__salary['to'] == 0:
                return f" от {self.__salary['from']} руб/мес"

        return 'не указана'

    @property
    def salary(self) -> str:
        return self.__get_salary()


class CountMixin:

    @staticmethod
    def _get_count_of_vacancy(file, sourse):
        with open(file) as f:
            data = json.load(f)
        count = 0
        for item in data:
            if item['source'] == sourse:
                count += 1

        return count

    @property
    def get_count_of_vacancy(self):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        pass


class HHVacancy(Vacancy, CountMixin):  # add counter mixin
    """ HeadHunter Vacancy """
    def __str__(self):
        return f'HH: {self.name}, зарплата: {self.salary}'


class SJVacancy(Vacancy, CountMixin):  # add counter mixin
    """ SuperJob Vacancy """

    # def __init__(self, data):
    #     super().__init__(data)
    #     self.experience = data['experience']

    def __str__(self):
        return f'SJ: {self.name}, зарплата: {self.salary}'


def sorting(vacancies):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    pass


def get_top(vacancies, top_count):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    pass


# hh = SJVacancy()

# print(CountMixin._get_count_of_vacancy('all.json', 'SuperJob'))

import json
from classes.vacanсy import HHVacancy, SJVacancy


def print_vacancies(data: list | str):
    """Вывод построчно с нумерацией, если список, либо вывод строки"""
    if isinstance(data, list):
        count = 1
        for item in data:
            print(f'{count} - {item}')
            count += 1
    else:
        print(data)


def get_vacancies(vacancies: list) -> list[HHVacancy | SJVacancy]:
    """Возвращает экземпляры HHVacancy/SJVacancy"""
    vacancies_list = []
    for vacancy in vacancies:
        if vacancy['source'] == "HeadHunter":
            vacancies_list.append(HHVacancy(vacancy))
        else:
            vacancies_list.append(SJVacancy(vacancy))
    return vacancies_list


def get_top_vacancies_by_date(file, top_count):
    """Возвращает top_count последних вакансий по дате публикации"""
    with open(file) as f:
        data = json.load(f)

    data.sort(key=lambda k: k['date_published'], reverse=True)
    top_vacancies = data[:top_count]

    return get_vacancies(top_vacancies)


def get_top_vacancies_by_to_salary(top_count, file):
    """Возвращает top_count вакансий по максимальной зарплате"""
    with open(file) as f:
        data = json.load(f)

    # Перебор данных из файла по зарплате
    vacancies = []
    for item in data:
        if item.get('salary') is None or item.get('salary').get('from') is None:
            continue
        else:
            vacancies.append(item)

    # Сортировка по зарплате
    vacancies.sort(key=lambda k: k['salary']['from'], reverse=True)
    top_vacancies = vacancies[:top_count]

    if len(top_vacancies) == 0:
        return "В вакансиях без опыта работы не указана зарплата"
    else:
        return get_vacancies(top_vacancies)
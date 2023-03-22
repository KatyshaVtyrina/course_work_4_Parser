import os

from classes.connector import Connector
from classes.engine import HH, SuperJob
from utils.utils import get_top_vacancies_by_date, get_top_vacancies_by_to_salary, print_vacancies


def main():

    path_all = os.path.join('data/all.json')
    path_no_experience = os.path.join('data/no_experience.json')

    while True:
        search = input("Введите слово, по которому будем искать вакансию\n")
        hh_all = HH(search)
        hh_no_experience = HH(search, 'noExperience')
        sj_all = SuperJob(search)
        if hh_all.get_request()['items'] == [] or sj_all.get_request()['objects'] == []:
            print('Такой вакансии нет')
            continue
        else:
            data_all = hh_all.get_vacancies() + sj_all.get_vacancies()
            all_vacancies = Connector(path_all)
            all_vacancies.insert(data_all)

            data_no_experience = hh_no_experience.get_vacancies() + sj_all.get_vacancies_no_experience()
            no_experience_vacancies = Connector(path_no_experience)
            no_experience_vacancies.insert(data_no_experience)
            break

    while True:
        top_count = input('Укажите какое количество вакансий будем выводить на экран\n')
        if not top_count.isdigit() or int(top_count) <= 0:
            print('Количество должно быть целым числом больше ноля. Попробуйте еще раз')
            continue
        else:
            top_count = int(top_count)
            break

    while True:
        try:
            print(f"Меню:\n\
                1 - вывести {top_count} последних вакансии\n\
                2 - вывести топ-{top_count} вакансий заработку\n\
                3 - вывести {top_count} последних вакансий без опыта работы \n\
                4 - вывести топ-{top_count} вакансий по заработку без опыта работы \n\
                stop - закончить работу")
            print()
            user_input = input("Введите нужный вариант\n")

            if user_input == '1':
                data = get_top_vacancies_by_date(file=path_all, top_count=top_count)
                print_vacancies(data)

            elif user_input == '2':
                data = get_top_vacancies_by_to_salary(file=path_all, top_count=top_count)
                print_vacancies(data)

            elif user_input == '3':
                data = get_top_vacancies_by_date(file=path_no_experience, top_count=top_count)
                print_vacancies(data)

            elif user_input == '4':
                data = get_top_vacancies_by_to_salary(file=path_no_experience, top_count=top_count)
                print_vacancies(data)

            elif user_input.lower() == 'stop':
                print('Программа завершает работу')
                break

            else:
                raise ValueError

        except ValueError:
            print("Такого варианта нет, попробуйте еще раз")
            continue

        else:
            print('Показать еще меню? Y/N')
            choice = input().upper()
            if choice == 'Y':
                continue
            else:
                print('Программа завершает работу')
                break

    exit()


if __name__ == '__main__':
    main()

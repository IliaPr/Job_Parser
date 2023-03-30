from engines import Engine, HH, Superjob
from top_jobs import JobVacancyList, File


if __name__ == '__main__':
    print('Привет! Введи ключевое слово для поиска вакансий')
    keyword = input().lower()
    print('Выполняется поиск, ожидайте...\n')
    hh = HH()
    hh.get_request(keyword)
    sj = Superjob()
    sj.get_request(keyword)
    f = File()
    f.combine()
    print('Вакансии найдены! Введите номер варианта представления результатов: \n1.Вывод профессий по убыванию заработной платы.\n2.Вывод профессий по заданной минимальной заработной платы. (Введите 1 или 2)')
    user_choice = int(input())
    if user_choice == 1:
        print('Введите количество вакансий для вывода')
        number_of_vacancies = int(input())
        if number_of_vacancies <= 0:
            print('Количество вакасий должно быть больше 0! Введите еще раз')
            number_of_vacancies = int(input())
        else:
            job_vacancies = JobVacancyList()
            job_vacancies.sort_by_salary_increase()
            job_vacancies.top_vacancies_by_salary(n=number_of_vacancies)
    elif user_choice == 2:
        print('Введите минимальное значение заработной платы: ')
        user_salary = int(input())
        print('Введите количество вакансий для вывода')
        number_of_vacancies = int(input())
        if number_of_vacancies <= 0:
            print('Количество вакасий должно быть больше 0! Введите еще раз')
            number_of_vacancies = int(input())
        else:
            job_vacancies = JobVacancyList()
            job_vacancies.sort_by_user_input_salary(number_of_vacancies, user_salary)

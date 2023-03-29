from engines import Engine, HH, Superjob
from top_jobs import JobVacancyList, File


if __name__ == '__main__':
    print('Привет! Введи ключевое слово для поиска вакансий')
    keyword = input().lower()
    print('Введите количество вакансий по убыванию заработной платы для вывода')
    number_of_vacancies = int(input())
    print('Выполняется поиск, ожидайте...\n')
    if number_of_vacancies <= 0:
        print('Количество вакасий должно быть больше 0! Введите еще раз')
        number_of_vacancies = int(input())
    else:
        hh = HH()
        hh.get_request(keyword)
        sj = Superjob()
        sj.get_request(keyword)
        f = File()
        f.combine()
        job_vacancies = JobVacancyList()
        job_vacancies.sort_by_salary_increase()
        job_vacancies.top_vacancies_by_salary(n=number_of_vacancies)


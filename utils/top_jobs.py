from engines import Engine, HH, Superjob
import json

class File:
    def combine(self):
        '''Создание общего файла с вакансиями'''
        hh = HH()
        hh.get_request()
        sj = Superjob()
        sj.get_request()
        Engine.get_connector('All_jobs.json')
        with open('vacanciesHH.json', 'r') as f1, open('vacanciesSJ.json', 'r') as f2, open('All_jobs.json', 'w') as outfile:
            data1_str = f1.read()
            data2_str = f2.read()

            data1 = json.loads(data1_str)
            data2 = json.loads(data2_str)

            combined_data = data1 + data2

            json.dump(combined_data, outfile, indent=4)


class Vacancy:
    def __init__(self, title, salary_from, salary_to, description, link):
        self.title = title
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.description = description
        self.link = link

    def __str__(self):
        return f"Название вакансии - {self.title}\nОписание: {self.description}\nЗарплата от: {self.salary_from}\nЗарплата до: {self.salary_to}\nСсылка на вакансию {self.link}"


class JobVacancyList:
    '''Сортировка вакансий'''
    def __init__(self):
        f = File()
        f.combine()
        with open('All_jobs.json', "r") as file:
            data = json.load(file)

        self.vacancies = []
        for vacancy in data:
            title = vacancy["Name"]
            if 'Salary' in vacancy:
                salary_from = vacancy["Salary"]['from']
                salary_to = vacancy["Salary"]['to']
            else:
                continue
            description = vacancy["Requirement"]
            link = vacancy['Link']
            self.vacancies.append(Vacancy(title, salary_from, salary_to, description, link))

    def sort_by_salary_increase(self):
        self.vacancies = sorted(self.vacancies, key=lambda v: v.salary_to)

    def top_vacancies_by_salary(self, n=5):
        sorted_vacancies = sorted(self.vacancies, key=lambda v: v.salary_to, reverse=True)
        top_vacancies = sorted_vacancies[:n]
        for vacancy in top_vacancies:
            print(f'{vacancy}\n')



job_vacancies = JobVacancyList()
job_vacancies.sort_by_salary_increase()
job_vacancies.top_vacancies_by_salary(n=10)


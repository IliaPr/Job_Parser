from utils import Engine
import json
class Vacancy:
    __slots__ = ('job_title', 'job_link', 'job_description', 'job_salary')

    def __init__(self, job_title, job_link, job_description, job_salary):
        self.job_title = job_title
        self.job_link = job_link
        self.job_description = job_description
        self.job_salary = job_salary


    def __str__(self):
        return f"Название вакансии - {self.job_title}\nОписание: {self.job_description}\nЗарплата: {self.job_salary}\nСсылка на вакансию{self.job_link}"

class File:
    def combine(self):
        '''Создание общего файла с вакансиями'''
        Engine.get_connector('All_jobs.json')
        with open('vacanciesHH.json', 'r') as f1, open('vacanciesSJ.json', 'r') as f2, open('All_jobs.json', 'w') as outfile:
            # read in the JSON files as strings
            data1_str = f1.read()
            data2_str = f2.read()

            # parse the JSON strings into Python objects
            data1 = json.loads(data1_str)
            data2 = json.loads(data2_str)

            # combine the two lists of dictionaries
            combined_data = data1 + data2

            # write the combined data to the output file with indentation
            json.dump(combined_data, outfile, indent=4)

json_combiner = File()
json_combiner.combine()


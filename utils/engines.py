import json
import os

import requests
from abc import ABC, abstractmethod


from connector import Connector

class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass

    @staticmethod
    def get_connector(file_name):
        """ Возвращает экземпляр класса Connector """
        connector = Connector(file_name)
        connector.data_file = file_name
        return connector
class HH(Engine):
    def get_request(self):
        Engine.get_connector('vacanciesHH.json')
        jobs = []
        for i in range(50):
            url = "https://api.hh.ru/vacancies"
            par = {'text': 'python', 'areas': 113, 'page': i}
            self.request = requests.get(url, params=par).json()
            for a in range(20):
                job = {}
                job["Name"] = self.request['items'][a]['name']
                if self.request['items'][a]['salary'] == None:
                    job['Salary'] = {'from': 0, 'to': 0}
                elif self.request['items'][a]['salary']['from'] == None:
                    if self.request['items'][a]['salary']['currency'] == 'RUR':
                        job['Salary'] = {'from': 0, 'to': self.request['items'][a]['salary']['to']}
                elif self.request['items'][a]['salary']['to'] == None:
                    if self.request['items'][a]['salary']['currency'] == 'RUR':
                        job['Salary'] = {'from': self.request['items'][a]['salary']['from'], 'to': 0}
                else:
                    if self.request['items'][a]['salary']['currency'] == 'RUR':
                        job['Salary'] = {'from': self.request['items'][a]['salary']['from'],
                                         'to': self.request['items'][a]['salary']['to']}
                # job = {'Salary': {'from':  self.request['items'][a]['salary']['from']}}
                # job = {'Salary': {'to':  self.request['items'][a]['salary']['to']}}
                #job["Salary"] = self.request['items'][a]['salary']
                job["Link"] = self.request['items'][a]['alternate_url']
                job['Requirement'] = self.request['items'][a]['snippet']['requirement']
                jobs.append(job)

            with open('vacanciesHH.json', 'w') as f:
                json.dump(jobs, f, indent=4)

class Superjob(Engine):
    def get_request(self):
        Engine.get_connector('vacanciesSJ.json')
        jobs = []
        for i in range(6):
            url = 'https://api.superjob.ru/2.0/vacancies/'
            api_key: str = os.getenv('SJApi')
            headers = {"X-Api-App-Id": api_key}
            par = {'keywords': 'python', 'page': i, 'count': 100}
            self.request = requests.get(url, headers=headers, params=par).json()
            for a in range(100):
                job = {}
                job["Name"] = self.request['objects'][a]['profession']
                job['Salary'] = {'from': self.request['objects'][a]['payment_from'], 'to': self.request['objects'][a]['payment_to']}
                job["Link"] = self.request['objects'][a]['link']
                job['Requirement'] = self.request['objects'][a]['candidat']
                jobs.append(job)

        with open('vacanciesSJ.json', 'w') as f:
            json.dump(jobs, f, indent=4)

if __name__ == '__main__':
    hh = HH()
    hh.get_request()






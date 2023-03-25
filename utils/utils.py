import json
import os

import requests
from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def get_request(self):
        ...

    @staticmethod
    def get_connector(file_name):
        """ Возвращает экземпляр класса Connector """
        pass
class HH(Engine):
    def get_request(self):
        jobs = []
        for i in range(1):
            url = "https://api.hh.ru/vacancies"
            par = {'text': 'python', 'areas': 113, 'page': i}
            self.request = requests.get(url, params=par).json()
            if self.request == []:
                continue
            for a in range(20):
                jobs.append(self.request['items'][a]['name'])
                jobs.append(self.request['items'][a]['alternate_url'])
                jobs.append(self.request['items'][a]['snippet']['requirement'])
                jobs.append(self.request['items'][a]['salary'])

            with open('vacanciesHH.json', 'w') as f:
                json.dump(jobs, f, indent=4)

class Superjob(Engine):
    def get_request(self):
        jobs = []

        for i in range(1):
            url = 'https://api.superjob.ru/2.0/vacancies/'
            api_key: str = os.getenv('SJApi')
            headers = {api_key}
            par = {'keywords': 'python', 'page': i, 'count': 100}
            self.request = requests.get(url, headers=headers, params=par).json()
            if self.request == []:
                continue
            for a in range(100):
                jobs.append(self.request['objects'][a]['profession'])
                jobs.append(self.request['objects'][a]['link'])
                jobs.append(self.request['objects'][a]['candidat'])
                jobs.append(self.request['objects'][a]['payment_from'])

        with open('vacanciesSJ.json', 'w') as f:
            json.dump(jobs, f, indent=4)
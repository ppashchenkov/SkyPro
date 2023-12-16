import requests
from company_api import CompanyApi


class EmployeeApi:
    def __init__(self, url):
        self.url = url

    def get_employees(self, params_to_add):
        return requests.get(self.url + '/employee', params=params_to_add).json()

    def add_employee(self, employee):
        my_headers = {}
        my_headers["x-client-token"] = CompanyApi.get_token()
        return requests.post(self.url + '/employee', json=employee, headers=my_headers).json()


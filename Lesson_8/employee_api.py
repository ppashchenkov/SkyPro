import requests
from company_api import CompanyApi


class EmployeeApi:
    def __init__(self, url):
        self.url = url

    def get_employees(self, company_id):
        resp =  requests.get(self.url + '/employee', params=str(company_id))

        return resp

    def add_employee(self, token, employee):
        my_headers = token
        return requests.post(self.url + '/employee', json=employee, headers=my_headers).json()

    def get_employee_by_id(self, employee_id):
        resp = requests.get(self.url + '/employee/' + employee_id)

        return resp.json()

    def edit_employee_by_id(self, employee_id, token, edited_employee):
        my_headers = token

        return requests.patch(self.url + '/employee/' + employee_id, json= edited_employee, headers=my_headers).json()

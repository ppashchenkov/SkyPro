import requests
import json
from employee_api import EmployeeApi
from company_api import CompanyApi


base_url = "https://x-clients-be.onrender.com"
new_company = {
    'name' : 'My New Company',
    'description' : 'New description for My New Company'
}
employee = {
            "id": 0,
            "firstName": "Peter",
            "lastName": "Petrov",
            "middleName": "Petrovich",
            "companyId": 0,
            "email": "p.petrov@mail.ru",
            "url": "https://none.com",
            "phone": "+79998887755",
            "birthdate": "1980-12-16T09:36:16.282Z",
            "isActive": true
}

api_employee = EmployeeApi(base_url)
api_company = CompanyApi(base_url)

company_id = api_company.create_company(new_company)["id"]


def test_add_employee():
    body = api_employee.add_employee(employee)
    assert body["id"] > 0

# def test_get_employees():
#     resp = api_employee.get_employees(company_id)
#     body = resp.json()
#     # assert resp.status_code == 200
#     assert len(body) >= 0


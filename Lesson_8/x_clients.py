import requests
import json
from employee_api import EmployeeApi
from company_api import CompanyApi
from auth_api import AuthApi

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
            "isActive": True
}

api_auth = AuthApi(base_url)
api_employee = EmployeeApi(base_url)
api_company = CompanyApi(base_url)

# company_id = api_company.create_company(new_company)["id"]

token = api_auth.get_token(user='roxy', password='animal-fairy')
print(token)

# def test_add_employee():
#     body = api_employee.add_employee(employee)
#     assert body["id"] > 0

# def test_get_employees():
#     resp = api_employee.get_employees(company_id)
#     body = resp.json()
#     # assert resp.status_code == 200
#     assert len(body) >= 0


from time import sleep
from employee_api import EmployeeApi
from company_api import CompanyApi
from auth_api import AuthApi

base_url = "https://x-clients-be.onrender.com"
new_company = {
    'name': 'My New Company',
    'description': 'New description for My New Company'
}
new_employee_1 = {
            "id": 0,
            "firstName": "Peter",
            "lastName": "Petrov",
            "middleName": "Petrovich",
            "companyId": 0,
            "email": "p.petrov@mail.ru",
            "url": "https://petrov.com/image.jpg",
            "phone": "+79998887755",
            "birthdate": "1980-12-16",
            "isActive": True
}
edited_employee = {
    "lastName": "Ivanov",
    "email": "p.ivanov@mail.ru",
    "url": "https://ivanov.com/image.jpg",
    "phone": "+79998887757",
    "isActive": True
}
user = {
    "username": "bloom",
    "password": "fire-fairy"
}

api_auth = AuthApi(base_url)
api_employee = EmployeeApi(base_url)
api_company = CompanyApi(base_url)

my_token = api_auth.get_token(user)
new_company_id = api_company.create_company(my_token, new_company)["id"]
new_employee_1["companyId"] = new_company_id


def test_add_employee():
    my_new_employee = api_employee.add_employee(my_token, new_employee_1)

    assert my_new_employee["id"] > 0


def test_get_employees():
    response = api_employee.get_employees(new_company_id)

    assert len(response) == 1

def test_get_employee_by_id():
    my_new_employee = api_employee.add_employee(my_token, new_employee_1)
    employee_by_id = api_employee.get_employee_by_id(str(my_new_employee["id"]))

    assert employee_by_id["firstName"] == new_employee_1["firstName"]
    assert employee_by_id["lastName"] == new_employee_1["lastName"]
    assert employee_by_id["middleName"] == new_employee_1["middleName"]
    assert employee_by_id["companyId"] == new_employee_1["companyId"]
    assert employee_by_id["email"] is None
    assert employee_by_id["phone"] == new_employee_1["phone"]
    assert employee_by_id["birthdate"] == new_employee_1["birthdate"]
    assert employee_by_id["isActive"]


def test_switch_status_employee():
    my_new_employee = api_employee.add_employee(my_token, new_employee_1)
    employee_by_id = api_employee.get_employee_by_id(str(my_new_employee["id"]))
    employee_status_before = employee_by_id["isActive"]
    edited_status_employee = api_employee.edit_employee_by_id(str(my_new_employee["id"]), my_token, {"isActive": False})
    employee_status_after = edited_status_employee["isActive"]

    assert employee_status_before != employee_status_after


def test_edit_employee():
    my_new_employee = api_employee.add_employee(my_token, new_employee_1)
    my_edited_employee = api_employee.edit_employee_by_id(str(my_new_employee["id"]), my_token, edited_employee)

    assert my_edited_employee["lastName"] == edited_employee["lastName"]
    assert my_edited_employee["email"] == edited_employee["email"]
    assert my_edited_employee["url"] == edited_employee["url"]
    assert my_edited_employee["phone"] == edited_employee["phone"]
    assert my_edited_employee["isActive"] == edited_employee["isActive"]
    assert my_new_employee["id"] == my_edited_employee["id"]


companies = api_company.get_company_list()
for c in companies:
    if c["name"] == new_company["name"]:
        deleted = api_company.delete_company(my_token, str(c["id"]))

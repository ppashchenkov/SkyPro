from employee_api import EmployeeApi
from company_api import CompanyApi
from auth_api import AuthApi
from sqlalchemy import column
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy import select
from sqlalchemy import table
from sqlalchemy import text

db_connection_string = "postgresql://x_clients_user:[axcmq7V3QLCQwgL39GymqgasJhUlDbH4@dpg-cl53o6ql7jac73cbgi2g-a.frankfurt-postgres.render.com](mailto:axcmq7V3QLCQwgL39GymqgasJhUlDbH4@dpg-cl53o6ql7jac73cbgi2g-a.frankfurt-postgres.render.com)/x_clients"

url = URL.create(
    drivername="postgresql",
    username="x_clients_user",
    password="axcmq7V3QLCQwgL39GymqgasJhUlDbH4",
    host="dpg-cl53o6ql7jac73cbgi2g-a.frankfurt-postgres.render.com",
    database="x_clients"
)

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
            "birthdate": "1980-12-16T09:36:16.282Z",
            "isActive": True
}
edited_employee = {
    "lastName": "Ivanov",
    "email": "p.ivanov@mail.ru",
    "url": "https://ivanov.com",
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
print(f"My token {my_token['x-client-token']}")

engine = create_engine(url)
connection = engine.connect()
result = connection.execute(text("SELECT * FROM company"))

# new_company_id = api_company.create_company(my_token, new_company)["id"]
# print(f"new company id = {new_company_id}")
# #
# new_employee_1["companyId"] = new_company_id
# print(f"New employee companyId = {new_employee_1['companyId']}")
#
# my_new_employee = api_employee.add_employee(my_token, new_employee_1)
# my_new_employee_id = str(my_new_employee['id'])
# print(f" My New employee id = {my_new_employee_id}")
#
# company_employees = api_employee.get_employees(new_company_id)
# print(f"employees len= {len(company_employees)}")
# print(company_employees)
#
# employee_by_id = api_employee.get_employee_by_id(my_new_employee_id)
# print(f"Employee by id = {employee_by_id}")
#
# edited_employee_by_id = api_employee.edit_employee_by_id(my_new_employee_id, my_token, edited_employee)
# print(f"Edited employee by id = {edited_employee_by_id['id']}")
# print(edited_employee_by_id)
#
# # switch isActive
# if employee_by_id["isActive"]:
#     print("Current employee status = True")
# else:
#     print("Current employee status = False")
# edite_status_employee = api_employee.edit_employee_by_id(my_new_employee_id, my_token, {"isActive": False})
# if edite_status_employee["isActive"]:
#     print("New employee status = True")
# else:
#     print("New employee status = False")
#
# print("")
# print(f"Pause 2 seconds")
# sleep(2)
# companies = api_company.get_company_list()
#
# for c in companies:
#     if c["name"] == new_company["name"]:
#         # print(f"Company id = {str(c['id'])}")
#         deleted = api_company.delete_company(my_token, str(c["id"]))
#         print(f"Deleted company id = {str(deleted['id'])}")

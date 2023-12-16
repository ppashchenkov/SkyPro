import requests


class CompanyApi:
    def __init__(self, url):
        self.url = url

    def get_company_list(self, params_to_add = None):
        return requests.get(self.url + '/company', params=params_to_add).json()

    def get_token(self, user='roxy', password='animal-fairy'):
        creds = {
            'username' : user,
            'password' : password
        }
        return requests.post(self.url + '/auth/login', json=creds).json()["userToken"]

    def create_company(self, name, description=''):
        company = {
            'name' : name,
            'description' : description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        return requests.post(self.url + '/company', json=company, headers=my_headers).json()

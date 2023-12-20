import requests


class CompanyApi:
    def __init__(self, url):
        self.url = url

    def get_company_list(self, params_to_add=None):
        return requests.get(self.url + '/company', params=params_to_add).json()

    def create_company(self, token, company):
        my_headers = token

        return requests.post(self.url + '/company', json=company, headers=my_headers).json()

    def delete_company(self, token, company_id):
        my_headers = token

        resp = requests.get(self.url + '/company/delete/' + company_id, headers=my_headers)

        return resp.json()

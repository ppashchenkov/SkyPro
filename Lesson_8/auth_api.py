from time import sleep
import requests


class AuthApi:
    def __init__(self,url):
        self.url = url

    def get_token(self, user='roxy', password='animal-fairy'):
        creds = {
            'username' : user,
            'password' : password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        print(f"Status code = {resp.status_code}")
        if resp.status_code > 299:
            print("Getting Token: ", end='')
            for i in range(0,25):
                print(".", end='')
                sleep(5)
            resp = requests.post(self.url + '/auth/login', json=creds)
            if resp.status_code < 300:
                return resp.json()["userToken"]
        return resp.json()["userToken"]

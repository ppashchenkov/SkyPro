from time import sleep
import requests


class AuthApi:
    def __init__(self,url):
        self.url = url

    def get_token(self, user):
        my_token = {
            "x-client-token": ""
        }

        resp = requests.post(self.url + '/auth/login', json=user)
        print(f" status = {resp.status_code}")
        if resp.status_code > 299:
            sleep(120)
            resp = requests.post(self.url + '/auth/login', json=user)
        my_token["x-client-token"] = resp.json()["userToken"]
        print(f"Token = {my_token}")

        return my_token

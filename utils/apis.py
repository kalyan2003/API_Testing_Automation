import requests
import json


class APIS:
    BASE_URL = "https://thinking-tester-contact-list.herokuapp.com"

    def __init__(self):
        self.header = {
            "Content-Type": "application/json",

        }


    def get(self, endpoint, authToken):
        url = f'{self.BASE_URL}/{endpoint}'
        headers = {
            **self.header,
            "Authorization": f"Bearer {authToken}"
        }
        response = requests.get(url, headers=headers)
        return response

    def register(self, data):
        url = f'{self.BASE_URL}/users'
        response = requests.post(url, headers=self.header, data=json.dumps(data))
        return response

    def patch(self,endpoint,authToken,data):
        url = f'{self.BASE_URL}/{endpoint}'
        headers = {
            **self.header,
            "Authorization": f"Bearer {authToken}"
        }
        response = requests.patch(url,headers=headers,data=json.dumps(data))
        return response


    def log_out_user(self,endpoint,authToken):
        url = f'{self.BASE_URL}/{endpoint}'
        headers = {
            **self.header,
            "Authorization": f"Bearer {authToken}"
        }
        response = requests.post(url,headers=headers)
        return response

    def log_in_user(self, endpoint, data):
        url = f'{self.BASE_URL}/{endpoint}'
        response = requests.post(url, headers=self.header, data=json.dumps(data))
        return response

    def delete_user(self, endpoint, authToken):
        url = f'{self.BASE_URL}/{endpoint}'
        headers = {
            **self.header,
            "Authorization": f"Bearer {authToken}"
        }
        response = requests.delete(url, headers=headers)
        return response

    def add_contact(self, endpoint, authToken, data):
        url = f'{self.BASE_URL}/{endpoint}'
        headers = {
            **self.header,
            "Authorization": f"Bearer {authToken}"
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response

    def get_contact(self,endpoint,authToken):
        url = f'{self.BASE_URL}/{endpoint}'
        headers = {
            **self.header,
            "Authorization": f"Bearer {authToken}"
        }
        response = requests.get(url, headers=headers)
        return response






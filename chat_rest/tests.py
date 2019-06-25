from django.test import TestCase
import requests
import json


# Create your tests here.

def get_access_token():
    data = {'username': 'test_2', 'password': 'efirgetbierifre'}
    response_token = requests.post('http://127.0.0.1:8000/token/get/', json=data)
    return json.loads(response_token.content)['access']


class ChatTestCase(TestCase):
    BASE_URL = 'http://127.0.0.1:8000/'
    TOKEN = None

    def setUp(self):
        self.TOKEN = get_access_token()

    def test_create_user(self):
        data = {'username': 'test_username', 'password': 'test_username_password'}
        response = requests.post(self.BASE_URL + 'user/create/', json=data)
        # print(response.content)
        self.assertEqual(response.status_code, 201)

    def test_get_auth_token(self):
        data = {'username': 'test_2', 'password': 'mariadontberude'}
        response = requests.post(self.BASE_URL + 'token/get/', json=data)
        # print(response.content)
        self.assertEqual(response.status_code, 200)

    def test_create_private_chat(self):
        token = get_access_token()
        header = {'Authorization': 'Bearer ' + token}
        data = {'users_in_chat': [2, 4]}
        response = requests.post(self.BASE_URL + 'chat/create_private/', json=data, headers=header)
        # print(response.content)
        self.assertEqual(response.status_code, 201)

    def test_create_public_chat(self):
        token = get_access_token()
        header = {'Authorization': 'Bearer ' + token}
        data = {'users_in_chat': [2, 3]}
        response = requests.post(self.BASE_URL + 'chat/create_public/', json=data, headers=header)
        print(response.content)
        self.assertEqual(response.status_code, 201)

    def test_create_new_message(self):
        header = {'Authorization': 'Bearer ' + self.TOKEN}
        chat_id = 16
        data = {'content': 'SANYA_OTKOI'}
        response = requests.post(self.BASE_URL + f'chat/{chat_id}/create_message/', json=data, headers=header)
        print(response.content)
        self.assertEqual(response.status_code, 201)

    def test_get_last_messages(self):
        header = {'Authorization': 'Bearer ' + self.TOKEN}
        chat_id = 16
        response = requests.get(self.BASE_URL + f'chat/{chat_id}/get_last_messages/', headers=header)
        print(response.content)
        self.assertEqual(response.status_code, 200)

    def test_get_last_messages_quantity(self):
        header = {'Authorization': 'Bearer ' + self.TOKEN}
        chat_id = 16
        quantity = 3
        response = requests.get(self.BASE_URL + f'chat/{chat_id}/get_last_messages/{quantity}/', headers=header)
        print(response.content)
        self.assertEqual(response.status_code, 200)

    def test_get_message_from_chat(self):
        header = {'Authorization': 'Bearer ' + self.TOKEN}
        chat_id = 16
        message_id = 15
        response = requests.get(self.BASE_URL + f'chat/{chat_id}/get_message/{message_id}/', headers=header)
        print(response.content)
        self.assertEqual(response.status_code, 200)

    def test_edit_chat_message(self):
        header = {'Authorization': 'Bearer ' + self.TOKEN}
        chat_id = 16
        message_id = 22
        data = {'content': 'edited'}
        response = requests.put(self.BASE_URL + f'chat/{chat_id}/get_message/{message_id}/', json=data, headers=header)
        print(response.content)
        self.assertEqual(response.status_code, 200)

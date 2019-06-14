from urllib.parse import urlencode
import requests

APP_ID = 6471121
AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
VERSION = '5.74'

auth_params = {
    'client_id': APP_ID,
    'redirect_uri': 'https://oauth.vk.com/blank.html',
    'display': 'popup',
    'scope': 'friends,status,video',
    'response_type': 'token',
}

token_link = '?'.join((AUTHORIZE_URL, urlencode(auth_params)))
print(token_link)

token = '2eb0e9c5198797503fa6fb0c9f5d6e63423e738478b4c9c3e24c2f00964f04f57f8b3870acf6afd3cd0a9'

# def get_mutual():
#
#     inp2 = input('введите id пользователя:')
#
#     params = {
#         'v': VERSION,
#         'source_uid': 6471121,
#         'target_uid': inp2,
#         'access_token': token
#     }
#
#     response = requests.get('https://api.vk.com/method/friends.getMutual', params)
#     response = response.json()['response']
#
#     for id in response:
#         print('id общего друга:', id)
#         print('ссылка на страницу: https://vk.com/id', id, sep='')
#
#
# get_mutual()


userID1 = 6471121
userID2 = 6471123

user1 = User(userID1)
user2 = User(userID2)

class User:
    def __and__(self, other_user):
        params = {
            'v': VERSION,
            'source_uid': userID1,
            'target_uid': userID2,
            'access_token': token
        }

        response = requests.get('https://api.vk.com/method/friends.getMutual', params)
        response = response.json()['response']

        for id in response:
            print('id общего друга:', id)
            print('ссылка на страницу: https://vk.com/id', id, sep='')

user1 & user2
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

token = 'a071fd352e962a79f47f61a1d158978a4cdb99dfb0155d42628fb3bba795ffb066364b90460bfa2f937fa'

def get_mutual():
    inp1 = input('введите id пользователя:')

    params = {
        'v': VERSION,
        'source_uid': 1410393,
        'target_uid': inp1,
        'access_token': token
    }

    response = requests.get('https://api.vk.com/method/friends.getMutual', params)
    response = response.json()['response']

    for id in response:
        print('id общего друга:', id)
        print('ссылка на страницу: https://vk.com/id', id, sep='')


get_mutual()
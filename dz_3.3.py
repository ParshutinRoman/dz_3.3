from urllib.parse import urlencode
import requests

APP_ID = 7029454
AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
VERSION = '5.95'
userID1 = 1410393
userID2 = 6471123

auth_params = {
    'client_id': APP_ID,
    'redirect_uri': 'https://oauth.vk.com/blank.html',
    'display': 'popup',
    'scope': 'friends,status,video',
    'response_type': 'token',
}

token_link = '?'.join((AUTHORIZE_URL, urlencode(auth_params)))
print(token_link)

token = '73e64e811349b00ae127a08ac05454fb2b4d5384b2ce955285e19398a18caccd6b8185402f0ceb965bb95'


class User():
    def __init__(self, id, token):
        self.id = id
        self.token = token

    def __and__(self, other_user):
        self.other_user = other_user

        params = {
            'v': VERSION,
            'source_uid': self,
            'target_uid': other_user,
            'access_token': token
        }

        response = requests.get('https://api.vk.com/method/friends.getMutual', params)
        response = response.json()#['response']
        print(response)


user1 = User(userID1, token)
user2 = User(userID2, token)


mutal_user_list = user1 & user2
print(mutal_user_list)


from urllib.parse import urlencode
import requests

APP_ID = 6471121
AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
VERSION = '5.95'
userID1 = 6471121
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

token = '2eb0e9c5198797503fa6fb0c9f5d6e63423e738478b4c9c3e24c2f00964f04f57f8b3870acf6afd3cd0a9'

class User():
    def __init__(self, token):
        self.token = global token

    def __and__(self, other_user):
        self.other_user = other_user


        inp2 = input('введите id пользователя:')

        params = {
            'v': VERSION,
            'source_uid': 6471121,
            'target_uid': inp2,
            'access_token': token
        }

        response = requests.get('https://api.vk.com/method/friends.getMutual', params)
        response = response.json()['response']

        for id in response:
            print('id общего друга:', id)
            print('ссылка на страницу: https://vk.com/id', id, sep='')




# user1 = User(user_id_1)
# user2 = User(user_id_2)
# #создали пользователей
#
# mutal_user_list = user1 & user2
# print(mutal_user_list)


# class User:
#     __and__(self, other_user):
#     # other_user - это другой экземпляр класса user
#     # далее идет логика получения общего списка друзей
#     return mutal_user_lust
#
# # теперь при применении оператора & к экземпляру класса User будет неявно вызываться метод __and__. Т.е вызвали user1 & user2, а фактически где то под капотом питона вызвалось user1.__and__(user2)

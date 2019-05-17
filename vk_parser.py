import requests

token = 'b5bc7a56b5bc7a56b5bc7a5664b5d6e5a7bb5bcb5bc7a56e9628524184d9adee598ff51'
version = 5.95
domain = 'science_technology'

BASE_URL = 'https://api.vk.com/method/'
method = 'wall.get'

url_initial = BASE_URL + method

response = requests.get(url_initial, params={
'access_token': token,
'v': version,
})
print(response)
# data = response.json()

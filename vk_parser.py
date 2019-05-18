import requests
resp = requests.get('https://www.avito.ru/rossiya/audio_i_video/mp3-pleery?s_trg=11')
print(resp.json())

# from httmock import urlmatch, HTTMock
# import requests
# import sys
# sys.stdout.buffer.write('Çàâîäñêàÿ'.encode(sys.stdout.encoding) + b'\n')
#
# token = 'b5bc7a56b5bc7a56b5bc7a5664b5d6e5a7bb5bcb5bc7a56e9628524184d9adee598ff51'
# version = 5.95
# domain = 'science_technology'
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',}
#
#
#
# BASE_URL = 'https://api.vk.com/method/'
# method = 'wall.get'
#
# url_initial = BASE_URL + method
#
# r = requests.get('https://www.avito.ru/rossiya/audio_i_video/mp3-pleery?s_trg=11')
# d = r.json()
# print(d)
# # response = requests.get('https://api.vk.com/method/wall.get?access_token=b5bc7a56b5bc7a56b5bc7a5664b5d6e5a7bb5bcb5bc7a56e9628524184d9adee598ff51&v=5.95&domain=science_technology')
# #
# # data = response.json()

import requests
from bs4 import BeautifulSoup

from random import choice
from time import sleep

import parser_proxy as pp

def main():
    token = 'b5bc7a56b5bc7a56b5bc7a5664b5d6e5a7bb5bcb5bc7a56e9628524184d9adee598ff51'
    version = 5.95
    domain = 'science_technology'

    BASE_URL = 'https://api.vk.com/method/'
    method = 'wall.get'

    # url = BASE_URL+method
    # url = 'https://api.vk.com/method/wall.get'
    # html = requests.get(url, params={
    # 'access_token': token,
    # 'v': version,
    # 'domain': domain
    # }, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'}, proxies={'https': 'http://217.113.122.142:3128'})

    url = 'https://toster.ru/q/190303'
    html = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'}, proxies={'http': 'http://217.113.122.142:3128'})

    print(html)

if __name__ == '__main__':
    main()

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

#
# url_initial = BASE_URL + method
#
# r = requests.get('https://www.avito.ru/rossiya/audio_i_video/mp3-pleery?s_trg=11')
# d = r.json()
# print(d)
# # response = requests.get('https://api.vk.com/method/wall.get?access_token=b5bc7a56b5bc7a56b5bc7a5664b5d6e5a7bb5bcb5bc7a56e9628524184d9adee598ff51&v=5.95&domain=science_technology')
# #
# # data = response.json()

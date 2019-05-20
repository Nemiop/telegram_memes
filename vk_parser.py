import requests
from bs4 import BeautifulSoup
import json
import parser_proxy as pp

def write_file(data):
    f = open('vk_html.txt', 'w')
    f.write(data)
    f.close()


def take_1000_posts(vk_group):
    # General Information about method and Vk_API
    token = 'b5bc7a56b5bc7a56b5bc7a5664b5d6e5a7bb5bcb5bc7a56e9628524184d9adee598ff51'
    version = 5.95
    params={
        'access_token': token,
        'v': version,
        'domain': vk_group,
        'count': 100
    }

    BASE_URL = 'https://api.vk.com/method/'
    method = 'wall.get'
    url = BASE_URL+method

    offset = 0
    all_posts = []

    while offset < 1000:
        params.update({'offset': offset})
        # Avoid block Vk.com in Ukraine
        html = pp.get_html_proxy(url, params)
        data = html.json()['response']['items']
        all_posts.extend(data)

        offset+=100

    return all_posts


def main():
    vk_group = 'mhkon'

    vk_posts = take_1000_posts(vk_group)
    # soup = BeautifulSoup()
    write_file(json.dumps(vk_posts, sort_keys=True, indent=1, separators=(',', ': ')))



if __name__ == '__main__':
    main()

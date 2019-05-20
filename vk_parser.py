import requests
import csv

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
    post_number = 100
    offset = 0

    all_posts = []
    BASE_URL = 'https://api.vk.com/method/'
    method = 'wall.get'
    url = BASE_URL+method

    params={
        'access_token': token,
        'v': version,
        'domain': vk_group,
        'count': post_number,
        'offset': offset
    }

    while offset < 1000:
        params.update({'offset': offset})
        # Avoid block Vk.com in Ukraine
        html = pp.get_html_proxy(url, params)
        data = html.json()['response']['items']
        all_posts.extend(data)

        offset+=100

    return all_posts

def file_writer(posts):
    with open('vk_mhk.csv', 'w', encoding='UTF-8') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('likes', 'body', 'url_photo'))

        for post in posts:
            post_likes = post['likes']['count']
            post_text = post['text']
            try:
                if post['attachments'][0]['type']:
                    img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
            except:
                img_url = 'NaN'

            a_pen.writerow((post_likes, post_text, img_url))



def main():
    vk_group = 'mhkon'

    vk_posts = take_1000_posts(vk_group)
    file_writer(vk_posts)
#    write_file(json.dumps(vk_posts, sort_keys=True, indent=1, separators=(',', ': ')))



if __name__ == '__main__':
    main()

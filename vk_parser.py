import requests
from bs4 import BeautifulSoup

import parser_proxy as pp

def main():
    # General informatoin.
    # URL parameters
    token = 'b5bc7a56b5bc7a56b5bc7a5664b5d6e5a7bb5bcb5bc7a56e9628524184d9adee598ff51'
    version = 5.95
    domain = 'science_technology'
    params={
        'access_token': token,
        'v': version,
        'domain': domain
    }

    BASE_URL = 'https://api.vk.com/method/'
    method = 'wall.get'
    url = BASE_URL+method
    # Avoid block Vk.com in Ukraine
    html = pp.get_html_proxy(url,params)

    print(html.json())




if __name__ == '__main__':
    main()

# Use dynamic changing Ip and Useragent

import requests

from random import choice
from time import sleep

def get_html(url, parameters, useragent=None, proxy=None):
    r = requests.get(url, params=parameters, headers=useragent, proxies=proxy)
    return r


def get_html_proxy(url, parameters):

    # Proxy - change ip and user-agent
    # Govnokod: Last element is ' ', so I delete it

    useragents = open('u_agents_list.txt').read().split('\n')
    useragents.pop()

    proxies = open('proxy_list.txt').read().split('\n')
    proxies.pop()

    for i in range(10):
#        sleep(uniform(3,6))                                 # Delay 'antiban'. Isn't needed if multi-ip
        proxy = {'https':  choice(proxies)}
        useragent = {'User-Agent': choice(useragents)}
        try:
            html = get_html(url, parameters, useragent, proxy)
        except:
            continue
        return html

import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse


def shorten_link(token, user_input, version):
    url = 'https://api.vk.com/method/utils.getShortLink'
    payload = {
        'url': user_input,
        'access_token': token,
        'v': version
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()
    short_link = response.json()
    return short_link['response']['short_url']
    

def count_clicks(token, version, key):
    url = 'https://api.vk.com/method/utils.getLinkStats'
    payload = {
        'access_token': token,
        'v': version,
        'key': key,
        'interval': 'forever'
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()
    link_stats = response.json()
    return link_stats['response']['stats']
    

def is_shorten_link(token, user_input, version):
    parsed_url = urlparse(user_input)
    if not all([parsed_url.scheme, parsed_url.netloc]):
        return False

    key = user_input.split('/')[-1]

    url = 'https://api.vk.com/method/utils.getLinkStats'
    payload = {
        'access_token': token,
        'v': version,
        'key': key,
        'interval': 'forever'
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()
    link_stats = response.json()
    return 'response' in link_stats and 'stats' in link_stats['response']
    
   
def main():
    load_dotenv()
    token = os.environ['VK_TOKEN']
    version = '5.199'

    parser = argparse.ArgumentParser(description='Сокращение ссылок и получение статистики по ним.')
    parser.add_argument('url', type=str, help='Введите ссылку для сокращения или статистики')
    args = parser.parse_args()

    user_input = args.url
    
    try:
        if is_shorten_link(token, user_input, version):
            key = user_input.split('/')[-1]
            stats = count_clicks(token, version, key)
            views=stats[0]['views']
            print(f'По вашей  ссылке  перешли {views} раз')
        else:
            shortened_link = shorten_link(token, user_input, version)
            print('Сокращенная ссылка:', shortened_link)
        
    except requests.exceptions.HTTPError as e:
        print(f"Ошибка HTTP: {e}")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка сетевого запроса: {e}")
    except KeyError as e:
        print(f"Ошибка: отсутствует необходимый ключ в ответе API: {e}")
    
  
if __name__ == "__main__":
    main()






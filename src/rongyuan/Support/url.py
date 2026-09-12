import requests
import os
import sys
merge = os.path.join
MY_DIR = os.path.dirname(os.path.abspath(__file__))
def check_url_exists(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def get_urls(url_file = merge(MY_DIR, 'URL')):
    with open(url_file, 'r') as file:
        urls = file.readlines()
    return [url.strip() for url in urls]
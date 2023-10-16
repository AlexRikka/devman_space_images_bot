import requests
import os
import urllib.parse


def download_image(link, path, payload=None):
    response_image = requests.get(link, params=payload)
    response_image.raise_for_status()
    with open(path, 'wb') as f:
        f.write(response_image.content)


def get_file_extention(url):
    file_path = urllib.parse.urlsplit(url).path
    return os.path.splitext(file_path)[1]

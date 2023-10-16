import requests
import os
from dotenv import load_dotenv
from image_downloader import download_image, get_file_extention


def fetch_nasa_apod(link, path, api_key):
    if not os.path.exists(path):
        os.makedirs(path)
    payload = {'api_key': api_key,  'count': 30}
    response = requests.get(url=link, params=payload)
    response.raise_for_status()
    response_list = response.json()
    for idx, response_idx in enumerate(response_list):
        image_link = response_idx['url']
        print(image_link)
        image_extension = get_file_extention(image_link)
        download_image(image_link, path+f'nasa_apod_{idx}{image_extension}')


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    path = 'images/'
    link = 'https://api.nasa.gov/planetary/apod'
    fetch_nasa_apod(link, path, nasa_api_key)

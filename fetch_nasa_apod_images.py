import requests
import os
from dotenv import load_dotenv
from image_downloader import download_image, get_file_extention


def fetch_nasa_apod(path):
    if not os.path.exists(path):
        os.makedirs(path)
    api_key = os.environ['NASA_API_KEY']
    link = 'https://api.nasa.gov/planetary/apod'
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
    path = 'images/'
    fetch_nasa_apod(path)

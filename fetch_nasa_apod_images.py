import requests
import os
from dotenv import load_dotenv
from image_downloader import download_image, get_file_extention


def fetch_nasa_apod(path, images_count):
    os.makedirs(path, exist_ok=True)
    api_key = os.environ['NASA_API_KEY']
    link = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': api_key,  'count': images_count}
    response = requests.get(url=link, params=payload)
    response.raise_for_status()
    responses = response.json()
    for idx, response_idx in enumerate(responses):
        image_link = response_idx['url']
        image_extension = get_file_extention(image_link)
        download_image(image_link, f'{path}nasa_apod_{idx}{image_extension}')


if __name__ == '__main__':
    load_dotenv()
    path = 'images/'
    images_count = 30
    fetch_nasa_apod(path, images_count)

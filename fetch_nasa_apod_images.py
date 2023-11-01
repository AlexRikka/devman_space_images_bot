import requests
import os
from dotenv import load_dotenv
from image_downloader import download_image, get_file_extention


def fetch_nasa_apod(path, images_count, nasa_token):
    os.makedirs(path, exist_ok=True)
    link = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': nasa_token,  'count': images_count}
    response = requests.get(url=link, params=payload)
    response.raise_for_status()
    responses = response.json()
    for idx, response_idx in enumerate(responses):
        image_link = response_idx['url']
        image_extension = get_file_extention(image_link)
        download_image(image_link, f'{path}nasa_apod_{idx}{image_extension}')


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ['NASA_API_KEY']
    path = 'images/'
    images_count = 30
    fetch_nasa_apod(path, images_count, nasa_token)

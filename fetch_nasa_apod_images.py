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
    response_images = response.json()
    for image_idx, image_payload in enumerate(response_images):
        image_link = image_payload['url']
        image_extension = get_file_extention(image_link)
        download_image(image_link,
                       f'{path}nasa_apod_{image_idx}{image_extension}')


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ['NASA_API_KEY']
    path = 'images/'
    images_count = 30
    fetch_nasa_apod(path, images_count, nasa_token)

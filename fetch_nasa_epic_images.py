import requests
import os
from dotenv import load_dotenv
from image_downloader import download_image, get_file_extention


def fetch_nasa_epic(path, nasa_token):
    os.makedirs(path, exist_ok=True)
    payload = {'api_key': nasa_token}
    response = requests.get('https://api.nasa.gov/EPIC/api/natural/all',
                            params=payload)
    last_image_date = response.json()[0]['date']
    last_image_date_formatted = last_image_date.replace('-', '/')
    response = requests.get(f'https://api.nasa.gov/EPIC/api/natural/'
                            f'date/{last_image_date}',
                            params=payload)
    response_images = response.json()
    for image_idx, image_payload in enumerate(response_images):
        image_identifier = image_payload['image']
        image_link = f'https://api.nasa.gov/EPIC/archive/natural/'\
            f'{last_image_date_formatted}/png/{image_identifier}.png'
        image_extension = get_file_extention(image_link)
        download_image(image_link,
                       f'{path}nasa_epic_{image_idx}{image_extension}',
                       payload)


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ['NASA_API_KEY']
    path = 'images/'
    fetch_nasa_epic(path, nasa_token)

import requests
import os
from dotenv import load_dotenv
from image_downloader import download_image, get_file_extention


def fetch_nasa_epic(path):
    os.makedirs(path, exist_ok=True)
    payload = {'api_key': nasa_token}
    response = requests.get('https://api.nasa.gov/EPIC/api/natural/all',
                            params=payload)
    date = response.json()[0]['date']
    date_fromatted = response.json()[0]['date'].replace('-', '/')
    response = requests.get(f'https://api.nasa.gov/EPIC/api/natural/'
                            f'date/{date}',
                            params=payload)
    responses = response.json()
    for idx, response_idx in enumerate(responses):
        image_identifier = response_idx['image']
        image_link = f'https://api.nasa.gov/EPIC/archive/natural/'\
            f'{date_fromatted}/png/{image_identifier}.png'
        image_extension = get_file_extention(image_link)
        download_image(image_link, f'{path}nasa_epic_{idx}{image_extension}',
                       payload)


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ['NASA_API_KEY']
    path = 'images/'
    fetch_nasa_epic(path)

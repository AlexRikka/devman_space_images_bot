import requests
import os
from dotenv import load_dotenv
from image_downloader import download_image, get_file_extention


def fetch_nasa_epic(path, api_key):
    if not os.path.exists(path):
        os.makedirs(path)
    payload = {'api_key': api_key}
    response = requests.get('https://api.nasa.gov/EPIC/api/natural/all',
                            params=payload)
    date = response.json()[0]['date']
    date_fromatted = response.json()[0]['date'].replace('-', '/')
    response = requests.get(f'https://api.nasa.gov/EPIC/api/natural/'
                            f'date/{date}',
                            params=payload)
    response_list = response.json()
    for idx, response_idx in enumerate(response_list):
        image_identifier = response_idx['image']
        image_link = f'https://api.nasa.gov/EPIC/archive/natural/'\
            f'{date_fromatted}/png/{image_identifier}.png'
        image_extension = get_file_extention(image_link)
        download_image(image_link, path+f'nasa_epic_{idx}{image_extension}',
                       payload)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    path = 'images/'
    fetch_nasa_epic(path, nasa_api_key)

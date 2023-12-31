import requests
import os
import argparse
from image_downloader import download_image, get_file_extention


def fetch_spacex_last_launch(launch_id, path):
    os.makedirs(path, exist_ok=True)
    link = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(link)
    response.raise_for_status()
    images = response.json()['links']['flickr']['original']
    for idx, image_link in enumerate(images):
        image_extension = get_file_extention(image_link)
        download_image(image_link, f'{path}spacex_{idx}{image_extension}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download images of ' +
                                     'SpaceX rockets from their website')
    parser.add_argument('launch_id',
                        help='launch ID',
                        nargs='?',
                        default='latest')
    launch_id = parser.parse_args().launch_id
    path = 'images/'
    fetch_spacex_last_launch(launch_id, path)

import requests
import os
import argparse
from image_downloader import download_image, get_file_extention


def fetch_spacex_last_launch(link, path):
    if not os.path.exists(path):
        os.makedirs(path)
    response = requests.get(link)
    response.raise_for_status()
    images = response.json()['links']['flickr']['original']
    for image_idx, image_link in enumerate(images):
        image_extension = get_file_extention(image_link)
        download_image(image_link, path+f'spacex_{image_idx}{image_extension}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('launch_id',
                        help='ID запуска',
                        nargs='?',
                        default='latest')
    launch_id = parser.parse_args().launch_id
    print(launch_id)
    link = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    path = 'images/'
    fetch_spacex_last_launch(link, path)

import telegram
import time
import random
import argparse
import os
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    telegram_api_key = os.environ['TG_BOT_HTTP_KEY']
    bot = telegram.Bot(token=telegram_api_key)
    chat_id = os.environ['TG_CHANNEL_NAME']

    parser = argparse.ArgumentParser(description='Publishes space images ' +
                                     'in the telegram channel.')
    parser.add_argument('post_delay',
                        help='Posting frequency in hours',
                        type=float,
                        nargs='?',
                        default=4)
    post_delay = parser.parse_args().post_delay
    image_paths = []
    for address, dirs, files in os.walk(r'images/'):
        image_paths.extend([os.path.join(address, name) for name in files])

    max_image_size = 20*1024*1024
    sec_per_hour = 3600
    while True:
        for image_path in image_paths:
            if not os.path.isfile(image_path):
                continue
            if os.path.getsize(image_path) > max_image_size:
                continue
            with open(image_path, 'rb') as f:
                bot.send_document(chat_id=chat_id, document=f)
            time.sleep(sec_per_hour*post_delay)
        random.shuffle(image_paths)

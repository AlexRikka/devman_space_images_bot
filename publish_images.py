import telegram
import time
import argparse
import os
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    telegram_api_key = os.environ['TELEGRAM_API_KEY']
    bot = telegram.Bot(token=telegram_api_key)
    chat_id = os.environ['CHANNEL_NAME']

    parser = argparse.ArgumentParser()
    parser.add_argument('post_delay',
                        help='Частота публикации в часах',
                        nargs='?',
                        default=4)
    post_delay = parser.parse_args().post_delay

    while True:
        for address, dirs, files in os.walk(r'images/'):
            for name in files:
                image_path = os.path.join(address, name)
                if not os.path.isfile(image_path):
                    continue
                if os.path.getsize(image_path)/1024**2 > 20:
                    continue
                bot.send_document(
                    chat_id=chat_id, document=open(image_path,
                                                   'rb'))
                time.sleep(3600*post_delay)

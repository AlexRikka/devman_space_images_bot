import telegram
import argparse
import os
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    telegram_api_key = os.environ['TELEGRAM_API_KEY']
    bot = telegram.Bot(token=telegram_api_key)
    chat_id = os.environ['CHANNEL_NAME']

    parser = argparse.ArgumentParser(description='Publishes given image ' +
                                     'in the telegram channel.')
    parser.add_argument('image_path',
                        help='Path to image')
    image_path = parser.parse_args().image_path
    bot.send_document(chat_id=chat_id, document=open(image_path, 'rb'))

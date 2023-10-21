import telegram
import os
from dotenv import load_dotenv
load_dotenv()
telegram_api_key = os.environ['TELEGRAM_API_KEY']
bot = telegram.Bot(token=telegram_api_key)
chat_id = '@jjspaceimages'
bot.send_document(chat_id=chat_id, document=open(r'images\spacex_0.jpg', 'rb'))

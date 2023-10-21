import telegram
import os
from dotenv import load_dotenv
load_dotenv()
telegram_api_key = os.environ['TELEGRAM_API_KEY']
bot = telegram.Bot(token=telegram_api_key)

bot.send_message(text='Hello!', chat_id='@jjspaceimages')

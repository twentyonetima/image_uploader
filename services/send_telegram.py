import time
import telebot
from django.conf import settings

bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)

def send_telegram_message(chat_id: str, message: str, retries: int = 3, delay: float = 1.0):
    for attempt in range(1, retries + 1):
        try:
            bot.send_message(chat_id, message)
            return
        except Exception as e:
            print(f"[Попытка {attempt}] Ошибка при отправке в Telegram: {e}")
            if attempt < retries:
                time.sleep(delay)
                delay *= 2
            else:
                print("Все попытки отправки сообщения исчерпаны.")
import os

import telegram

from dotenv import load_dotenv
load_dotenv()


def main():
    tele_key = os.environ.get('TELEGRAM_KEY')

    bot = telegram.Bot(token=tele_key)

    chat_id = '@cosmo_sp'

    bot.send_message(chat_id=chat_id, text="suck cock please")


if __name__ == '__main__':
    main()
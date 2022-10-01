import os
import argparse

from time import sleep
from random import shuffle

import telegram

from dotenv import load_dotenv
load_dotenv()


def get_user_args():

    sleep_time = os.environ.get('SLEEP_TIME')

    parser = argparse.ArgumentParser(
        description='Delay time for sending messages'
    )
    parser.add_argument('--sleep_time', default=sleep_time, type=int,
        help='Delay time'
    )

    args = parser.parse_args()

    return args


def main():
    args = get_user_args()

    while True:
        images = os.listdir(path="images/")

        shuffle(images)

        telegram_token = os.environ.get('TELEGRAM_TOKEN')
        telegram_chat_id = os.environ.get('TELEGRAM_CHAT_ID')

        bot = telegram.Bot(token=telegram_token)
        
        for image in images:

            bot.send_document(chat_id=telegram_chat_id, 
                document=open(f'images/{image}', 'rb')
                )

            sleep(args.sleep_time)


if __name__ == '__main__':
    main()
import os
import argparse

from time import sleep
from random import shuffle

import telegram

from dotenv import load_dotenv
load_dotenv()


SLEEP_TIME = 14400


def get_user_args():
    parser = argparse.ArgumentParser(
        description='Delay time for sending messages and choosing a photo'
    )
    parser.add_argument('--image', default=None, help='photo to post')

    args = parser.parse_args()

    return args


def main():
    args = get_user_args()

    while True:
        images = os.listdir(path="images/")

        shuffle(images)

        telegram_token = os.environ['TELEGRAM_TOKEN']
        telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']

        bot = telegram.Bot(token=telegram_token)

        if args.image:
            post_image = args.image

        else:
            for image in images:
                post_image = image

        bot.send_document(
            chat_id=telegram_chat_id,
            document=open(f'images/{post_image}', 'rb')
        )

        sleep(SLEEP_TIME)


if __name__ == '__main__':
    main()

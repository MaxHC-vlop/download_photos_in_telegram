import os
import argparse

from time import sleep
from random import shuffle

import telegram

from dotenv import load_dotenv
load_dotenv()


SLEEP_TIME = 3


def get_user_args():
    parser = argparse.ArgumentParser(
        description='Delay time for sending messages and choosing a photo'
    )
    parser.add_argument('--image', default=None, help='photo to post')

    args = parser.parse_args()

    return args


def main():
    args = get_user_args()

    images_folder = os.path.join('images')

    os.makedirs(images_folder, exist_ok=True)

    images = os.listdir(path=images_folder)

    shuffle(images)

    telegram_token = os.environ['TELEGRAM_TOKEN']

    telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']

    bot = telegram.Bot(token=telegram_token)

    for image in images:
        img = os.path.join('images', image)

        with open(img, 'rb') as file:
            bot.send_document(
                chat_id=telegram_chat_id,
                document=file
            )

            sleep(SLEEP_TIME)


if __name__ == '__main__':
    main()

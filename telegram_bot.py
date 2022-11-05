import os
import argparse
import logging

from time import sleep
from random import shuffle, choice

import telegram

from dotenv import load_dotenv


SLEEP_TIME = 14400


def get_user_args():
    parser = argparse.ArgumentParser(
        description='Upload photos from nasa and spacex to telegram channel'
    )
    parser.add_argument(
        '-a', '--all_images', action=argparse.BooleanOptionalAction, help='Submit all images'
        )
    parser.add_argument(
        '-o','--one_image', action=argparse.BooleanOptionalAction, help='Submit one image'
        )
    parser.add_argument(
        '-i','--image', default=None, help='Photo to post'
        )

    args = parser.parse_args()

    return args


def send_file(bot, chat_id, image_folder):
    with open(image_folder, 'rb') as file:
        bot.send_document(chat_id, file)


def main():
    args = get_user_args()

    images_folder = os.path.join('images')

    os.makedirs(images_folder, exist_ok=True)

    images = os.listdir(path=images_folder)

    shuffle(images)

    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']

    telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']


    bot = telegram.Bot(token=telegram_token)

    if args.one_image:
        image = os.path.join('images', choice(images))

        if args.image:
            image = os.path.join('images', args.image)

        send_file(bot, telegram_chat_id, image)

    if args.all_images:
        while True:
            try:
                for image in images:
                    image_folder = os.path.join('images', image)
                    send_file(bot, telegram_chat_id, image_folder)
                    sleep(SLEEP_TIME)

            except telegram.error.NetworkError as errn:
                logging.error(f'NetworkError: {errn}')
                sleep(10)
                continue

if __name__ == '__main__':
    main()

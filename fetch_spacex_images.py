import argparse
import os

from urllib.parse import urljoin

from download_image import get_file_format, download_image

import requests


SPACEX_URL = 'https://api.spacexdata.com/v5/launches/'


def get_user_args():
    parser = argparse.ArgumentParser(
        description='Download spacex image'
    )
    parser.add_argument(
        '--spacex_id', default='5eb87d47ffd86e000604b38a',
        help='ID spacex API'
    )

    args = parser.parse_args()

    return args


def main():
    images_folder = os.path.join(
        'images',
        )

    os.makedirs(images_folder, exist_ok=True)

    args = get_user_args()

    response = requests.get(SPACEX_URL)
    response.raise_for_status()

    spacex_id = args.spacex_id

    spacex_url = urljoin(SPACEX_URL, spacex_id)

    response = requests.get(spacex_url)
    response.raise_for_status()

    spacex_links = response.json()['links']['flickr']['original']

    for number, link in enumerate(spacex_links):
        response = requests.get(link)
        response.raise_for_status()

        extension = get_file_format(response.url)

        filename = f'{images_folder}{os.sep}spacex_{number}{extension}'
        download_image(link, filename)


if __name__ == '__main__':
    main()

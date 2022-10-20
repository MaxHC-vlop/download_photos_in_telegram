import os
import argparse

from download_image import get_file_format, download_image

import requests

from dotenv import load_dotenv


NASA_URL = 'https://api.nasa.gov/planetary/apod/'


def get_user_args():
    parser = argparse.ArgumentParser(
        description='Download nasa images'
    )
    parser.add_argument(
        '--count', default=1,
        help='Count images',
        type=int
    )

    args = parser.parse_args()

    return args


def main():
    images_folder = os.path.join(
        'images',
        )

    os.makedirs(images_folder, exist_ok=True)

    load_dotenv()
    nasa_key = os.environ['NASA_TOKEN']

    args = get_user_args()

    payload = {
        'api_key': nasa_key,
        'count': args.count
    }

    response = requests.get(NASA_URL, params=payload)
    response.raise_for_status()

    nasa_links = []

    for link in response.json():
        media_type = 'image'
        if link['media_type'] == media_type:
            nasa_links.append(link['url'])

    for number, link in enumerate(nasa_links):
        response = requests.get(link)
        response.raise_for_status()

        extension = get_file_format(response.url)

        if extension:
            filename = f'{images_folder}{os.sep}nasa_{number}{extension}'
            download_image(link, filename)


if __name__ == '__main__':
    main()

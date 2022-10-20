import os

from datetime import datetime
from urllib.parse import urljoin

from download_image import download_image

import requests

from dotenv import load_dotenv


EPIC_NASA_URL = 'https://api.nasa.gov/EPIC/api/natural/'

EPIC_ARCHIVE_URL = 'https://api.nasa.gov/EPIC/archive/natural/'


def main():
    images_folder = os.path.join(
        'images',
        )

    os.makedirs(images_folder, exist_ok=True)

    load_dotenv()
    nasa_key = os.environ['NASA_TOKEN']

    payload = {
        'api_key': nasa_key
    }

    response = requests.get(EPIC_NASA_URL, params=payload)
    response.raise_for_status()

    for number, image_content in enumerate(response.json()):
        image_date = datetime.strptime(image_content["date"],
                                       "%Y-%m-%d %H:%M:%S")
        image_url = image_content['image']

        image_url = (
            f'{image_date.strftime("%Y/%m/%d")}/png/'
            f'{image_url}.png'
        )

        link = urljoin(EPIC_ARCHIVE_URL, image_url)

        filename = f'{images_folder}{os.sep}epic_nasa_{number}.png'
        download_image(link, filename, payload)


if __name__ == '__main__':
    main()

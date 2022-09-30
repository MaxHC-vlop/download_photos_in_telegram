import os

from download_image import get_file_format, download_image

import requests

from dotenv import load_dotenv


NASA_URL = 'https://api.nasa.gov/planetary/apod/'


def main():
    images_folder = os.path.join(
        'images',
        )

    os.makedirs(images_folder, exist_ok=True)

    load_dotenv()
    nasa_key = os.environ.get('NASA_KEY')

    payload = {
        'api_key': nasa_key,
        'count': 30
    }

    response = requests.get(NASA_URL, params=payload)
    response.raise_for_status()

    nasa_links = [link['url'] for link in response.json()]

    for number, link in enumerate(nasa_links):
        response = requests.get(link)
        response.raise_for_status()

        extension = get_file_format(response.url)

        if extension:
            filename = f'{images_folder}{os.sep}nasa_{number}{extension}'
            download_image(link, filename)


if __name__ == '__main__':
    main()

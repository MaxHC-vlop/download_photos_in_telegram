import os
from datetime import datetime
from sys import prefix

from urllib.parse import urlsplit, urljoin

import requests

from dotenv import load_dotenv


SPACEX_URL = 'https://api.spacexdata.com/v5/launches/'

NASA_URL = 'https://api.nasa.gov/planetary/apod/'

EPIC_NASA_URL = 'https://api.nasa.gov/EPIC/api/natural/'

QQQ = 'https://api.nasa.gov/EPIC/archive/natural/'


def download_spacex_image(url, filename):
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def download_nasa_image(url, filename):
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def download_epic_nasa_image(url, payload, filename):
    response = requests.get(url, params=payload)
    response.raise_for_status()

    prefix = get_split(response.url)

    filename += prefix

    with open(filename, 'wb') as file:
            file.write(response.content)


def get_split(url):
    url = urlsplit(url)
    image_folder, image_name = os.path.split(url.path)
    image, image_extension = os.path.splitext(image_name)
    
    return image_extension


def main():
    images_folder = os.path.join(
        'images',
        )

    os.makedirs(images_folder, exist_ok=True)

    response = requests.get(SPACEX_URL)
    response.raise_for_status()

    spacex_id = '5eb87d47ffd86e000604b38a'  # response.json()[0]['id']

    spacex_url = urljoin(SPACEX_URL, spacex_id)

    response = requests.get(spacex_url)
    response.raise_for_status()

    spacex_links = response.json()['links']['flickr']['original']

    for number, link in enumerate(spacex_links):
        response = requests.get(link)
        response.raise_for_status()

        extension = get_split(response.url)

        filename = f'{images_folder}{os.sep}spacex_{number}{extension}'
        download_spacex_image(link, filename)

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

        extension = get_split(response.url)

        if extension:
            filename = f'{images_folder}{os.sep}nasa_{number}{extension}'
            download_nasa_image(link, filename)

    payload = {
        'api_key': nasa_key,
        'count': 5
    }

    response = requests.get(EPIC_NASA_URL, params=payload)
    response.raise_for_status()

    for number, image_content in enumerate(response.json()):
        image_date = datetime.strptime(image_content["date"], "%Y-%m-%d %H:%M:%S")
        image_url = image_content['image']

        image_url = (
            f'{image_date.strftime("%Y/%m/%d")}/png/'
            f'{image_url}.png'
        )

        link = urljoin(QQQ, image_url)

        filename = f'{images_folder}{os.sep}epic_nasa_{number}'
        download_epic_nasa_image(link, payload, filename)


if __name__ == '__main__':
    main()

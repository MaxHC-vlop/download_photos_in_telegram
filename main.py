import os
from urllib import response

import requests

from dotenv import load_dotenv



URL = 'https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384'


def download_spacex_image(url, folder):
    response = requests.get(url)
    response.raise_for_status()
    with open(folder, 'wb') as file:
        file.write(response.content)


def download_nasa_image(url, folder, payload):
    response = requests.get(url, params=payload)
    response.raise_for_status()

    response = requests.get(response.json()['url'])
    response.raise_for_status()
    with open(folder, 'wb') as file:
        file.write(response.content)


def main():
    books_folder = os.path.join(
        'images',
        )

    os.makedirs(books_folder, exist_ok=True)

    response = requests.get(URL)
    response.raise_for_status()

    links = response.json()['links']['flickr']['original']
    image_count = 1

    load_dotenv()
    nasa_key = os.environ.get('NASA_KEY')
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': nasa_key
    }

    filename = f'{books_folder}{os.sep}nasa.jpeg'

    download_nasa_image(nasa_url, filename, payload)

    # for link in links:

    #     filename = f'{books_folder}{os.sep}spacex_{image_count}.jpeg'
    #     download_spacex_image(link, filename)

    #     image_count += 1


if __name__ == '__main__':
    main()
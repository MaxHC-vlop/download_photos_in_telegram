import os
from urllib.parse import urlsplit

import requests

from dotenv import load_dotenv



URL = 'https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384'


def download_spacex_image(url, folder):
    response = requests.get(url)
    response.raise_for_status()
    with open(folder, 'wb') as file:
        file.write(response.content)


def download_nasa_image(books_folder, url, payload):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    
    x = 1

    for i in response.json():

        response = requests.get(i['url'])
        get_split(response.url)
        response.raise_for_status()
        extension = get_split(response.url)

        print(i['url'])

        filename = f'{books_folder}{os.sep}nasa{x}{extension}'

        with open(filename, 'wb') as file:
            file.write(response.content)

        x += 1

def get_split(url):
    url = urlsplit(url)
    image_folder, image_name = os.path.split(url.path)
    image, image_extension = os.path.splitext(image_name)
    print(image_extension)
    
    return image_extension


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
        'api_key': nasa_key,
        'count': 30
    }
    download_nasa_image(books_folder, nasa_url, payload)

    for link in links:
        response = requests.get(link)
        response.raise_for_status()

        extension = get_split(response.url)

        filename = f'{books_folder}{os.sep}spacex_{image_count}{extension}'
        download_spacex_image(link, filename)

        image_count += 1


if __name__ == '__main__':
    main()
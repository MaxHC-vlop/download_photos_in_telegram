import os
import json

import requests




URL = 'https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384'


def download_image(url, folder):
    response = requests.get(url)
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
    for link in links:

        filename = f'{books_folder}{os.sep}spacex_{image_count}.jpeg'
        download_image(link, filename)

        image_count += 1


if __name__ == '__main__':
    main()
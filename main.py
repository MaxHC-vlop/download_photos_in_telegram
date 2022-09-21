import os

import requests


URL = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'


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

    filename = f'{books_folder}{os.sep}hubble.jpeg'

    download_image(URL, filename)


if __name__ == '__main__':
    main()
import os

import requests


URL = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'

def main():
    books_folder = os.path.join(
        'images',
        )

    filename = f'{books_folder}{os.sep}hubble.jpeg'

    print(books_folder)

    os.makedirs(books_folder, exist_ok=True)

    response = requests.get(URL)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    main()
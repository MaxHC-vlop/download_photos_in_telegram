import requests


URL = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
FILENAME = 'hubble.jpeg'

def main():
    response = requests.get(URL)
    response.raise_for_status()

    with open(FILENAME, 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    main()
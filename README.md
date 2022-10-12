# Download photos in telegram

Modules download space photos and upload them to Telegram.

## How to install

- Сlone this repository:
```bash
git@github.com:MaxHC-vlop/download_photos_in_telegram.git
```
 - Create a virtual environment on directory project:
 ```bash
python3 -m venv env
 ```
- Start the virtual environment:
```bash
. env/bin/activate
```
- Then use pip to install dependencies:
```bash
pip install -r requirements.txt
```
Create `API_TOKEN` variables in `.env` file given by [BotFather](https://t.me/BotFather) and [NASA](https://api.nasa.gov/) also provide telegram chat id:

```
NASA_TOKEN='super_secret'

TELEGRAM_TOKEN='super_secret'

TELEGRAM_CHAT_ID='your_chat_id (@your_chat)'
```

## Arguments
- telegram_bot.py:
  - `--image` - specify what picture to throw in the chat (default None)

- fetch_spacex_images.py
  - `--spacex_id` - specify run ID (default last run)

### Example
- Download pictures and post them in telegram chat :
```bash
# Download image spaceX
python3 fetch_spacex_images.py

# Post images chat
telegram_bot.py
```

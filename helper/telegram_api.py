import requests
import os
from dotenv import load_dotenv
load_dotenv()

Telegram_API_key = os.getenv('Telegram_API_key')

def sendMessage(sender_id = int, message= str ) -> None:
    url = f"https://api.telegram.org/bot{Telegram_API_key}/sendMessage"

    payload = {
        "chat_id": sender_id,
        "text": message
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Insomnia/2023.5.7"
    }

    requests.request("POST", url, json=payload, headers=headers)

    # response = requests.request("POST", url, json=payload, headers=headers)

def sendPhoto(sender_id:int, photo_url:str, caption:str=' ') -> None:
    url =  f"https://api.telegram.org/bot{Telegram_API_key}/sendPhoto"

    payload = {
        "chat_id": sender_id,
        "photo": photo_url,
        "caption": caption
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Insomnia/2023.5.7"
    }

    requests.request("POST", url, json=payload, headers=headers) 
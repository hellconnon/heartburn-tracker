import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.environ.get("API_URL")


def authenticate_telegram_id(telegram_id: int):
    response = requests.post(
        f"{API_URL}/auth/login_telegram",
        json={"telegram_id": telegram_id},
    )
    if response.status_code == 200:
        return response.json()
    else:
        return None


if __name__ == "__main__":
    auth_data = authenticate_telegram_id(42069)
    if auth_data:
        print(auth_data)
    else:
        print("Invalid Telegram ID")

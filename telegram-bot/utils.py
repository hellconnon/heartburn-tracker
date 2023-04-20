import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.environ.get("API_URL")


def authenticate_telegram_id(telegram_id: int):
    response = requests.post(
        f"{API_URL}/api/auth/login_telegram",
        json={"telegram_id": telegram_id},
    )
    return response.json()


if __name__ == "__main__":
    authenticate_telegram_id(42069)
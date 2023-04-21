import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.environ.get("API_URL")


def authenticate_telegram_id(telegram_id: int):
    """Authenticate a Telegram ID with the API
    :arg: telegram_id {int} -- Telegram ID to authenticate
    :return: {access_token, refresh_token, user_id} if successful, None otherwise
    """
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

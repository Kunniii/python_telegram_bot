from requests import get, post


class TelegramBot:
    _BOT_TOKEN: str
    _GROUP_ID: str
    _API: str

    def __init__(self, bot_token, group_id) -> None:
        self._BOT_TOKEN = bot_token
        self._GROUP_ID = group_id
        self._API = f"https://api.telegram.org/bot{self._BOT_TOKEN}"
        print("Bot initialized!")

    def send_message(self, message: str):
        url = self._API + "/sendMessage"
        json_body = {"chat_id": self._GROUP_ID, "text": message}
        print("Sending message....")
        return post(url, json=json_body).json()

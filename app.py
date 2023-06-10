import os
from TelegramBot import TelegramBot
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from requests import get, post

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
GROUP_ID = os.getenv("GROUP_ID")

bot = TelegramBot(API_TOKEN, GROUP_ID)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "OK"})


@app.route("/send_alert", methods=["POST"])
def send_alert():
    request_body: dict = request.json
    message = request_body.get("message")
    if message:
        return jsonify(bot.send_message(message))
    else:
        return jsonify({"ok": False, "message": "must have `message`"}), 400

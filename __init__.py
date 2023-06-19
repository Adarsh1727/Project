from telethon import TelegramClient

import logging

import time


api_id = "25058178"
api_hash = "131929c537e9d4914c045f0e01d5cda3"
bot_token = "5965355150:AAGRxhv6Rd2HDqov9yDY-gtmIG31OwHmJxQ"

bot = TelegramClient("aadi",api_id,api_hash).start(bot_token = bot_token)

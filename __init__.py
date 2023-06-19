from telethon import TelegramClient 
import telebot

import logging 
 
import time 
 
openai_key = "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"
 
api_id ="1125689"
api_hash ="4772d1792ed194020a8fb06a91ffb8fa"
bot_token ="5907130062:AAHtiF3fTjWSxG4EI-xE3w12Cx6LJp-_ovU"
 
bot = TelegramClient("rjbot",api_id,api_hash).start(bot_token=bot_token)
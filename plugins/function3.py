from telethon import TelegramClient 
from datetime import datetime
from .. import bot
 
from telethon import events 
 
 
#@tgbot.on(events.NewMessage(incoming=True, pattern="/start")) 
#async def start(event):
#await event.reply("Hello!") 
 
@bot.on(events.NewMessage(pattern='(?i)what is the time'))  # Case-insensitive pattern matching for "hello" 
async def handle_hello(event): 
    # Get the incoming message details 
    message = event.message 
    sender = await message.get_sender()
    today=datetime.now()
    #today=now.strftime("%d-%m-%Y %H:%M:%S")
    # Prepare the response 
    response = f"{sender.first_name},time is-"+str(today)
 
    # Send the response back to the chat 
    await bot.send_message(message.chat_id, response)

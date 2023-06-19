from telethon import TelegramClient 
 
from .. import bot
 
from telethon import events 
 
 
#@tgbot.on(events.NewMessage(incoming=True, pattern="/start")) 
#async def start(event):
#await event.reply("Hello!") 
 
@bot.on(events.NewMessage(pattern='(?i)tell me something'))  # Case-insensitive pattern matching for "hello" 
async def handle_hello(event): 
    # Get the incoming message details 
    message = event.message 
    sender = await message.get_sender() 
 
    # Prepare the response 
    response = f"what do yo want to know, {sender.first_name}!"
 
    # Send the response back to the chat 
    await bot.send_message(message.chat_id, response)

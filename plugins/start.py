from telethon import TelegramClient 

from .. import bot
import openai 
from telethon import events 

import asyncio

#@tgbot.on(events.NewMessage(incoming=True, pattern="/start")) 
#async def start(event):
#await event.reply("Hello!") 

 
@bot.on(events.NewMessage(pattern='(?i)hello'))  # Case-insensitive pattern matching for "hello" 
async def handle_hello(event): 
    # Get the incoming message details 
    message = event.message 
    sender = await message.get_sender() 
 
    # Prepare the response 
    response = f"Hello, {sender.first_name}!"
 
    # Send the response back to the chat 
    await bot.send_message(message.chat_id, response)



@bot.on(events. NewMessage(incoming = True, 
pattern = "/get"))
async def start(event):
  await event.reply("Hello, This is Get command,, i am jasvi,,  How can I help you sir/madam...Jarvis is an artificial intelligence (AI) system developed by Adarsh Singh in the Marvel Cinematic Universe. However, please note that I am javis  and not directly related to the Jarvis AI from the movies. How can I assist you today?")



# @bot.on(events.NewMessage(incoming = True,
# pattern = "/eval"))
# async def start(event):
#   await event.reply("Hello This is Eval command")
  
  
@bot.on(events.NewMessage(incoming = True,
pattern = "/get"))
async def start(event):
  a=await event.reply("Hello This is Get command i am jasvi,,  How can I help you sir/madam...Jarvis is an artificial intelligence (AI) system developed by Adarsh Singh in the Marvel Cinematic Universe. However, please note that I am javis  and not directly related to the Jarvis AI from the movies. How can I assist you today?")
  await asyncio.sleep(1)
  await a.edit("This is the edit msg by jasvi")



@bot.on(events.NewMessage(incoming = True,
pattern = "/eval"))
async def start(event):
  a=await  event.reply("Hello This is Eval command i am jasvi,,  How can I help you sir/madam...Jarvis is an artificial intelligence (AI) system developed by Adarsh Singh in the Marvel Cinematic Universe. However, please note that I am javis  and not directly related to the Jarvis AI from the movies. How can I assist you today?")
  await asyncio.sleep(1)
  await a.edit("This is editing msg by jasvi")
  
  
  
  
  

#to download profile picture

@bot.on(events.NewMessage(incoming=True,pattern='(?i)/mypic'))
async def my_pic(event):
    user = await event.get_sender()
    chat = await event.get_chat()
    photo = await bot.download_profile_photo(user)
    await bot.send_file(chat,file=photo,caption="ye dekh le... apne aap ko.....Wow! This picture is absolutely stunning. The colors and composition are on point!")
  
  

#this is to edit message after the given time
@bot.on(events.NewMessage(incoming=True,pattern='(?i)/edit'))
async def edit(event):
    a = await event.reply("Hey!, lets edit this message")
    await asyncio.sleep(5)
    await a.edit("Boom!! message has been edited")  
    
    
 
 
    #this will reply when user send a spesfic command
@bot.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("Hello! how can i assist")
    
    


       
@bot.on(events.NewMessage(incoming=True, pattern='(?i)/hey'))
async def hello(event):
    await event.reply("Hey! how are you")
    
  
  
    
@bot.on(events.NewMessage(incoming=True,pattern='(?i)/help'))
async def help(event):
    txt ='''ᵂᵉˡᶜᵒᵐᵉ ᵗᵒ ᵐʸ ᵀᵉˡᵉᵍʳᵃᵐ ᵇᵒᵗ!

Here are the available commands and their functions:

/help - Show a list of available commands and their functions.

Hello - .......
/hey - hal chal puchne k liye.
/edit - 2 Second k bad msg edit 

/start - Start the bot
/get - Hello, This is Get command,, i am jasvi,,  How can I help you sir/madam...Jarvis is an artificial intelligence (AI) system developed by Adarsh Singh in the Marvel Cinematic Universe. However, please note that I am javis  and not directly related to the Jarvis AI from the movies. How can I assist you today?

/eval -This is editing msg by jasvi

/What is the time - time and date....

/ask - You are My Developer You developed me very well, hi i am javis.., what can do for you /sir/madam

/mypic@Jarv65_bot - ye dekh le... apne aap ko.....Wow! This picture is absolutely stunning. The colors and composition are on point!


/yta - audio download (copy this link paste here.. )



/ytv- video download (copy this link paste here..)


/tr language name -.............

Feel free to explore and interact with the bot. If you have any questions or need assistance, don't hesitate to ask!

Enjoy your experience with the bot!

𝖢𝗋𝖾𝖺𝗍𝖾𝖽 𝖺𝗇𝖽 𝖬𝖺𝗇𝖺𝗀𝖾𝖽 𝖡𝗒: @Adarsh517
'''
    await event.reply(txt)
    

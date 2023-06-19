from .. import bot
from telethon import events
import asyncio



@bot.on(events.NewMessage(incoming=True, pattern="hello"))
async def hello(event):
  await event.reply("How are you")

@bot.on(events.NewMessage(incoming=True, pattern="/start"))
async def hello(event):
  await event.reply("welcome")

@bot.on(events.NewMessage(incoming=True, pattern="python"))
async def hello(event):
  await event.reply("Is a programming language")
  
@bot.on(events.NewMessage(incoming=True, pattern="hii"))
async def hello(event):
  await event.reply("hello sir/medam,how can I help you?")
  
@bot.on(events.NewMessage(incoming=True,pattern= "(?i)/ask"))
async def ask(event):
  if event.sender_id == int(5259217283) :
    await event.reply("you are developer! you developed me very well")
  else:
    await event.reply("you are a user!how can I help you?")

import random
from telethon import TelegramClient, events
from .. import bot


# Jokes list
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
    "I'm reading a book about anti-gravity. It's impossible to put down!",
    "Why don't skeletons fight each other? They don't have the guts!",
    "I used to play piano by ear, but now I use my hands.",
    "Why don't eggs tell jokes? Because they might crack up!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why don't skeletons fight each other? They don't have the guts!"
    ]
# Command handler
@bot.on(events.NewMessage(pattern='/joke'))
async def handle_joke(event):
    chat = await event.get_chat()

    # Select a random joke
    joke = random.choice(jokes)

    # Send the joke as a message
    await event.reply(joke)
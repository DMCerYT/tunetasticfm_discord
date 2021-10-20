import discord
from discord.client import client

@client.event
async def on_messagetest(message):
    message.content.lower()
    if message.author == client.user:
        return

    if message.content.startswith("hello tunetastic"):
        await message.channel.send("Hello, I am Emmet's new born child :D")

    if message.content.startswith("number one victory royale"):
        await message.channel.send("Yea fortnite we boutta get down!")
    
    if message.content.startswith("what is your purpose tunetastic?"):
        await message.channel.send("To one day be able to play music in the Voice Channels...")
    
    if message.content.startswith("ea sports"):
        await message.channel.send("its in the game")

    if message.content.startswith("sus"):
        await message.channel.send(":cheems:")

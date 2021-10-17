import discord
import youtube_dl
import os
import asyncio
import datetime
from discord.channel import VoiceChannel
from discord.ext import commands
#import motwcount
#import coolmessage

x = datetime.datetime.now()

client = discord.Client()

"""
joestar = 0
supremeleaderofjo = 0
dmcer = 0
person_four = 0
person_five = 0
person_six = 0
"""
#motwcount()

    

@client.event
async def on_message(message):
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
"""
@client.command()
async def play(ctx, url : str, channel):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel)
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if not voice.is_connect():
        await voiceChannel.connect()

@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.sent("The bot is not connected to a VOICE CHANNEL!")

@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing. :/")

@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.set("The audio is not paused.")

@client.command
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop




"""
#runs the client :D
client.run('ODg3NDY3MTQ5ODM5NDUwMTIz.YUEkMA.CZnuIPvvlbZVZ_UyOs_KUUpsFFM')
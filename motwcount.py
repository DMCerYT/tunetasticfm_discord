import datetime
import random
import time
import discord
from discord import channel
from discord import client

while True:
    testone = datetime.datetime.now()
    print(testone.strftime("%W"))
    time.sleep(2)
    testtwo = datetime.datetime.now()
    print(testtwo.strftime("%W"))
    if testone.strftime("%W") != testtwo.strftime("%W"):
        print("different")
    elif testone.strftime("%W") == testtwo.strftime("%W"):
        print("same")
        break
    time.sleep(2)

lastmessage = datetime.datetime.now()

counter = 0
@client.event
async for message in channel.history(limit = 1000, after = lastmessage.strftime("%W")):
    if message.auythor == client.user:
        counter += 1
        print(counter)
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
        
    if message.content.startswith("no tunetastic"):
        await message.channel.send("ok boomer")
       
    if message.content.startswith("why tunetastic"):
        await message.channel.send("Nihilism (/ˈnaɪ(h)ɪlɪzəm, ˈniː-/; from Latin nihil 'nothing') is a philosophy, or family of views within philosophy, that rejects general or fundamental aspects of human existence, such as objective truth, knowledge, morality, values or meaning. Different nihilist positions hold variously that human values are baseless, that life is meaningless, that knowledge is impossible, or that some set of entities do not exist or are meaningless or pointless.")

    if message.content.startswith("hotel"):
        await message.channel.send("trivago") 
        
    if message.content.startswith("kromer"):
        await message.channel.send("HEY EVERY !! IT’S ME!!! EV3RY BUDDY ‘S FAVORITE [[Number 1 Rated Salesman1997]] SPAMT SPAMTON G. SPAMTON!! WOAH!! IF IT ISN”T A… LIGHT nER! HEY-HE Y HEY!!! LOOKS LIKE YOU’RE [[All Alone On A Late Night?]] ALL YOUR FRIENDS, [[Abandoned you for the slime]] YOU ARE? SALES, GONE DOWN THE [[Drain]] [[Drain]]?? LIVING IN A GODDAMN GARBAGE CAN??? WELL HAVE I GOT A [[Specil Deal]] FOR LONELY [[Hearts]] LIKE YOU!! IF YOU’VE [[Lost Control Of Your Life]] THEN YOU JUST GOTTA GRAB IT BY THE [[Silly Strings]] WHY BE THE [Little Sponge]] WHO HATES ITS [[$4.99]] LIFE WHEN YOU CAN BE A [[BIG SHOT!!!]] [[BIG SHOT!!!!]] [[BIG SHOT!!!!!]] THAT’S RIGHT!! NOW’S YOUR CHANCE TO BE A [[BIG SHOT]]!! AND I HAVE JUST. THE THING. YOU NEED. THAT’S [[Hyperlink Blocked]] YOU WANT IT. YOU WANT [[Hyperlink Blocked]] DON’T YOU. WELL HAVE I GOT A DEAL FOR YOU!! ALL YOU HAVE TO DO IS SHOW ME. YOUR [[HeartShapedObject]]. YOU’RE LIGHT neR< AREN’T YOU? YOUVE GOT THE [[LIGHT.]] WHY DON’T YOU [[Show t off?]]")        

import discord
import requests
import os
client = discord.Client()

@client.event
async def on_ready(): # ready to be used
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): # receiving messages
    if message.author == client.user:
        return

    msg = message.content
    if msg.startswith('$hello'):
        await message.channel.send('Wassup I am O\'hare! I am a cool smug rabbit and I also care about you ♥.')
    
    if msg.startswith('$depression'):
        await message.channel.send('onO, you wanna talk about it?')

    
client.run(os.getenv('TOKEN'))
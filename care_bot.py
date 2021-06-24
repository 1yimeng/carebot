import discord
import os
from pickup import text_list
from dotenv import load_dotenv
import random
import funresponses

load_dotenv('TOKEN.env')
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

love_words = ['love', 'bf', 'gf', 'dating', 'like']

@client.event
async def on_ready(): # ready to be used
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): # receiving messages
    if message.author == client.user:
        return

    msg = message.content
    if msg.startswith('-hello'):
        await message.channel.send('Wassup I am O\'hare! I am a cool smug rabbit and I also care about you ♥.')
    
    if msg.startswith('-depression'):
        embed = discord.Embed()
        embed.description = '\n\n**Useful Links**\n[Tips on how to deal with depression](https://www.helpguide.org/articles/depression/coping-with-depression.htm) \n[Tips on how to help someone that has depression](https://www.helpguide.org/articles/depression/helping-someone-with-depression.htm)'
        await message.channel.send('**Depression** \nDepression (major depressive disorder) is a common and serious medical illness that negatively affects how you feel, the way you think and how you act. Fortunately, it is also treatable. Depression causes feelings of sadness and/or a loss of interest in activities you once enjoyed. It can lead to a variety of emotional and physical problems and can decrease your ability to function at work and at home.')
        await message.channel.send(embed = embed)
    
    if msg.startswith('-pick me up'):
        await message.channel.send(random.choice(text_list))

    if any(word in msg for word in love_words):
        await message.channel.send("Love in the air!")

    if msg.startswith('-toast'):
        await message.channel.send(funresponses.toast())

    if msg.startswith('-roast'):
        await message.channel.send(funresponses.roast())

    if msg.startswith('-joke'):
        await message.channel.send(funresponses.joke())

    if msg.startswith('-help'):
        await message.channel.send('**Current available commands:** \n-hello \n-pick me up \n-depression \n-toast \n-roast \n-joke')

client.run(TOKEN)
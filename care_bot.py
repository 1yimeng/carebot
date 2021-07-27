import discord
import os
from pickup import text_list
from dotenv import load_dotenv
import random
import funresponses
import atexit
import sys 
from convo_starter import get_convo

load_dotenv('TOKEN.env')
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

love_words = ['love', 'bf', 'gf', 'dating', 'like']
quotes = []
emojis = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣']

def saving_quotes():
    if not quotes:
        sys.quit()
        print('No quotes to write to file')
    elif quotes == getting_quotes():
        print("\n")
    else:
        with open('quotes.txt', 'w') as f:
            f.write('\n'.join(quotes))
            f.close()
        print('\nQuotes written in file.')

def getting_quotes():
    quotes = []
    if os.stat('quotes.txt').st_size == 0:
        print('No quotes in the text file, none read.')
        return quotes
    else:
        with open('quotes.txt', 'r') as f:
            content = f.readlines()
            f.close()
        quotes = [x.strip() for x in content]
        return quotes

@client.event
async def on_ready(): # ready to be used
    print('We have logged in as {0.user}'.format(client))
    global quotes 
    quotes = getting_quotes()
    # print(quotes)
    print('Quotes are read.')

@client.event
async def on_message(message): # receiving messages
    msg = message.content
    
    for emoji in emojis:
        if emoji in msg and message.author.bot:
            await message.add_reaction(emoji)

    # if message.author == client.user:
    #     return

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
        await message.channel.send('**Current available commands:** \n-hello \n-pick me up \n-depression \n-toast \n-roast \n-joke \n-add quotes [insert quotes] \n-quotes (get random quotes) \n-del quotes \n-del num')

    if msg.startswith('-add quotes'):
        new_quote = msg.split('-add quotes ', 1)[1]
        quotes.append(new_quote)
        await message.channel.send(f'The quote: \'{new_quote}\' is added.')
    
    if msg.startswith('-quotes'):
        if not quotes:
            await message.channel.send('There is no quote stored D:')
        else:
            await message.channel.send(random.choice(quotes))
    
    if msg.startswith('-del quotes'):
        if not quotes:
            await message.channel.send('There is no quote stored D:')
        else:    
            await message.channel.send('The quotes stored are: ')
            await message.channel.send("\n".join(quotes))
            await message.channel.send('Enter -del num (quote\'s position\'s number) to delete')

    if msg.startswith('-del num'):
        if not quotes:
            await message.channel.send('There is no quote stored D:')
        else:   
            index = int(msg.split('-del num ', 1)[1])
            quotes.remove(quotes[index-1])
            if not quotes:
                await message.channel.send('No more quotes!')
            else:
                await message.channel.send('The quotes stored are: ')
                await message.channel.send("\n".join(quotes))
    
    if msg.startswith('-poll'):
        in_list = msg.split(",")
        question = in_list[1]
        pure_option = in_list[2:]
        new_option = [option.strip() for option in pure_option]
        await message.channel.send('**'+ question + '**')
        my_options = []
        for i in range(len(new_option)): 
            my_options.append(emojis[i] + " " + new_option[i])
        await message.channel.send('\n'.join(my_options))

    if msg.startswith('-convo'):
        my_convo = get_convo()
        await message.channel.send('**'+ random.choice(my_convo) + '**')
        
client.run(TOKEN)
atexit.register(saving_quotes)
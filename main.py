import re

import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if re.findall('^l$', message.content):
        await message.channel.send('sauce lc 3#1')

    if message.author == '661826254215053324' and re.findall("Looking up .+? by .+?\.", message.content):
        # ID is for License checker bot
        author = re.search("Looking up .+? by (.+?)\.", message.content).group(1)
        await message.channel.send(f"sauce -qa {author}")

#!/usr/bin/python3.6

import discord

from secret_token import client_secret

client = discord.Client()



@client.event
async def on_message(message):
    print(message.content)
    if message.content.find("!hello") != -1:
        await message.channel.send("Hi")
        await message.channel.send('Hello', file=discord.File('img.png'))

client.run(client_secret)

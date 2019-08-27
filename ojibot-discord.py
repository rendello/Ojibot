#!/usr/bin/python3.6

import discord

from Discord.secret_token import client_secret
from Discord.format import fmt_all, fmt_dict_to_text
import Core.lookup

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.find("!oji") != -1:
        if message.author == client.user:
            return
        command = message.content.replace('!oji ', '', 1)
        info = Core.lookup.fetch_oji_word_info(command)
        formatted_info = fmt_dict_to_text(fmt_all(info))

        await message.channel.send(formatted_info)

client.run(client_secret)

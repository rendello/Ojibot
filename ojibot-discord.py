#!/usr/bin/python3.6

import discord

from Discord.secret_token import client_secret
from Discord.format import fmt_all, fmt_dict_to_text
import Core.lookup

client = discord.Client()

string = """.\n__**gaandakii'iganaak**__
a push pole

__Word Parts__
 **gaandakii'iganaak** /gaandakii'iganaakw-/: /__gaandakii'igan__-/ stem of __gaandakii'igan__  ; /-__aakw__/ stick, wood, organic solid 

__Example sentences__
**Gaandakii'iganaak gii-aabajitoowaad igi anishinaabeg gii-manoominikewaad.**
> *The Ojibwe use a push pole when ricing.*

**Mii 'i dinowa gaa-aabadak gaandakii'iganaak gii-manoominkewaad igiw anishinaabeg.**
> *The thing that the Ojibwe use when they rice is a push pole.*

**Ogii-peshaakwanamowaan iniw ojiwaaman megwaa gaandakii'iged i'iw ogaandakii'iganaak.**
> *While he was poling he nearly missed his friend with his push pole.*
"""

@client.event
async def on_message(message):
    print(message.content)
    if message.content.find("!oji") != -1:
        if message.author == client.user:
            return
        #await message.channel.send("Hi")
        #await message.channel.send(string)
        command = message.content.replace('!oji ', '', 1)
        info = Core.lookup.fetch_oji_word_info(command)
        formatted_info = fmt_dict_to_text(fmt_all(info))

        await message.channel.send(formatted_info)

client.run(client_secret)

#!/usr/bin/python3.6

import discord

from secret_token import client_secret

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
    if message.content.find("!hello") != -1:
        await message.channel.send("Hi")
        await message.channel.send(string)

client.run(client_secret)

#!/usr/bin/python3.6

import discord
from discord.ext import commands

import Core.backend as backend
from Core.secrets import discord_secret

bot = commands.Bot(command_prefix='!')

@bot.command()
async def oji(ctx, word):
    string = backend.to_eng(word)
    await ctx.send(string)


@bot.command()
async def random(ctx):
    string = backend.random_to_eng()
    await ctx.send(string)


bot.run(discord_secret)

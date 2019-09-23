#!/usr/bin/python3.6

import discord
from discord.ext import commands

from Core.lookup import fetch_oji_word_info
from Core.db_lookup import fuzzy_match, get_random_word, get_word_urls
from Core.normalize import to_rough_fiero
from Core.format import serialize_all, format_for_discord

from Core.secret_token import discord_secret

bot = commands.Bot(command_prefix='!')


def oji_backend(word):
    ''' Gets a supposed Ojibwe word from the chat, and gives the definiton and
    other word information. Tries to find the closest word if the spelling's
    not exactly the same.

    Args:
        ctx: context, needed for Discord
        word: <str>, a supposed Ojibwe word.

    Returns:
        string: a <str> of nicely formatted information about the requested
        word (or whatever word's most similar).
    '''
    urls = get_word_urls(word)

    # Find the closest word if the specific requested spelling's not in db
    if urls == []:
        word = to_rough_fiero(word)
        word = fuzzy_match(word, 1)[0]['word'] # Single element list containing dict
        urls = get_word_urls(word)

    # Sometimes there's multiple words with the same definition
    string = ''
    for url in urls:
        info = fetch_oji_word_info(url)
        serialized = serialize_all(info)
        string += format_for_discord(serialized)

    return string


@bot.command()
async def oji(ctx, word):
    string = oji_backend(word)
    await ctx.send(string)


@bot.command()
async def random(ctx):
    string = oji_backend(get_random_word())
    await ctx.send(string)


bot.run(discord_secret)

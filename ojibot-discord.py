#!/usr/bin/python3.6

import discord
from discord.ext import commands

from Discord.secret_token import client_secret
from Discord.format import fmt_all, fmt_dict_to_text
from Core.lookup import get_word_urls, fetch_oji_word_info
from Core.db_lookup import fuzzy_match
from Core.normalize import to_rough_fiero

bot = commands.Bot(command_prefix='!')

@bot.command()
async def oji(ctx, word):
    ''' Gets a supposed Ojibwe word from the chat, and gives the definiton and
    other word information. Tries to find the closest word if the spelling's
    not exactly the same.

    Args:
        ctx: context, needed for Discord
        word: <str>, a supposed Ojibwe word.

    Returns:
        <None>
    '''
    urls = get_word_urls(word)

    # Find the closest word if the specific requested spelling's not in db
    if urls == []:
        word = to_rough_fiero(word)
        word = fuzzy_match(word, 1)[0]['word'] # Single element list containing dict
        urls = get_word_urls(word)

    # Sometimes there's multiple words with the same definition
    for url in urls:
        info = fetch_oji_word_info(url)
        string = fmt_dict_to_text(fmt_all(info))
        await ctx.send(string)
    



bot.run(client_secret)

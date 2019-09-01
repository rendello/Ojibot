#!/usr/bin/python3.6

import discord
from discord.ext import commands

from Discord.secret_token import client_secret
from Discord.format import fmt_all, fmt_dict_to_text
from Core.lookup import get_word_urls, fetch_oji_word_info
from Core.db_lookup import fuzzy_match
from Core.normalize import to_rough_fiero

bot = commands.Bot(command_prefix='!oji ')

@bot.command()
async def oji(ctx, word):
    urls = get_word_urls(word)
    if urls == []:
        word = to_rough_fiero(word)
        word = fuzzy_match(word, 1)[0]['word']
        print(word)
    urls = get_word_urls(word)
    for url in urls:
        info = fetch_oji_word_info(url)
        string = fmt_dict_to_text(fmt_all(info))
        await ctx.send(string)
    



bot.run(client_secret)

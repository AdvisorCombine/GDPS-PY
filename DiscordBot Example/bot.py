### Module: PyCord

import discord
from discord.ext import commands
from gdps import *

bot = commands.Bot(command_prefix='!', help_command=None)

@bot.event
async def on_ready():
    print('Bot is Ready')

@bot.command()
async def level(ctx, identify):
    level = await fetch_level(identify)
    e = discord.Embed(
        title=f'Information about {level.name()}',
        color=discord.Colour.dark_magenta()
    )
    e.add_field(name='Coins:', value=f'{level.coins()}', inline=False)
    e.add_field(name='Stars:', value=f'{level.stars()}', inline=False)
    await ctx.reply(embed=e)

bot.run('token')
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$', description="This is a Helper Bot")

word_list = []
with open("word_list.txt") as file_in:
    for line in file_in:
        word_list.append(line)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def pm(ctx):
    await ctx.message.author.send('test message')

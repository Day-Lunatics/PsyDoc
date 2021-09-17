import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>', description="This is a Helper Bot")


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run('ODg4NDQwNzYwMTAwMzU2MDk4.YUSu7w.SAN_I8QmJREGl9FgCyCc6Z6-PbA')

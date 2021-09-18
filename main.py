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


# @bot.command()
# async def pm(ctx):
#     await ctx.message.author.send('test message')


@bot.command()
async def tests(ctx):
    embed = discord.Embed(colour=discord.Color.green())
    embed.set_author(name='Tests:')
    embed.add_field(name='depression', value='lorem ipsum dolor sin ament', inline=False)
    embed.add_field(name='alcoholism', value='lorem ipsum dolor sin ament', inline=False)
    embed.add_field(name='drug', value='lorem ipsum dolor sin ament', inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def depression(ctx):
    await ctx.message.author.send('test message depression')


@bot.command()
async def alcoholism(ctx):
    await ctx.message.author.send('test message alcoholism')


@bot.command()
async def drug(ctx):
    await ctx.message.author.send('test message drug')
    # embed = discord.Embed(title="New Poll!", description='message', color=0xff0000)
    # reaction = "👍"
    # await ctx.message.add_reaction(emoji=reaction)

@bot.command()
async def poll(ctx):
    message = await ctx.send(f"Question 1: \n1️= Answer 1\n2️= Answer 2\n3️= Answer 3\n4️= Answer 4\n")
    await message.add_reaction('1️⃣')
    await message.add_reaction('2️⃣')
    await message.add_reaction('3️⃣')
    await message.add_reaction('4️⃣')


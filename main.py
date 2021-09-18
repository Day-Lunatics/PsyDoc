import json

import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='$', description="This is a Helper Bot")
question_bank = ['Question1', 'Question2', 'Question3', 'Question4', 'Question5', 'Question6',
                 'Question7', 'Question8', 'Question9', 'Question10']

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
    random_List_No_Rep = random.sample(question_bank, 5)
    with open('gambling.json') as json_file:
        data = json.load(json_file)
        for idx, val in enumerate(random_List_No_Rep):
            for p in data[random_List_No_Rep[idx]]:    #random.choice(question_bank)
                message = await ctx.send(f"" + p['q'] + "\n"
                                         f"1️= " + p['a'] + "\n"
                                         f"2️= " + p['b'] + "\n"
                                         f"3️= " + p['c'] + "\n"
                                         f"4️= " + p['d'] + "\n")
                await message.add_reaction('1️⃣')
                await message.add_reaction('2️⃣')
                await message.add_reaction('3️⃣')
                await message.add_reaction('4️⃣')


@bot.command()
async def pool2(ctx):
    await ctx.send("You want to take a quick survey?")
    message = await bot.wait_for('message', timeout=20, check=lambda m:m.author == ctx.author and m.channel == ctx.channel)
    if message.content == "yes":
        #await ctx.send("Good, so pick a category you interest in")
        user_answer = []
        await ctx.send(f"Good, so pick a category you interest in\n"
                       f"1️= Drug\n"
                       f"2️= Drunk\n"
                       f"3️= Depression\n")
        message = await bot.wait_for('message', timeout=20, check=lambda m:m.author == ctx.author and m.channel == ctx.channel)
        if message.content == "1":
            random_List_No_Rep = random.sample(question_bank, 5)
            with open('gambling.json') as json_file:
                data = json.load(json_file)
                for idx, val in enumerate(random_List_No_Rep):
                    for p in data[random_List_No_Rep[idx]]:  # random.choice(question_bank)
                        message = await ctx.send(f"" + p['q'] + "\n"
                                                 f"1️= " + p['a'] + "\n"
                                                 f"2️= " + p['b'] + "\n"
                                                 f"3️= " + p['c'] + "\n"
                                                 f"4️= " + p['d'] + "\n")

                        message = await bot.wait_for('message', timeout=20, check=lambda m:m.author == ctx.author and m.channel == ctx.channel)
                        user_answer.append(int(message.content))

            total_points = sum(user_answer)

            if total_points >= 18:
                await ctx.send(f">=18 Dobra to dajem jaki masz problem byczq")
            if total_points >= 15 & total_points < 18:
                await ctx.send(f">=15 Dobra to dajem jaki masz problem byczq")
            if total_points >= 10 & total_points < 15:
                await ctx.send(f">=10 Dobra to dajem jaki masz problem byczq")
            if total_points < 10:
                await ctx.send(f"<10 Dobra to dajem jaki masz problem byczq")




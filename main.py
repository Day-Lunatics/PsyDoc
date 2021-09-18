import json

import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='$', description="This is a PsyBot")
question_bank = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


@bot.command()
async def PsyBot(ctx):
    await ctx.message.author.send("You want to take a quick survey?")
    message = await bot.wait_for('message', timeout=20, check=lambda m:m.author == ctx.author)
    if message.content == "yes":
        user_answer = []
        await ctx.message.author.send(f"Choose with form you would like to take\n Type the appropriate number \n"
                                      f"1️= Gambling addiction\n"
                                      f"2️= Alcoholism\n"
                                      f"3️= Depression\n")
        message = await bot.wait_for('message', timeout=20, check=lambda m:m.author == ctx.author)
        if message.content == "1":
            random_List_No_Rep = random.sample(question_bank, 5)
            with open('gambling.json') as json_file:
                data = json.load(json_file)
                for idx, val in enumerate(random_List_No_Rep):
                    for p in data[random_List_No_Rep[idx]]:  # random.choice(question_bank)
                        message = await ctx.message.author.send(f"" + p['q'] + "\n Type the appropriate number \n"
                                                                f"1️= " + p['a'] + "\n"
                                                                f"2️= " + p['b'] + "\n"
                                                                f"3️= " + p['c'] + "\n"
                                                                f"4️= " + p['d'] + "\n")

                        message = await bot.wait_for('message', timeout=20, check=lambda m:m.author == ctx.author)
                        user_answer.append(int(message.content))

            total_points = sum(user_answer)

            await ctx.message.author.send(total_points)

            if total_points >= 18:
                await ctx.message.author.send(f"You should contact professional help")
            elif 15 <= total_points < 18:
                await ctx.message.author.send(f"You should highly consider contacting professional help")
            elif 10 <= total_points < 15:
                await ctx.message.author.send(f"You should consider contacting someone and talk about your problems")
            elif total_points < 10:
                await ctx.message.author.send(f"You don't need to contact anyone at the moment but remember to take good care of yourself")

        if message.content == "2":
            random_List_No_Rep = random.sample(question_bank, 5)
            with open('alcohol.json') as json_file:
                data = json.load(json_file)
                for idx, val in enumerate(random_List_No_Rep):
                    for p in data[random_List_No_Rep[idx]]:
                        message = await ctx.message.author.send(f"" + p['q'] + "\n Type the appropriate number \n"
                                                                f"1️= " + p['a'] + "\n"
                                                                f"2️= " + p['b'] + "\n"
                                                                f"3️= " + p['c'] + "\n"
                                                                f"4️= " + p['d'] + "\n")

                        message = await bot.wait_for('message', timeout=20, check=lambda m:m.author == ctx.author)
                        user_answer.append(int(message.content))

            total_points = sum(user_answer)

            await ctx.message.author.send(total_points)

            if total_points >= 18:
                await ctx.message.author.send(f"You should contact professional help")
            elif 15 <= total_points < 18:
                await ctx.message.author.send(f"You should highly consider contacting professional help")
            elif 10 <= total_points < 15:
                await ctx.message.author.send(f"You should consider contacting someone and talk about your problems")
            elif total_points < 10:
                await ctx.message.author.send(f"You don't need to contact anyone at the moment but remember to take good care of yourself")

        if message.content == "3":
            random_List_No_Rep = random.sample(question_bank, 5)
            with open('depression.json') as json_file:
                data = json.load(json_file)
                for idx, val in enumerate(random_List_No_Rep):
                    for p in data[random_List_No_Rep[idx]]:
                        message = await ctx.message.author.send(f"" + p['q'] + "\n Type the appropriate number \n"
                                                                f"1️= " + p['a'] + "\n"
                                                                f"2️= " + p['b'] + "\n"
                                                                f"3️= " + p['c'] + "\n"
                                                                f"4️= " + p['d'] + "\n")

                        message = await bot.wait_for('message', timeout=20, check=lambda m:m.author == ctx.author)
                        user_answer.append(int(message.content))

            total_points = sum(user_answer)

            await ctx.message.author.send(total_points)

            if total_points >= 18:
                await ctx.message.author.send(f"You should contact professional help")
            elif 15 <= total_points < 18:
                await ctx.message.author.send(f"You should highly consider contacting professional help")
            elif 10 <= total_points < 15:
                await ctx.message.author.send(f"You should consider contacting someone and talk about your problems")
            elif total_points < 10:
                await ctx.message.author.send(f"You don't need to contact anyone at the moment but remember to take good care of yourself")


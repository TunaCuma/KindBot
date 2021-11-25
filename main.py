import discord
from discord.ext import commands
import random
bot = discord.Client()
bot_prefix="?kind "
bot = commands.Bot(command_prefix=bot_prefix)


@bot.event
async def on_ready() :
    print("Bot is online!")
    print("Name : {}".format(bot.user.name))
    print("ID : {}".format(bot.user.id))
    print("reaching " + str(len(set(bot.get_all_members()))) + " users!")
    await bot.change_presence (activity=discord.Game('type "?kind info"'))


@bot.command(pass_context=True)
async def info(ctx) :
    await ctx.send('type "?kind quote" for a inspirational quote.\ntype "?kind gif" for a cute gif.')

@bot.command(pass_context=True)
async def gif(ctx):
    gifs = ["https://imgur.com/t/dog/ERI7tFc","https://imgur.com/t/dog/3P9LLbR","https://imgur.com/t/dog/thmKlZz","https://imgur.com/t/dog/ju2DfSL","https://imgur.com/t/dog/HoatTmh","https://imgur.com/t/dog/DWG5kS6","https://imgur.com/t/dog/VsLWHQO","https://imgur.com/t/dog/GRsqF9I","https://imgur.com/t/dog/2v72KG8","https://imgur.com/t/dog/7hwPm1J"]
    await ctx.send(random.choice(gifs))

@bot.command(pass_context=True)
async def quote(ctx):
    filesize = 8000              #size of the really big file
    offset = random.randrange(filesize)

    f = open('quotes.csv')
    f.seek(offset)                  #go to random position
    f.readline()                    # discard - bound to be partial line
    random_line = f.readline()      # bingo!

    # extra to handle last/first line edge cases
    if len(random_line) == 0:       # we have hit the end
        f.seek(0)
        random_line = f.readline()  # so we'll grab the first line instead
    person = random_line.split(",")[0]
    await ctx.send(random_line[len(random_line.split(",")[0])+1:]+"-"+person[1:][:-1])



bot.run("OTEzNTQ5NTI3NjgyNzg1MzUw.YaAHTA.XxGgCN1HYMNgfB9G7_vPWivFobE")
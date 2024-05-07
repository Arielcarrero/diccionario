import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def saludos(ctx):
    await ctx.send("Bienvenidos")

@bot.command()
async def suma(ctx, num1:int, num2:int ):
    resultado=num1+num2
    await ctx.send(resultado)

@bot.command()
async def multiplica(ctx, num1:int, num2:int ):
    resultado=num1*num2
    await ctx.send(resultado)

@bot.command()
async def resta(ctx, num1:int, num2:int ):
    resultado=num1-num2
    await ctx.send(resultado)

@bot.command()
async def divide(ctx, num1:int, num2:int ):
    resultado=num1/num2
    await ctx.send(resultado)
bot.run()

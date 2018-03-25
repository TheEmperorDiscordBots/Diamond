import discord
from discord.ext import commands
import asyncio
import os

bot = commands.Bot(command_prefix='d.')
        
bot.blacklist = []

        
@bot.event
async def on_ready():
    while True:
        await bot.change_presence(game=discord.Game(name=f"with {len(bot.guilds)} servers!"))
        await asyncio.sleep(20)
        await bot.change_presence(game=discord.Game(name="d.help!"))
        await asyncio.sleep(20)
        await bot.change_presence(game=discord.Game(name="https://discord.gg/zzzJAKM"))
        await asyncio.sleep(20)

        
@bot.command()
async def ping(ctx):
    '''Pong! Get the bot's response time'''
    em = discord.Embed(color=discord.Color(value=0x00ff00))
    em.title = "Pong!"
    em.description = f'{bot.ws.latency * 1000:.4f} ms'
    await ctx.send(embed=em)
        
@bot.event
async def on_message(msg):
    if not msg.author.bot:
        if not str(msg.author.id) in bot.blacklist:
            await bot.process_commands(msg)


@bot.event
async def on_ready():
        """Shows bot's status"""
        print("----------------")
        print("Logged in as:")
        print("Name : {}".format(bot.user.name))
        print("ID : {}".format(bot.user.id))
        print("Py Lib Version: %s"%discord.__version__)
        print("----------------")

if not os.environ.get('TOKEN'):
    print("no token found!")
bot.run(os.environ.get('TOKEN').strip('"'))

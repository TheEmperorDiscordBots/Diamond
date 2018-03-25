import discord
from discord.ext import commands
import asyncio
import os

bot = commands.Bot(command_prefix='d.')
        
@bot.event
async def on_ready():
    while True:
        await bot.change_presence(activity=discord.Game(name=f"with {len(bot.guilds)} servers"))
        await asyncio.sleep(20)
        await bot.change_presence(activity=discord.Game(name="d.help"))
        await asyncio.sleep(20)
        await bot.change_presence(activity=discord.Game(name="https://discord.gg/zzzJAKM"))
        await asyncio.sleep(20)

        
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    await bot.process_commands(message)


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

import discord
import unicodedata
from discord.ext import commands
import time
from motor.motor_asyncio import AsyncIOMotorClient
import motor.motor_asyncio 
import datetime
import sys
import psutil
import asyncpg
from pymongo import MongoClient
import requests
import ftfy
import traceback
from discord.ext.commands import errors
import openweathermapy.core as weather
import platform
import copy
import asyncio
import os
import urllib.parse
from urllib.request import urlopen
import aiohttp
import json
import random
import io
import textwrap
import subprocess
import inspect
from urllib.parse import urlencode
from contextlib import redirect_stdout
from utils.config import *
from pyfiglet import figlet_format as ascii_format

bot = commands.Bot(command_prefix='=')
        
bot.blacklist = []

startup_extensions = [

    'cogs.Owner',
    'cogs.Errorhandler'

]


def dev_check(id):
    with open('data/devs.json') as f:
        devs = json.load(f)
        if id in devs:
            return True
        return False  

def cleanup_code(content):
    '''Automatically removes code blocks from the code.'''
    # remove ```py\n```
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])

    return content.strip('` \n')

@bot.command()
async def invite(ctx):
    await ctx.send("https://discordapp.com/api/oauth2/authorize?client_id=430124797838491678&permissions=0&scope=bot")

        
@bot.event
async def on_ready():
    while True:
        await bot.change_presence(activity=discord.Game(name=f"with {len(bot.guilds)} servers!"))
        await asyncio.sleep(20)
        await bot.change_presence(activity=discord.Game(name="=help"))
        await asyncio.sleep(20)
        await bot.change_presence(activity=discord.Game(name="https://discord.gg/zzzJAKM"))
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

        
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
            print('Loaded extension: {}'.format(extension))
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))


if not os.environ.get('TOKEN'):
    print("no token found!")
bot.run(os.environ.get('TOKEN').strip('"'))

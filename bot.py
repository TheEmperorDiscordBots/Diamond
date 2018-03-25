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
from utils.paginator import Pages
import io
import textwrap
import subprocess
import inspect
from urllib.parse import urlencode
from contextlib import redirect_stdout
from utils.config import *
from ext import utils
from pyfiglet import figlet_format as ascii_format

bot = commands.Bot(command_prefix='d.')
        
bot.blacklist = []


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
async def eval(ctx, *, body: str):
    '''Evaluate python code'''
    if not dev_check(ctx.author.id):
        return await ctx.send("Sorry you cannot use this command.")
    env = {
        'bot': bot,
        'ctx': ctx,
        'channel': ctx.channel,
        'author': ctx.author,
        'guild': ctx.guild,
        'message': ctx.message,
    }

    env.update(globals())

    body = cleanup_code(body)
    stdout = io.StringIO()

    to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

    try:
        exec(to_compile, env)
    except Exception as e:
        return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

    func = env['func']
    try:
        with redirect_stdout(stdout):
            ret = await func()
    except Exception as e:
        value = stdout.getvalue()
        await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
    else:
        value = stdout.getvalue()
        try:
            await ctx.message.add_reaction('\u2705')
        except:
            pass

        if ret is None:
            if value:
                await ctx.send(f'```py\n{value}\n```')
        else:
            await ctx.send(f'```py\n{value}{ret}\n```')
        
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

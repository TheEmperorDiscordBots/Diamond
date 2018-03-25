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



class Owner:
    '''
    Owner commands
    '''
    def __init__(self, bot):
        self.bot = bot
        
        
        
    @commands.cooldown(1, 600, commands.BucketType.user)
    @commands.guild_only()
    @commands.command(pass_context = True)
    async def suggest(self, ctx, *, pmessage : str = None):
        """Suggest something"""
        invite = await ctx.channel.create_invite(max_uses = 1, xkcd = True)
        dev = self.bot.get_user(349674631260667925)

        if pmessage == None:
            embed = discord.Embed(description = f"**{ctx.author.name}**, my developers need to know something. Type a feedback!", color = failcolor)
            message = await ctx.send(embed = embed)
            await message.edit(delete_after = 15)

        else:
            try:
                embed = discord.Embed(colour = passcolor)
                embed.set_thumbnail(url = f"{ctx.author.avatar_url}")
                embed.add_field(name = f"Information: ", value = f"Name: **{ctx.author.name}**\nID: **{ctx.author.id}**\nServer: [**{ctx.guild}**]({invite.url})", inline = False)
                embed.add_field(name = f"Feedback/Message: ", value = f"{pmessage}", inline = False)
                await dev.send(embed = embed)
                embed = discord.Embed(description = f"I have sent a message to my developer with your feedback! Thank you for your help!", color = passcolor)
                await ctx.send(embed = embed)
            except discord.Forbidden:
                embed = discord.Embed(color = failcolor)
                embed.add_field(name = "Oops, something went wrong!", value = f"**{ctx.author.name}**, I'm not allowed to do this!", inline = False)
                await ctx.send(embed = embed)    
                
                
                
                
                
                
def setup(bot):
    bot.add_cog(Owner(bot))

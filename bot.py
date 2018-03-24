import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='d.')


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

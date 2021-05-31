from __future__ import print_function
import discord
from discord.ext import commands
from discord.ext.commands.core import command
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import calendarAPI

description = '''A bot to help organise committee meetings'''

bot = commands.Bot(command_prefix='>')
intents = discord.Intents.default()
intents.members = True
token = open('discordToken.scrt').read()

calService = calendarAPI.authorize()


bot = commands.Bot(command_prefix='>', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    

@bot.command()
async def meeting(ctx):
    if ctx.channel.id == 828691588766761021:
        await ctx.send(calService.getEvents(1))
    else:
        await ctx.send("Not in <#828691588766761021>")

bot.run(token)
